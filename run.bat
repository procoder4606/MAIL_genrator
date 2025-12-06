@echo off
title MAIL-GENRATOR - Email Responder
color 0B

echo.
echo ========================================
echo         MAIL-GENRATOR - STARTING
echo ========================================
echo.

REM Check if virtual environment exists
if not exist venv (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run install.bat first.
    echo.
    pause
    exit /b 1
)

REM Check if secrets.toml exists
if not exist .streamlit\secrets.toml (
    echo [ERROR] secrets.toml not found!
    echo.
    echo Please configure your API keys in:
    echo .streamlit\secrets.toml
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Start Streamlit
echo Starting MAIL-GENRATOR...
echo.
echo The app will open in your browser automatically.
echo To stop the app, press Ctrl+C in this window.
echo.
echo ========================================
echo.

streamlit run main.py

REM If streamlit command fails
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to start application!
    echo.
    echo Possible solutions:
    echo  1. Run install.bat again
    echo  2. Check if dependencies are installed: pip list
    echo.
    pause
)
```

---

## 🎯 **How to Use These Files**

### **First Time Setup (One-time):**
1. **Double-click `install.bat`**
2. Wait 2-3 minutes for installation
3. Press **Y** when asked to edit secrets.toml
4. Add your API keys
5. Save and close

### **Every Time You Want to Use the App:**
1. **Double-click `run.bat`**
2. Browser opens automatically
3. Use the app
4. Press **Ctrl+C** in the black window to stop

---

## 📋 **What Each File Does**

### **`install.bat` does:**
- ✅ Checks if Python is installed
- ✅ Creates virtual environment (`venv` folder)
- ✅ Activates the virtual environment
- ✅ Upgrades pip to latest version
- ✅ Installs streamlit and google-generativeai
- ✅ Creates `.streamlit` folder
- ✅ Creates template `secrets.toml` file
- ✅ Opens secrets.toml for editing (optional)

### **`run.bat` does:**
- ✅ Checks if installation was completed
- ✅ Checks if secrets are configured
- ✅ Activates virtual environment
- ✅ Starts Streamlit app
- ✅ Opens browser automatically to localhost:8501

---

## ⚡ **Quick Visual Guide**

**Your workflow:**
```
Step 1: Double-click install.bat
   ↓
   Creates venv folder
   Installs packages
   Creates secrets.toml template
   ↓
Step 2: Edit secrets.toml with your keys
   ↓
Step 3: Double-click run.bat
   ↓
   App opens in browser!
```

---

## 🔧 **Troubleshooting**

### **Problem: "Python is not installed"**
```
[ERROR] Python is not installed or not in PATH!
```
**Fix:** Install Python from python.org and check "Add to PATH"

---

### **Problem: "Virtual environment not found"**
```
[ERROR] Virtual environment not found!
Please run install.bat first.
```
**Fix:** Run `install.bat` first before running `run.bat`

---

### **Problem: "secrets.toml not found"**
```
[ERROR] secrets.toml not found!
```
**Fix:** Edit `.streamlit\secrets.toml` and add your API keys

---

### **Problem: Nothing happens when double-clicking**
**Fix:** 
- Right-click → "Run as administrator"
- Or right-click → "Edit" to check the code is correct

---

## 💾 **Save These Files**

After creating both files, your folder should look like:
```
MAIL-GENRATOR/
├── agents/
│   └── email_agent.py
├── utils/
│   └── email_sender.py
├── main.py
├── requirements.txt
├── install.bat          ← You just created this
└── run.bat             ← You just created this