#!/usr/bin/env python3
"""
sync_docs.py — Incremental Documentation Sync for IPN Legacy Documentation Explorer

Detects which source files changed since last run using MD5 hashes, regenerates
documentation ONLY for those files, removes docs for deleted files, then rebuilds
SUMMARY.md and documentation.json.

Usage:
    python scripts/sync_docs.py              # Incremental: only process changes
    python scripts/sync_docs.py --full       # Full: force-regenerate all docs
    python scripts/sync_docs.py --dry-run    # Preview changes without writing anything

Requirements:
    pip install anthropic openai pyyaml

Environment variables:
    GH_READ_TOKEN         Read token for cloning/pulling source repos
    ANTHROPIC_API_KEY     API key when provider is "claude"
    OPENAI_API_KEY        API key when provider is "openai"

Config:
    Copy config.example.yaml to config.yaml and fill in your values.
"""

import os
import sys
import json
import hashlib
import subprocess
import shutil
import re
import argparse
import io
from pathlib import Path
from datetime import datetime, timezone

# Ensure stdout uses UTF-8 on Windows (handles emoji in node/python output)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Path setup
# ---------------------------------------------------------------------------
SCRIPTS_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

# Load .env from project root (so OPENAI_API_KEY / ANTHROPIC_API_KEY are available)
try:
    from dotenv import load_dotenv
    _env_file = PROJECT_ROOT / ".env"
    if _env_file.exists():
        load_dotenv(_env_file)
        print(f"[Env] Loaded {_env_file}")
except ImportError:
    pass  # python-dotenv not installed — rely on system env vars

try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False

# ---------------------------------------------------------------------------
# Import reusable parsers and utilities from generate_docs.py
# ---------------------------------------------------------------------------
try:
    from generate_docs import (
        RepoManager,
        PHPParser, JSParser, TypeScriptParser, VueParser,
        MDXParser, GherkinParser, GenericParser,
        MarkdownGenerator, ParserUtils,
    )
    GENERATE_DOCS_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import from generate_docs.py: {e}")
    print("Basic file processing will be used (no AI enhancement, no parsers).")
    GENERATE_DOCS_AVAILABLE = False

# ---------------------------------------------------------------------------
# Dual-provider AI Enhancer (Claude + OpenAI)
# ---------------------------------------------------------------------------
class DualAIEnhancer:
    """Generates documentation summaries using Claude (Anthropic) or OpenAI."""

    def __init__(self, config: dict):
        self.enabled = config.get("enabled", False)
        self.provider = config.get("provider", "claude").lower()
        self.model = config.get("model", "")
        self.client = None

        if not self.enabled:
            return

        api_key = self._resolve_env(config.get("api_key", ""))
        if not api_key:
            print(f"Warning: AI enhancement enabled but no API key found. Disabling.")
            self.enabled = False
            return

        if self.provider == "claude":
            try:
                from anthropic import Anthropic
                self.client = Anthropic(api_key=api_key)
                model = self.model or "claude-haiku-4-5-20251001"
                self.model = model
                print(f"[AI] Using Claude ({self.model})")
            except ImportError:
                print("Warning: 'anthropic' not installed. Run: pip install anthropic")
                self.enabled = False
            except Exception as e:
                print(f"Warning: Failed to init Claude client: {e}")
                self.enabled = False

        elif self.provider == "openai":
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=api_key)
                model = self.model or "gpt-4o-mini"
                self.model = model
                print(f"[AI] Using OpenAI ({self.model})")
            except ImportError:
                print("Warning: 'openai' not installed. Run: pip install openai")
                self.enabled = False
            except Exception as e:
                print(f"Warning: Failed to init OpenAI client: {e}")
                self.enabled = False
        else:
            print(f"Warning: Unknown AI provider '{self.provider}'. Use 'claude' or 'openai'.")
            self.enabled = False

    @staticmethod
    def _resolve_env(value: str) -> str:
        """Resolve ${ENV_VAR} syntax to actual environment variable values."""
        if value and value.startswith("${") and value.endswith("}"):
            env_var = value[2:-1]
            return os.environ.get(env_var, "")
        return value

    def _call_llm(self, prompt: str, max_tokens: int = 200) -> str:
        """Send a prompt to the configured LLM and return the response text."""
        try:
            if self.provider == "claude":
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.content[0].text.strip()

            elif self.provider == "openai":
                response = self.client.chat.completions.create(
                    model=self.model,
                    max_tokens=max_tokens,
                    messages=[{"role": "user", "content": prompt}],
                )
                return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"    [AI] LLM call failed: {e}")
        return ""

    def enhance_file_summary(self, file_path: str, code_snippet: str,
                              basic_summary: str, classes: list, functions: list) -> str:
        if not self.enabled:
            return basic_summary

        code_preview = code_snippet[:2000] if code_snippet else ""
        prompt = f"""Analyze this code file and provide a concise 2-3 sentence summary of its purpose and main functionality.

File: {file_path}
Classes: {', '.join(classes) if classes else 'None'}
Functions: {', '.join(functions[:10]) if functions else 'None'}

Code preview:
{code_preview}

Current basic summary: {basic_summary}

Provide a clear, technical summary. Focus on WHAT the code does and WHY it exists. Be specific about the domain/business logic."""

        result = self._call_llm(prompt, max_tokens=200)
        return result if result else basic_summary

    def enhance_function_doc(self, function_name: str, params: str,
                              code_snippet: str, basic_doc: str) -> str:
        if not self.enabled or not code_snippet:
            return basic_doc

        prompt = f"""Explain what this function does in 1 sentence. Be concise and technical.

Function: {function_name}({params})
Code:
{code_snippet[:500]}

Provide only the description, no preamble."""

        result = self._call_llm(prompt, max_tokens=100)
        return result if result else basic_doc


# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MANIFEST_FILE = PROJECT_ROOT / "docs_manifest.json"
CONFIG_FILE = PROJECT_ROOT / "config.yaml"

SUPPORTED_EXTENSIONS = {
    ".php", ".js", ".jsx", ".ts", ".tsx", ".vue",
    ".md", ".mdx", ".feature", ".twig", ".json",
    ".yaml", ".yml", ".xml", ".css", ".html", ".neon",
    ".sh", ".bash",
}

EXCLUDE_DIRS = {
    ".git", "node_modules", "vendor", "dist", "build",
    "__pycache__", ".idea", ".vscode", ".github",
}

# ---------------------------------------------------------------------------
# Manifest helpers
# ---------------------------------------------------------------------------
def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"repos": {}, "last_sync": None}


def save_manifest(manifest: dict):
    manifest["last_sync"] = datetime.now(timezone.utc).isoformat()
    with open(MANIFEST_FILE, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"[Manifest] Saved -> {MANIFEST_FILE.name}")


def file_md5(path: Path) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Repo scanning and change detection
# ---------------------------------------------------------------------------
def scan_repo(repo_path: Path, exclude_patterns: list) -> dict:
    """Scan all processable files in a repo. Returns {rel_path_str: md5}."""
    current = {}
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [
            d for d in dirs
            if d not in EXCLUDE_DIRS and d not in exclude_patterns
        ]
        for file in files:
            fp = Path(root) / file
            ext = fp.suffix.lower()
            is_dockerfile = fp.name.lower() in ("dockerfile",) or fp.name.lower().endswith(".dockerfile")
            if ext not in SUPPORTED_EXTENSIONS and not is_dockerfile:
                continue
            if any(pat in str(fp) for pat in exclude_patterns):
                continue
            try:
                rel = str(fp.relative_to(repo_path))
                current[rel] = file_md5(fp)
            except Exception:
                pass
    return current


def detect_changes(current: dict, previous: dict) -> tuple:
    """Returns (new_files, modified_files, deleted_files)."""
    new_files = [f for f in current if f not in previous]
    modified_files = [f for f in current if f in previous and current[f] != previous[f]]
    deleted_files = [f for f in previous if f not in current]
    return new_files, modified_files, deleted_files


# ---------------------------------------------------------------------------
# Doc name mapping — must match generate_docs.py convention
# ---------------------------------------------------------------------------
def source_to_doc_name(rel_path: str) -> str:
    """Convert a relative source path to its .md filename in output_dir."""
    normalized = rel_path.replace("\\", "_").replace("/", "_").replace(".", "_")
    return normalized + ".md"


# ---------------------------------------------------------------------------
# Fallback doc generator (no parser/AI)
# ---------------------------------------------------------------------------
def basic_generate_doc(file_path: Path, rel_path: str, output_path: Path):
    """Write a minimal .md for a file when parsers are unavailable."""
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        content = ""

    file_name = Path(rel_path).name
    rel_fwd = rel_path.replace("\\", "/")
    lines = [
        f"# {file_name}\n\n",
        f"**Path**: `{rel_fwd}`\n\n",
        "## Summary\n",
        f"Auto-generated documentation for `{file_name}`.\n\n",
    ]

    classes = re.findall(r"class\s+(\w+)", content)
    if classes:
        lines.append("## Classes\n")
        for cls in classes:
            lines.append(f"- `{cls}`\n")
        lines.append("\n")

    funcs = re.findall(r"function\s+(\w+)\s*\(", content)
    if funcs:
        lines.append("## Functions\n")
        for fn in funcs[:20]:
            lines.append(f"- `{fn}`\n")
        lines.append("\n")

    output_path.write_text("".join(lines), encoding="utf-8")


