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
pip install anthropic openai pyyaml python-dotenv -q --disable-pip-version-check
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
echo Done! Press any key to close.
pause >nul
