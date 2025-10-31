@echo off
title MailMate - Windows Installer
color 0A

echo.
echo ========================================
echo    MAILMATE - AUTOMATED INSTALLER
echo ========================================
echo.
echo This script will:
echo  1. Create virtual environment
echo  2. Install all dependencies
echo  3. Set up project structure
echo.
pause

REM Check if Python is installed
echo.
echo [1/5] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)
echo [OK] Python is installed
python --version

REM Create virtual environment
echo.
echo [2/5] Creating virtual environment...
if exist venv (
    echo [WARNING] Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created
)

REM Activate virtual environment
echo.
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment!
    pause
    exit /b 1
)
echo [OK] Virtual environment activated

REM Upgrade pip
echo.
echo [4/5] Upgrading pip...
python -m pip install --upgrade pip --quiet
echo [OK] Pip upgraded

REM Install dependencies
echo.
echo [5/5] Installing dependencies...
echo This may take a few minutes...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies!
    pause
    exit /b 1
)
echo [OK] All dependencies installed

REM Create .streamlit folder if it doesn't exist
echo.
echo Creating .streamlit folder...
if not exist .streamlit mkdir .streamlit
echo [OK] Folder structure ready

REM Check if secrets.toml exists
echo.
if exist .streamlit\secrets.toml (
    echo [OK] secrets.toml already exists
) else (
    echo [WARNING] secrets.toml not found!
    echo.
    echo Creating template secrets file...
    (
        echo # Gemini API Key
        echo GEMINI_API_KEY = "your-gemini-api-key-here"
        echo.
        echo # Email credentials
        echo SENDER_EMAIL = "your-email@gmail.com"
        echo EMAIL_PASSWORD = "your-gmail-app-password"
        echo.
        echo # SMTP settings
        echo SMTP_SERVER = "smtp.gmail.com"
        echo SMTP_PORT = 587
    ) > .streamlit\secrets.toml
    echo [OK] Template created at .streamlit\secrets.toml
)

REM Display completion message
echo.
echo ========================================
echo    INSTALLATION COMPLETED!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. CONFIGURE API KEYS:
echo    - Edit .streamlit\secrets.toml
echo    - Add your Gemini API key
echo    - Add your Gmail credentials
echo.
echo 2. GET API KEYS:
echo    - Gemini: https://aistudio.google.com/app/apikey
echo    - Gmail: https://myaccount.google.com/apppasswords
echo.
echo 3. RUN THE APP:
echo    - Double-click run.bat
echo    - Or run: streamlit run main.py
echo.
echo ========================================

REM Open secrets.toml for editing
echo.
choice /C YN /M "Do you want to edit secrets.toml now"
if errorlevel 2 goto :skip_edit
if errorlevel 1 goto :edit_secrets

:edit_secrets
echo Opening secrets.toml in Notepad...
start notepad .streamlit\secrets.toml
goto :end

:skip_edit
echo You can edit it later: .streamlit\secrets.toml

:end
echo.
pause