# ---------------------------------------------------------------------------
# SUMMARY.md rebuilder — scans output_dir, reads embedded **Path** metadata
# ---------------------------------------------------------------------------
def get_doc_category(path_str: str) -> str:
    p = path_str.lower()
    if "controller" in p:
        return "Controllers"
    if "entit" in p:
        return "Entities"
    if "repositor" in p:
        return "Repositories"
    if "service" in p:
        return "Services"
    if "command" in p:
        return "Commands"
    if "event" in p or "listener" in p:
        return "Events"
    if "plugin" in p:
        return "Plugins"
    return "Other"


def rebuild_summary(output_dir: Path, summary_path: Path):
    """
    Rebuild SUMMARY.md by reading **Path** metadata from every .md in output_dir.
    Writes both the root SUMMARY.md and public/docs/SUMMARY.md.
    """
    tree: dict = {}

    def add_to_tree(path_parts: list, link: str, category: str):
        if category not in tree:
            tree[category] = {}
        node = tree[category]
        start = 1 if path_parts and path_parts[0] in ("src", "app") else 0
        for part in path_parts[start:-1]:
            if not isinstance(node, dict):
                return
            if part not in node:
                node[part] = {}
            node = node[part]
        if isinstance(node, dict):
            node[path_parts[-1]] = link

    processed = 0
    for md_file in sorted(output_dir.glob("*.md")):
        if md_file.name == "SUMMARY.md":
            continue
        try:
            # Only read first 512 bytes — we only need the header
            header = md_file.read_text(encoding="utf-8", errors="ignore")[:512]
            match = re.search(r"\*\*Path\*\*:\s*`([^`]+)`", header)
            if not match:
                continue
            source_path = match.group(1).replace("\\", "/")
            parts = [p for p in source_path.split("/") if p]
            if not parts:
                continue
            category = get_doc_category(source_path)
            link = f"[{parts[-1]}]({md_file.name})"
            add_to_tree(parts, link, category)
            processed += 1
        except Exception as e:
            print(f"    Warning: Could not read {md_file.name}: {e}")

    # Render tree to SUMMARY.md lines
    def tree_to_lines(d: dict, level: int = 0) -> list:
        result = []
        indent = "  " * level
        for key in sorted(d.keys()):
            val = d[key]
            if isinstance(val, dict):
                result.append(f"{indent}- **{key}**")
                result.extend(tree_to_lines(val, level + 1))
            else:
                result.append(f"{indent}- {val}")
        return result

    lines = ["# Documentation Index\n"]
    priority = ["Controllers", "Services", "Entities", "Repositories",
                 "Commands", "Events", "Plugins", "Other"]
    for cat in priority:
        if cat in tree and tree[cat]:
            lines.append(f"## {cat}\n")
            lines.extend(tree_to_lines(tree[cat]))
            lines.append("\n")

    content = "\n".join(lines)
    summary_path.write_text(content, encoding="utf-8")
    print(f"[SUMMARY] Rebuilt {summary_path} ({processed} entries, {len(tree)} categories)")


