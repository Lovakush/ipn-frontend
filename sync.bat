@echo off
setlocal EnableDelayedExpansion

echo ============================================================
echo   IPN Documentation Sync
echo ============================================================
echo.

REM ---- Check Python ----
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python not found in PATH.
    echo Please install Python 3.x from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

REM ---- Check config.yaml ----
if not exist "%~dp0config.yaml" (
    echo ERROR: config.yaml not found.
    echo.
    echo Please create it by copying config.example.yaml:
    echo   copy config.example.yaml config.yaml
    echo.
    echo Then fill in your repository URLs and API keys.
    pause
    exit /b 1
)

REM ---- Install Python dependencies (silent if already installed) ----
echo [Setup] Installing/verifying Python dependencies...
pip install anthropic openai google-generativeai pyyaml python-dotenv -q --disable-pip-version-check
if %errorlevel% neq 0 (
    echo WARNING: pip install had issues. Attempting to continue...
)
echo.

REM ---- Run sync ----
echo [Sync] Starting documentation sync...
echo.
python "%~dp0scripts\sync_docs.py" %*

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Sync failed with exit code %errorlevel%.
    pause
    exit /b %errorlevel%
)

echo.

REM ---- Git commit and push ----
echo [Git] Checking for changes to commit...
cd /d "%~dp0"

git add public\docs\ src\data\documentation.json public\data\documentation.json SUMMARY.md docs_manifest.json 2>nul

git diff --cached --quiet
if %errorlevel% neq 0 (
    echo [Git] Committing changes...
    for /f "tokens=1-3 delims=/ " %%a in ("%date%") do set TODAY=%%c-%%a-%%b
    for /f "tokens=1-2 delims=: " %%a in ("%time%") do set NOW=%%a:%%b
    git commit -m "docs: auto-sync documentation [!TODAY! !NOW!]"

    echo [Git] Pushing to remote...
    git push
    if %errorlevel% neq 0 (
        echo ERROR: git push failed. Check your credentials and remote URL.
        pause
        exit /b 1
    )
    echo [Git] Pushed! CI/CD pipeline will now build and deploy to Azure automatically.
) else (
    echo [Git] No changes detected. Nothing to push.
)

echo.
echo Done! Press any key to close.
pause >nul
