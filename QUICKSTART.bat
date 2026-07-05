@echo off
REM Offline Pentesting AI - Quick Start Script for Windows
REM This script automates the installation and setup process
REM Usage: QUICKSTART.bat

setlocal enabledelayedexpansion
cls

REM Colors (using PowerShell for colored output if available)
set "Green=[32m"
set "Red=[31m"
set "Yellow=[33m"
set "Blue=[34m"
set "NC=[0m"

echo.
echo ===============================================
echo Offline Pentesting AI - Quick Start Setup
echo ===============================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found
    echo Please install Python 3.9+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
) else (
    for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
    echo OK: Python !PYTHON_VERSION! found
)

REM Check Git installation
echo Checking Git installation...
git --version >nul 2>&1
if errorlevel 1 (
    echo WARNING: Git not found
    echo Please install from https://git-scm.com/download/win
    echo.
)

REM Check if in repository directory
if not exist ".git" (
    echo ERROR: Not in repository directory
    echo Please run this script from the project root directory
    pause
    exit /b 1
)

echo.
echo Setting up Python Virtual Environment...
if not exist "venv" (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Could not create virtual environment
        pause
        exit /b 1
    )
    echo OK: Virtual environment created
) else (
    echo OK: Virtual environment already exists
)

REM Activate virtual environment
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Could not activate virtual environment
    pause
    exit /b 1
)
echo OK: Virtual environment activated

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip setuptools wheel
if errorlevel 1 (
    echo WARNING: Could not upgrade pip
)

REM Install Python dependencies
echo.
echo Installing Python dependencies from requirements.txt...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Could not install dependencies
    pause
    exit /b 1
)
echo OK: Dependencies installed

REM Create directory structure
echo.
echo Creating directory structure...
for %%D in (
    cache
    exports
    sessions
    logs
    database\sqlite
    database\vectors
    database\cache
    reports\html
    reports\pdf
    reports\json
    models\local_llm
    models\embeddings
    knowledge
) do (
    if not exist "%%D" (
        mkdir "%%D"
        echo OK: Created %%D\
    ) else (
        echo OK: %%D\ already exists
    )
)

REM Create .env file
echo.
echo Creating environment configuration...
if not exist ".env" (
    (
        echo DEBUG=False
        echo LOG_LEVEL=INFO
        echo API_HOST=0.0.0.0
        echo API_PORT=8000
        echo OLLAMA_BASE_URL=http://localhost:11434
        echo OLLAMA_MODEL=mistral
        echo EMBEDDINGS_MODEL=nomic-embed-text
        echo DATABASE_URL=sqlite:///./database/sqlite/app.db
        echo VECTOR_DB_TYPE=chroma
        echo SECRET_KEY=your-secret-key-change-me
        echo ALLOWED_HOSTS=localhost,127.0.0.1
        echo REPORT_FORMAT=html,pdf,json
        echo REPORT_INCLUDE_EVIDENCE=true
    ) > .env
    echo OK: .env file created
) else (
    echo OK: .env file already exists
)

REM Test installation
echo.
echo Testing installation...
python -c "import fastapi; import ollama; print('OK: Core modules imported successfully')" >nul 2>&1
if errorlevel 1 (
    echo WARNING: Some modules may not be installed correctly
) else (
    echo OK: Core modules verified
)

REM Print next steps
echo.
echo ===============================================
echo Installation Complete! 
echo ===============================================
echo.
echo Next Steps:
echo.
echo 1. Install Ollama from: https://ollama.ai
echo.
echo 2. Start Ollama service (open new Command Prompt):
echo    ollama serve
echo.
echo 3. Pull a language model (in another Command Prompt):
echo    ollama pull mistral
echo.
echo 4. Run the application:
echo    python main.py
echo.
echo For more information, see:
echo   - README.md (Overview and features)
echo   - INSTALL.md (Detailed installation guide)
echo   - GETTING_STARTED.md (Quick start guide)
echo.
echo WARNING: This tool is for educational purposes only!
echo Only test systems you own or have explicit permission to test.
echo.

pause