# ---------------------------------------------------------------------------
# Per-repo sync
# ---------------------------------------------------------------------------
def sync_repo(
    repo_name: str,
    repo_path: Path,
    old_hashes: dict,
    output_dir: Path,
    ai_enhancer,
    parsers: dict,
    generator,
    exclude_patterns: list,
    dry_run: bool = False,
    full: bool = False,
) -> dict:
    """Process one repository. Returns updated hash dict."""

    print(f"\n{'='*50}")
    print(f"[Repo: {repo_name}] Scanning {repo_path}...")
    current_hashes = scan_repo(repo_path, exclude_patterns)

    if full:
        new_files = list(current_hashes.keys())
        modified_files = []
        deleted_files = list(old_hashes.keys())
        print(f"[Repo: {repo_name}] FULL mode — {len(new_files)} files to process")
    else:
        new_files, modified_files, deleted_files = detect_changes(current_hashes, old_hashes)
        print(f"[Repo: {repo_name}] Changes detected:")
        print(f"   + {len(new_files)} new")
        print(f"   ~ {len(modified_files)} modified")
        print(f"   - {len(deleted_files)} deleted")

    if not new_files and not modified_files and not deleted_files:
        print(f"[Repo: {repo_name}] No changes. Skipping.")
        return current_hashes

    if dry_run:
        def _show(label, items):
            for f in items[:5]:
                print(f"  {label} {f}")
            if len(items) > 5:
                print(f"  {label} ... ({len(items) - 5} more)")

        print("\n[DRY RUN] Would process:")
        _show("+", new_files)
        _show("~", modified_files)
        _show("-", deleted_files)
        return current_hashes

    # ---- Delete docs for removed source files ----
    for rel in deleted_files:
        doc_path = output_dir / source_to_doc_name(rel)
        if doc_path.exists():
            doc_path.unlink()
            print(f"  [Delete] {doc_path.name}")

    # ---- Clear stale docs for modified files (force regen) ----
    for rel in modified_files:
        doc_path = output_dir / source_to_doc_name(rel)
        if doc_path.exists():
            doc_path.unlink()

    # ---- Generate docs for new + modified files ----
    files_to_generate = new_files + modified_files
    print(f"\n[Repo: {repo_name}] Generating {len(files_to_generate)} docs...")

    for i, rel in enumerate(files_to_generate, 1):
        abs_path = repo_path / rel
        doc_name = source_to_doc_name(rel)
        doc_path = output_dir / doc_name

        print(f"  [{i}/{len(files_to_generate)}] {rel}")

        if not abs_path.exists():
            print(f"    Warning: Source file not found: {abs_path}")
            continue

        if GENERATE_DOCS_AVAILABLE and generator and parsers:
            ext = abs_path.suffix.lower()
            is_dockerfile = abs_path.name.lower() in ("dockerfile",) or abs_path.name.lower().endswith(".dockerfile")
            parser_key = "Dockerfile" if is_dockerfile else ext
            parser = parsers.get(parser_key)

            if parser:
                try:
                    content = abs_path.read_text(encoding="utf-8", errors="ignore")
                    info = parser.parse(content)

                    # AI-enhance summary if enabled
                    if ai_enhancer and ai_enhancer.enabled:
                        enhanced = ai_enhancer.enhance_file_summary(
                            rel,
                            content,
                            info.get("summary", ""),
                            info.get("classes", []),
                            list(info.get("methods", {}).keys()),
                        )
                        if enhanced:
                            info["summary"] = enhanced

                    # Write doc using MarkdownGenerator (it won't skip since we deleted first)
                    generator.generate(str(abs_path), info, str(repo_path), repo_name, content)
                except Exception as e:
                    print(f"    Warning: Parser failed for {rel}: {e}")
                    basic_generate_doc(abs_path, rel, doc_path)
            else:
                # No parser for this extension — write basic doc
                basic_generate_doc(abs_path, rel, doc_path)
        else:
            # generate_docs.py not available — use basic fallback
            basic_generate_doc(abs_path, rel, doc_path)

    return current_hashes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    arg_parser = argparse.ArgumentParser(
        description="Incremental documentation sync — only regenerates changed files."
    )
    arg_parser.add_argument("--full", action="store_true",
                            help="Force full regeneration of all docs")
    arg_parser.add_argument("--dry-run", action="store_true",
                            help="Show changes without writing anything")
    args = arg_parser.parse_args()

    print("=" * 60)
    print("IPN Documentation Sync")
    print("=" * 60)
    if args.full:
        print("Mode: FULL (regenerate all)")
    elif args.dry_run:
        print("Mode: DRY RUN (no writes)")
    else:
        print("Mode: INCREMENTAL (changed files only)")
    print()

    # ---- Dependency checks ----
    if not YAML_AVAILABLE:
        print("Error: 'pyyaml' not installed. Run: pip install pyyaml")
        sys.exit(1)

    if not CONFIG_FILE.exists():
        print(f"Error: config.yaml not found at {CONFIG_FILE}")
        print("Copy config.example.yaml to config.yaml and fill in your values.")
        sys.exit(1)

    # ---- Load config ----
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    output_dir = Path(config.get("output_dir", "./public/docs"))
    if not args.dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    exclude_patterns = config.get("exclude", [])

    # ---- Init AI enhancer ----
    ai_config = config.get("ai_enhancement", {})
    ai_enhancer = DualAIEnhancer(ai_config)

    # ---- Init parsers and generator (reuse generate_docs.py classes) ----
    generator = None
    parsers_map = None
    if GENERATE_DOCS_AVAILABLE:
        generator = MarkdownGenerator(str(output_dir), None)  # AI handled separately above
        parsers_map = {
            ".php": PHPParser(),
            ".js": JSParser(), ".jsx": JSParser(),
            ".ts": TypeScriptParser(), ".tsx": TypeScriptParser(),
            ".vue": VueParser(),
            ".md": MDXParser(), ".mdx": MDXParser(),
            ".feature": GherkinParser(),
            ".twig": GenericParser(), ".json": GenericParser(),
            ".yaml": GenericParser(), ".yml": GenericParser(),
            ".xml": GenericParser(), ".css": GenericParser(),
            ".html": GenericParser(), ".neon": GenericParser(),
            ".sh": GenericParser(), ".bash": GenericParser(),
            "Dockerfile": GenericParser(),
        }

    # ---- Load manifest ----
    manifest = load_manifest()
    if manifest.get("last_sync"):
        print(f"Last sync: {manifest['last_sync']}")
    else:
        print("No previous sync found — will treat all files as new.")
    print()

    # ---- Determine repos ----
    repos_cfg = config.get("repositories", [])
    if not repos_cfg:
        # Legacy single-repo fallback
        repos_cfg = [{
            "name": "main",
            "url": config.get("repo_url", ""),
            "local_path": config.get("local_path", "./repo_src"),
        }]

    # ---- Process each repo ----
    any_changes = False
    for repo in repos_cfg:
        repo_name = repo.get("name", "unknown")
        repo_url = repo.get("url", "")
        local_path = Path(repo.get("local_path") or f"repo_src/{repo_name}")
        token = os.environ.get("GH_READ_TOKEN", repo.get("token", ""))

        # Pull / clone the source repo
        if repo_url:
            print(f"[Setup] Pulling {repo_name} from {repo_url}...")
            if GENERATE_DOCS_AVAILABLE:
                rm = RepoManager(repo_name, repo_url, str(local_path), token)
                rm.setup()
            else:
                # Minimal git pull/clone without RepoManager
                git = shutil.which("git") or "git"
                auth_url = repo_url
                if token and "https://" in repo_url:
                    auth_url = repo_url.replace("https://", f"https://{token}@")
                if local_path.exists():
                    subprocess.run([git, "-C", str(local_path), "pull"], check=False)
                else:
                    subprocess.run([git, "clone", auth_url, str(local_path)], check=True)
        elif not local_path.exists():
            print(f"Error: Repository path {local_path} does not exist and no URL configured.")
            continue

        old_hashes = manifest.get("repos", {}).get(repo_name, {})

        updated_hashes = sync_repo(
            repo_name=repo_name,
            repo_path=local_path,
            old_hashes=old_hashes,
            output_dir=output_dir,
            ai_enhancer=ai_enhancer,
            parsers=parsers_map,
            generator=generator,
            exclude_patterns=exclude_patterns,
            dry_run=args.dry_run,
            full=args.full,
        )

        if not args.dry_run:
            manifest.setdefault("repos", {})[repo_name] = updated_hashes
            any_changes = True

    if args.dry_run:
        print("\n[DRY RUN] No files were written.")
        return

    if not any_changes:
        print("\nNothing changed.")
        return

    # ---- Save manifest ----
    save_manifest(manifest)

    # ---- Rebuild SUMMARY.md (root + public/docs/) ----
    print("\n[Step] Rebuilding SUMMARY.md...")
    root_summary = PROJECT_ROOT / "SUMMARY.md"
    rebuild_summary(output_dir, root_summary)

    docs_summary = output_dir / "SUMMARY.md"
    if docs_summary != root_summary:
        rebuild_summary(output_dir, docs_summary)

    # ---- Re-run generateDocsData.js ----
    print("\n[Step] Running generateDocsData.js...")
    node_bin = shutil.which("node") or "node"
    gen_script = PROJECT_ROOT / "scripts" / "generateDocsData.js"
    try:
        result = subprocess.run(
            [node_bin, str(gen_script)],
            cwd=str(PROJECT_ROOT),
            check=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )
        if result.stdout:
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        stderr = e.stderr or ""
        print(f"Warning: generateDocsData.js failed:\n{stderr}")
    except FileNotFoundError:
        print("Warning: 'node' not found in PATH. Run 'npm run generate-docs' manually.")

    print("\n" + "=" * 60)
    print("Sync complete.")
    print("=" * 60)


if __name__ == "__main__":
    main()
