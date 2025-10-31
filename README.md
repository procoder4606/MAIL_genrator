# MailMate - AI Email Response Generator

Automatically generate and send professional email responses using Google Gemini AI.

## Features
- AI-powered email response generation
- Multiple tone options (Professional, Friendly, Apologetic, Persuasive)
- Direct email sending via Gmail SMTP
- Clean Streamlit web interface

## Setup Instructions

### 1. Install Python
Download Python 3.8+ from [python.org](https://www.python.org/downloads/)

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.\venv\Scripts\Activate
```


### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Secrets
Create `.streamlit/secrets.toml` with your credentials:
```toml
GEMINI_API_KEY = "your-gemini-api-key"
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

**Get API Keys:**
- Gemini: [Google AI Studio](https://aistudio.google.com/app/apikey)
- Gmail App Password: [Google Account Security](https://myaccount.google.com/apppasswords)

### 6. Run Application
```bash
streamlit run main.py
```

Visit `http://localhost:8501` in your browser.

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- SMTP

## Security
⚠️ Never commit your `secrets.toml` file or share API keys publicly!

