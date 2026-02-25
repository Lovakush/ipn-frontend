# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**IPN Legacy Documentation Explorer** — a React/TypeScript SPA that provides authenticated browsing of 4,500+ auto-generated markdown documentation files from a PHP/Symfony backend and Vue/Nuxt frontend codebase.

## Commands

```bash
npm install                  # Install dependencies
npm run generate-docs        # Parse SUMMARY.md → documentation.json (run after any SUMMARY.md change)
npm run dev                  # generate-docs + vite dev server at http://localhost:5173
npm run build                # generate-docs + vite build → dist/
```

No test suite is configured. To add one: `npm install -D vitest @testing-library/react @testing-library/jest-dom`

## Architecture

### Data Pipeline

`SUMMARY.md` (6,472-line doc index) → `scripts/generateDocsData.js` → two output files:
- `src/data/documentation.json` (build-time import)
- `public/data/documentation.json` (runtime fetch)

The script categorizes files by extension: `.php` → backend, `.js/.ts/.tsx/.jsx/.vue/.json` → frontend, rest → other. **Always run `npm run generate-docs` before dev/build or after modifying SUMMARY.md.**

### Authentication Flow

Firebase email/password auth. `AuthContext` (`src/contexts/AuthContext.tsx`) exposes `currentUser`, `isAuthenticated`, `loading`, `login()`, `logout()`. `ProtectedRoute` (`src/components/ProtectedRoute.tsx`) guards all routes except `/` (Login). The context renders `null` while loading to prevent flashes.

### Routing

| Path | Component | Protected |
|------|-----------|-----------|
| `/` | Login | No |
| `/home` | Home | Yes |
| `/explore` | Explore | Yes |
| `/overview` | Overview | Yes |
| `/docs` | Documentation | Yes |
| `/admin` | AdminPanel | Yes |

Routes defined in `src/App.tsx`. `src/router.tsx` also exists but is the alternative/unused config.

### Component Organization

- `src/app/components/ui/` — 40+ shadcn/ui components (Radix UI primitives)
- `src/components/` — shared layout components (Navigation, Footer, ProtectedRoute)
- `src/pages/` — route-level page components
- `src/app/components/figma/` — Figma-specific components

### Styling

- **Tailwind CSS v4** — configured CSS-first in `src/styles/theme.css` (not `tailwind.config.js`)
- CSS variables and light/dark mode defined in `src/styles/theme.css`
- Brand color: `#024639` (emerald); frontend badge: `blue-600`; other badge: `gray-600`
- Use `cn()` from `src/app/components/ui/utils.ts` for conditional class merging

### Path Alias

`@/` maps to `src/` (configured in both `vite.config.ts` and `tsconfig.json`).

## Environment Variables

Required in `.env` for Firebase Auth:
```
VITE_FIREBASE_API_KEY
VITE_FIREBASE_AUTH_DOMAIN
VITE_FIREBASE_PROJECT_ID
VITE_FIREBASE_STORAGE_BUCKET
VITE_FIREBASE_MESSAGING_SENDER_ID
VITE_FIREBASE_APP_ID
VITE_FIREBASE_MEASUREMENT_ID
```

## Incremental Doc Sync

Regenerates documentation only for files that changed since the last run.

```bash
# Windows (local dev)
python scripts/sync_docs.py              # incremental — only changed files
python scripts/sync_docs.py --dry-run   # preview changes without writing
python scripts/sync_docs.py --full      # force-regenerate all docs

# Linux / Azure terminal
python3 scripts/sync_docs.py
npm run sync-docs                        # same as above via npm
```

**How it works:**
1. Pulls/clones source repos via `GITHUB_TOKEN` (read token)
2. Computes MD5 of each source file, compares to `docs_manifest.json`
3. For deleted files → removes their `.md` from `public/docs/`
4. For modified/new files → calls LLM to regenerate `.md`
5. Rebuilds root `SUMMARY.md` and `public/docs/SUMMARY.md`
6. Runs `generateDocsData.js` to update `documentation.json`
7. Saves updated `docs_manifest.json`

**Required setup:**
1. `cp config.example.yaml config.yaml` and fill in repo URLs and API key
2. `pip install anthropic openai pyyaml`
3. Set env vars: `GITHUB_TOKEN` (repo read access), and either `ANTHROPIC_API_KEY` or `OPENAI_API_KEY`

**AI providers** (configured in `config.yaml`):
- `provider: claude` + `model: claude-haiku-4-5-20251001` ← recommended (fast, low cost)
- `provider: openai` + `model: gpt-4o-mini`

**Key files:**
- [scripts/sync_docs.py](scripts/sync_docs.py) — main sync script
- [config.example.yaml](config.example.yaml) — config template
- `docs_manifest.json` — auto-generated hash manifest (gitignore this)

## Deployment

Deployed to Vercel. `vercel.json` rewrites all routes to `index.html` for SPA routing. Build output is `dist/`. Documentation `.md` files are served at runtime from `public/docs/`.
