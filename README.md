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

AI-powered email response generatorShareSGwhat does this project do explain in bullet points import streamlit as st
import openai
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:
Email:
{email_text}
Reply:
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
import smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(recipient, body):
    try:
        sender_email = st.secrets["SENDER_EMAIL"]
        sender_password = st.secrets["EMAIL_PASSWORD"]
        smtp_server = st.secrets.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = st.secrets.get("SMTP_PORT", 587)
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Response To Your Email"
        message.attach(MIMEText(body, "plain"))
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email
st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("📧 MailMate – Think Less, Send Smart")
email_text = st.text_area("Paste the email content you received:", height=300)
recipient_email = st.text_input("Recipient Email Address")
tone = st.selectbox("Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])
if st.button("Generate & Send Email"):
    if not recipient_email:
        st.warning("Please enter the recipient's email address.")
    else:
        with st.spinner("Generating and sending email..."):
            response = generate_email_response(email_text, tone)
            send_status = send_email(recipient_email, response)
            st.subheader("✉️ Response")
            st.markdown(response, unsafe_allow_html=True)
            if send_status:
                st.success(f"Email sent successfully to {recipient_email}")
            else:
                st.error("Failed to send the email.")
streamlit
openai>=1.0.0Show moreThis project is an automated email response generator and sender built with Streamlit. Here's what it does:
Core Functionality

Generates AI-powered email replies using OpenAI's GPT-4 model based on incoming email content
Automatically sends the generated response via SMTP email to specified recipients
Customizes tone of replies (Professional, Friendly, Apologetic, or Persuasive)

Key Components
Email Generation (email_agent.py)

Uses OpenAI API to craft contextual email responses
Takes the original email text and desired tone as input
Returns AI-generated reply text

Email Sending (email_sender.py)

Connects to SMTP server (default: Gmail) to send emails
Uses credentials stored in Streamlit secrets
Handles authentication and message formatting

User Interface (app.py)

Provides a web interface titled "MailMate – Think Less, Send Smart"
Input fields for: original email content, recipient address, and response tone
Single-button operation to generate and send responses
Displays the generated response before sending
Shows success/error notifications

Technical Details

Built with Streamlit for the web interface
Uses OpenAI GPT-4 for natural language generation
Requires API keys and email credentials stored in st.secrets
Dependencies: streamlit and openai>=1.0.0

Use Case
Streamlines email communication by automatically drafting and sending professional replies, saving time on routine correspondence.RetrySGcan i use google gemini api key for thisYes, you can use Google Gemini API instead of OpenAI, but you'll need to modify the code. Here's what needs to change:
Required Changes
1. Update Dependencies (requirements.txt)
streamlit
google-generativeai
2. Modify email_agent.py
Replace the OpenAI code with Gemini:
pythonimport streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:
Email:
{email_text}
Reply:
"""
    model = genai.GenerativeModel('gemini-1.5-flash')  # or 'gemini-1.5-pro'
    response = model.generate_content(prompt)
    return response.text
3. Update Secrets Configuration
In your .streamlit/secrets.toml file:
tomlGEMINI_API_KEY = "your-gemini-api-key-here"
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
Key Differences

API syntax: Gemini uses generate_content() instead of chat.completions.create()
Model names: Use gemini-1.5-flash (faster/cheaper) or gemini-1.5-pro (more capable)
Cost: Gemini has a free tier with generous limits, making it more cost-effective for testing

The rest of the code (email sending and Streamlit UI) remains unchanged. Would you like me to create the complete modified version?RetrySGhow to  run in your local computerHere's how to run this project on your local computer:
Step 1: Install Python

Download and install Python 3.8+ from python.org
Verify installation: Open terminal/command prompt and type python --version

Step 2: Create Project Structure
Create a folder with this structure:
email-responder/
├── app.py
├── requirements.txt
├── agents/
│   └── email_agent.py
├── utils/
│   └── email_sender.py
└── .streamlit/
    └── secrets.toml
Step 3: Install Dependencies
Open terminal in your project folder and run:
bashpip install streamlit openai
Or if using Gemini:
bashpip install streamlit google-generativeai
Step 4: Set Up Secrets File
Create .streamlit/secrets.toml with your credentials:
toml# For OpenAI version
OPENAI_API_KEY = "sk-your-openai-key-here"

# For Gemini version
GEMINI_API_KEY = "your-gemini-key-here"

# Email credentials (required for both)
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Step 5: Get API Keys
For Gemini (Free tier available):

Go to Google AI Studio
Click "Get API Key"
Copy your key

For Gmail App Password:

Go to your Google Account settings
Security → 2-Step Verification → App passwords
Generate a new app password for "Mail"
Copy the 16-character password

Step 6: Run the Application
In terminal, navigate to your project folder and run:
bashstreamlit run app.py
Step 7: Access the App

Your browser will automatically open
Or manually go to: http://localhost:8501

Troubleshooting Tips

Port already in use: Run streamlit run app.py --server.port 8502
Module not found: Make sure you're in the correct folder and installed dependencies
Email sending fails: Check if "Less secure app access" is enabled or use App Password
Secrets not found: Ensure .streamlit/secrets.toml is in the right location

Would you like help with any specific step?RetrySGPS C:\Users\shlok\Desktop\shlok and aahand\MailMate> tree /F
>> 
Folder PATH listing
Volume serial number is 649F-5B93
C:.
│   .DS_Store
│   main.py
│   requirements.txt
│   
├───agents
│       email_agent.py
│       
└───utils
        email_sender.pyShow moreGood! Your project structure looks correct. Now follow these steps to run it:
Step 1: Create the Secrets File
You're missing the .streamlit folder. Create it:
bashmkdir .streamlit
Then create a file .streamlit\secrets.toml with your API keys:
toml# Choose one - OpenAI or Gemini
GEMINI_API_KEY = "your-gemini-api-key-here"
# or
OPENAI_API_KEY = "your-openai-api-key-here"

# Email credentials (required)
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Step 2: Install Dependencies
Run in your PowerShell:
bashpip install -r requirements.txt
Step 3: Check Your Main File
Your main file is named main.py instead of app.py. That's fine! Just make sure it contains the Streamlit UI code.
Step 4: Run the Application
bashstreamlit run main.py
```

## Expected Output
You should see something like:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
If You Get Errors:
"No module named 'streamlit'":
bashpip install streamlit openai
"Secrets file not found":

Make sure .streamlit\secrets.toml exists in C:\Users\shlok\Desktop\shlok and aahand\MailMate\.streamlit\

Want to verify your structure is complete?
Run this to see if secrets folder exists:
bashtree /F
The output should show .streamlit\secrets.toml
Need help with any specific step?RetrySGinstall using virual environomentHere's how to set up and run the project using a virtual environment:
Step 1: Create Virtual Environment
In PowerShell, navigate to your project folder:
bashcd "C:\Users\shlok\Desktop\shlok and aahand\MailMate"
Create the virtual environment:
bashpython -m venv venv
Step 2: Activate Virtual Environment
bash.\venv\Scripts\Activate
```

Your prompt should now show `(venv)` at the beginning:
```
(venv) PS C:\Users\shlok\Desktop\shlok and aahand\MailMate>
Step 3: Install Dependencies
bashpip install -r requirements.txt
Step 4: Create Secrets File
Create the .streamlit folder and secrets file:
bashmkdir .streamlit
Then create .streamlit\secrets.toml file with:
toml# For Gemini API
GEMINI_API_KEY = "your-gemini-api-key-here"

# Email credentials
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Step 5: Run the Application
bashstreamlit run main.py
Step 6: Deactivate (When Done)
To exit the virtual environment:
bashdeactivate
```

## Your Complete Project Structure Should Be:
```
MailMate/
├── venv/                    # Virtual environment (created)
├── .streamlit/
│   └── secrets.toml        # Your API keys
├── agents/
│   └── email_agent.py
├── utils/
│   └── email_sender.py
├── main.py
└── requirements.txt
Troubleshooting
"Activate.ps1 cannot be loaded" error:
Run PowerShell as Administrator and execute:
bashSet-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Then try activating again.
Want to verify virtual environment is active?
bashwhere python
Should show path to venv\Scripts\python.exe
Ready to run? Let me know if you hit any errors! 🚀RetrySGPerfect! You've successfully generated both credentials. Now let's add them to your project:
Update Your .streamlit\secrets.toml File
Create or edit the file .streamlit\secrets.toml in your MailMate folder with these credentials:
toml# Gemini API Key (from Image 2)
GEMINI_API_KEY = "your-actual-gemini-api-key-here"

# Email credentials (from Image 1)
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "dyuw tbtt ybfj olpc"

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Important Notes:

Copy your actual Gemini API key - In Image 2, click the copy icon next to the API key (the square icon with two overlapping squares) and paste it in the secrets file
Gmail App Password - Use exactly as shown: dyuw tbtt ybfj olpc (with spaces, as Google provides it)
Your email address - Replace your-email@gmail.com with your actual Gmail address

Complete Setup Steps:
bash# 1. Make sure you're in the virtual environment
.\venv\Scripts\Activate

# 2. Verify the secrets file exists
type .streamlit\secrets.toml

# 3. Run the application
streamlit run main.py
Security Reminder:
⚠️ Never share or commit the secrets.toml file to GitHub or any public repository! Add it to .gitignore:
bashecho .streamlit/ >> .gitignore
Ready to run? Let me know if you need help with anything! 🚀RetrySGAIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIgGreat! Now create your .streamlit\secrets.toml file with all the credentials:
Create the Secrets File
In PowerShell, run:
bashmkdir .streamlit
notepad .streamlit\secrets.toml
Then paste this content:
toml# Gemini API Key
GEMINI_API_KEY = "AIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIg"

# Email credentials
SENDER_EMAIL = "your-actual-email@gmail.com"
EMAIL_PASSWORD = "dyuw tbtt ybfj olpc"

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Important: Replace your-actual-email@gmail.com with the Gmail address you used to generate the app password.
Save and close Notepad (Ctrl+S, then close).
Now Run Your Application
bash# Make sure virtual environment is active
.\venv\Scripts\Activate

# Run the app
streamlit run main.py
Security Warning ⚠️
Since you've posted your API key publicly here, I recommend:

Regenerate your Gemini API key after testing:

Go to Google AI Studio
Delete the current key
Create a new one


Add to .gitignore to prevent accidentally sharing it:

bashecho .streamlit/ >> .gitignore
Your app should now work! Let me know if you see any errors when you run it. 🚀RetrySGshlokkumar4606@gmail.comPerfect! Now update your .streamlit\secrets.toml file with the complete information:
Final .streamlit\secrets.toml Configuration
toml# Gemini API Key
GEMINI_API_KEY = "AIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIg"

# Email credentials
SENDER_EMAIL = "shlokkumar4606@gmail.com"
EMAIL_PASSWORD = "dyuw tbtt ybfj olpc"

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
Now Run Your Application
bash# Make sure you're in the project directory
cd "C:\Users\shlok\Desktop\shlok and aahand\MailMate"

# Activate virtual environment
.\venv\Scripts\Activate

# Run the app
streamlit run main.py
Your app should now:
✅ Generate email responses using Gemini AI
✅ Send emails from shlokkumar4606@gmail.com
✅ Open in your browser at http://localhost:8501
🔒 CRITICAL Security Actions (Do This NOW):
Since you've posted sensitive credentials publicly:

Regenerate Gemini API Key immediately:

Go to https://aistudio.google.com/app/apikey
Delete the key ending in ...PUvIg
Create a new one


Regenerate Gmail App Password:

Go to https://myaccount.google.com/apppasswords
Delete the "Mail" app password
Generate a new one


Update your secrets.toml with the new keys

Never share API keys or passwords publicly! Let me know once the app is running! 🚀RetrySGwhy no colourThe lack of syntax highlighting (colors) in your secrets.toml file is normal in VS Code. TOML files don't have syntax highlighting by default unless you install an extension.
To Add Color Syntax (Optional):

Install TOML Language Support:

Press Ctrl + Shift + X (Extensions)
Search for "Even Better TOML"
Click Install


Or just continue without it - the file will work perfectly fine without colors!


More Important: Run Your Application!
Your secrets.toml looks perfect. Now let's run the app:
bash# In the terminal at the bottom, type:
streamlit run main.py
```

You should see output like:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
Your browser will automatically open with the MailMate application! 🚀

If You Get an Error:
"ModuleNotFoundError" - Install dependencies:
bashpip install streamlit google-generativeai
"Virtual environment not activated" - The (venv) should show before PS:
bash.\venv\Scripts\Activate
Try running it now and let me know what happens!RetrySGwhat actually this project do in bullet pointsWhat This MailMate Project Actually Does:
Core Purpose:

Automatically writes email replies for you using AI (Google Gemini)
Sends the generated email directly from your Gmail account

Step-by-Step Workflow:

User pastes an email they received into a text box
User enters recipient's email address (where to send the reply)
User selects the tone (Professional, Friendly, Apologetic, or Persuasive)
Click "Generate & Send Email" button
AI reads the original email and writes an appropriate response in the chosen tone
Shows you the generated reply on screen
Automatically sends the email from your Gmail (shlokkumar4606@gmail.com) to the recipient
Confirms if sent successfully or shows an error

Real-World Use Cases:

Reply to customer support emails quickly
Respond to meeting requests professionally
Handle routine correspondence without typing from scratch
Save time on repetitive email responses
Maintain consistent tone across communications

Technical Summary:

Frontend: Streamlit web interface (runs in browser)
AI Brain: Google Gemini API (generates intelligent responses)
Email Sending: SMTP protocol through Gmail
One-click operation: Generate + Send combined in single button

Bottom Line:
It's an AI email assistant that reads incoming emails, writes contextually appropriate responses in your chosen tone, and automatically sends them - saving you time and effort! ⚡📧RetrySG(venv) Pstreamlit run main.pytop\shlok and aahand\MailMate>
      👋 Welcome to Streamlit!
      If you'd like to receive helpful onboarding emails, news, offers, promotions,
      and the occasional swag, please enter your email address below. Otherwise,
      leave this field blank.
      Email:Great! Streamlit is starting up. Here's what to do:
At the Email Prompt:
Option 1 (Recommended): Just press Enter to skip

You don't need to enter anything
The app will start immediately

Option 2: Enter your email if you want Streamlit updates

Type your email and press Enter
You'll get tips and news from Streamlit


What Happens Next:
After you press Enter, you'll see:
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
Your browser will automatically open with the MailMate application! 🎉

What You'll See in the Browser:
📧 MailMate – Think Less, Send Smart

A large text area to paste email content
An input field for recipient's email address
A dropdown to select tone (Professional/Friendly/Apologetic/Persuasive)
A "Generate & Send Email" button


Just press Enter now and your app will launch! Let me know when you see the interface! 🚀RetrySGgoogle.api_core.exceptions.NotFound: 404 models/gemini-1.5-flash is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 129, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\main.py", line 17, in <module>
    response = generate_email_response(email_text, tone)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\agents\email_agent.py", line 15, in generate_email_response
    response = model.generate_content(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\generativeai\generative_models.py", line 331, in generate_content
    response = self._client.generate_content(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\ai\generativelanguage_v1beta\services\generative_service\client.py", line 835, in generate_content
    response = rpc(
               ^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\gapic_v1\method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 294, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 156, in retry_target
    next_sleep = _retry_error_helper(
                 ^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_base.py", line 214, in _retry_error_helper
    raise final_exc from source_exc
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 147, in retry_target
    result = target()
             ^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\timeout.py", line 130, in func_with_timeout
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\grpc_helpers.py", line 77, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from excShow moreThe error shows that the Gemini model name is incorrect. Let's fix your email_agent.py file:
Fix the Model Name
Open agents\email_agent.py and update it:
pythonimport streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:
Email:
{email_text}
Reply:
"""
    # CHANGE THIS LINE - Remove the version number
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
The key change: Replace gemini-1.5-flash with gemini-pro
Alternative Models You Can Use:
If gemini-pro doesn't work, try these:

gemini-1.5-pro-latest
gemini-1.5-flash-latest
models/gemini-pro

After Making Changes:

Save the file (Ctrl + S)
Go back to your browser where Streamlit is running
Click "Always rerun" (Streamlit will detect the changes automatically)

Or stop and restart in terminal:
bash# Press Ctrl + C to stop
# Then run again:
streamlit run main.py
Try it now and let me know if it works! 🚀RetrySGgoogle.api_core.exceptions.NotFound: 404 models/gemini-pro is not found for API version v1beta, or is not supported for generateContent. Call ListModels to see the list of available models and their supported methods.
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 129, in exec_func_with_error_handling
    result = func()
             ^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\streamlit\runtime\scriptrunner\script_runner.py", line 669, in code_to_exec
    exec(code, module.__dict__)  # noqa: S102
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\main.py", line 17, in <module>
    response = generate_email_response(email_text, tone)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\agents\email_agent.py", line 16, in generate_email_response
    response = model.generate_content(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\generativeai\generative_models.py", line 331, in generate_content
    response = self._client.generate_content(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\ai\generativelanguage_v1beta\services\generative_service\client.py", line 835, in generate_content
    response = rpc(
               ^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\gapic_v1\method.py", line 131, in __call__
    return wrapped_func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 294, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 156, in retry_target
    next_sleep = _retry_error_helper(
                 ^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_base.py", line 214, in _retry_error_helper
    raise final_exc from source_exc
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\retry\retry_unary.py", line 147, in retry_target
    result = target()
             ^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\timeout.py", line 130, in func_with_timeout
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
File "C:\Users\shlok\Desktop\shlok and aahand\MailMate\venv\Lib\site-packages\google\api_core\grpc_helpers.py", line 77, in error_remapped_callable
    raise exceptions.from_grpc_error(exc) from excShow moreThe issue is that your API key might be for Google AI Studio (free tier) which has different model names. Let's check and fix this:
Update email_agent.py with the correct model name:
pythonimport streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:
Email:
{email_text}
Reply:
"""
    # Try this model name for free tier API
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
If that still doesn't work, let's check which models are available:
Create a test file test_models.py in your MailMate folder:
pythonimport google.generativeai as genai

# Your API key
genai.configure(api_key="AIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIg")

# List all available models
print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  - {model.name}")
Run it:
bashpython test_models.py
This will show you the exact model names available for your API key. Copy one of the model names and use it in your email_agent.py.
Let me know what models it shows! 🔍RetrySGhow to create a test fileCreate the Test File:
Method 1: Using VS Code (Easiest)

In VS Code, click on the MailMate folder in the left sidebar
Click the "New File" icon (📄 with a +)
Name it: test_models.py
Paste this code:

pythonimport google.generativeai as genai

# Your API key
genai.configure(api_key="AIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIg")

# List all available models
print("Available models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"  - {model.name}")

Save it (Ctrl + S)


Method 2: Using PowerShell
bash# In your terminal (make sure you're in MailMate folder)
notepad test_models.py
When Notepad opens:

Paste the code above
Click File → Save
Close Notepad


Run the Test File:
In your VS Code terminal (bottom panel):
bash# Make sure virtual environment is active (you should see (venv))
python test_models.py
```

It will print a list of available Gemini models like:
```
Available models:
  - models/gemini-1.5-flash
  - models/gemini-1.5-pro
  - models/gemini-pro
Copy one of these model names and we'll use it in your email_agent.py!
What models does it show? 📋RetrySGvenv) PS C:\Users\shlok\Desktop\shlok and aahand\MailMate> python test_models.py
Available models:
  - models/gemini-2.5-pro-preview-03-25
  - models/gemini-2.5-flash-preview-05-20
  - models/gemini-2.5-flash
  - models/gemini-2.5-flash-lite-preview-06-17      
  - models/gemini-2.5-pro-preview-05-06
  - models/gemini-2.5-pro-preview-06-05
  - models/gemini-2.5-pro
  - models/gemini-2.0-flash-exp
  - models/gemini-2.0-flash
  - models/gemini-2.0-flash-001
  - models/gemini-2.0-flash-exp-image-generation    
  - models/gemini-2.0-flash-lite-001
  - models/gemini-2.0-flash-lite
  - models/gemini-2.0-flash-preview-image-generation
  - models/gemini-2.0-flash-lite-preview-02-05      
  - models/gemini-2.0-flash-lite-preview
  - models/gemini-2.0-pro-exp
  - models/gemini-2.0-pro-exp-02-05
  - models/gemini-exp-1206
  - models/gemini-2.0-flash-thinking-exp-01-21      
  - models/gemini-2.0-flash-thinking-exp
  - models/gemini-2.0-flash-thinking-exp-1219       
  - models/gemini-2.5-flash-preview-tts
  - models/gemini-2.5-pro-preview-tts
  - models/learnlm-2.0-flash-experimental
  - models/gemma-3-1b-it
  - models/gemma-3-4b-it
  - models/gemma-3-12b-it
  - models/gemma-3-27b-it
  - models/gemma-3n-e4b-it
  - models/gemma-3n-e2b-it
  - models/gemini-flash-latest
  - models/gemini-flash-lite-latest
  - models/gemini-pro-latest
  - models/gemini-2.5-flash-lite
  - models/gemini-2.5-flash-image-preview
  - models/gemini-2.5-flash-image
  - models/gemini-2.5-flash-preview-09-2025
  - models/gemini-2.5-flash-lite-preview-09-2025    
  - models/gemini-robotics-er-1.5-preview
  - models/gemini-2.5-computer-use-preview-10-2025  
(venv) PS C:\Users\shlok\Desktop\shlok and aahand\MailMate>Show morePerfect! Now update your email_agent.py file with a working model:
Update agents\email_agent.py:
Open the file in VS Code and change it to:
pythonimport streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:
Email:
{email_text}
Reply:
"""
    # Use the correct model name from your available models
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text
Key change: Line 15 now uses 'gemini-2.5-flash' (one of the fastest and most efficient models from your list)
Save and Restart:

Save the file (Ctrl + S)
Go back to your browser where Streamlit is running
It should auto-reload, or click "Always rerun"

Or restart in terminal:
bash# Press Ctrl + C to stop
streamlit run main.py
Now Try Using the App:

Paste an email in the text area
Enter a recipient email
Choose a tone
Click "Generate & Send Email"

It should work now! 🎉 Let me know what happens!RetrySGmake gitigonor file and how to post it o n githubStep 1: Create .gitignore File
In VS Code:

Click on MailMate folder
Click "New File" icon
Name it: .gitignore
Paste this content:

# Virtual Environment
venv/
env/
ENV/

# Streamlit Secrets (IMPORTANT - contains API keys!)
.streamlit/
secrets.toml

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Test files
test_models.py

# Logs
*.log

Save it (Ctrl + S)


Step 2: Initialize Git Repository
In your VS Code terminal:
bash# Make sure you're in the MailMate folder
cd "C:\Users\shlok\Desktop\shlok and aahand\MailMate"

# Initialize git
git init

# Add all files (except those in .gitignore)
git add .

# Create first commit
git commit -m "Initial commit: MailMate email responder"

Step 3: Create GitHub Repository

Go to github.com
Click the "+" icon (top right) → "New repository"
Fill in:

Repository name: MailMate
Description: "AI-powered email response generator using Gemini API"
Keep it Public or Private (your choice)
DON'T check "Initialize with README" (you already have files)


Click "Create repository"


Step 4: Push to GitHub
GitHub will show you commands. Use these in your terminal:
bash# Add GitHub as remote
git remote add origin https://github.com/YOUR-USERNAME/MailMate.git

# Push your code
git branch -M main
git push -u origin main
Replace YOUR-USERNAME with your actual GitHub username.

Step 5: Verify
Go to your GitHub repository URL and you should see:

✅ All your code files
✅ requirements.txt
✅ agents/ and utils/ folders
❌ NO .streamlit/ folder (protected by .gitignore)
❌ NO venv/ folder (protected by .gitignore)


⚠️ CRITICAL Security Check:
Before pushing, verify secrets are NOT included:
bashgit status
Make sure .streamlit/ is NOT listed. If it is, run:
bashgit rm -r --cached .streamlit/
git commit -m "Remove secrets from tracking"

Create a README.md (Optional but Recommended):
Create README.md in VS Code:
markdown# MailMate - AI Email Response Generator

Automatically generate and send professional email responses using Google Gemini AI.

## Features
- AI-powered email response generation
- Multiple tone options (Professional, Friendly, Apologetic, Persuasive)
- Direct email sending via Gmail SMTP
- Clean Streamlit web interface

## Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `.\venv\Scripts\Activate` (Windows)
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.streamlit/secrets.toml` with your API keys
6. Run: `streamlit run main.py`

## Required Secrets
```toml
GEMINI_API_KEY = "your-key"
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-app-password"
```

## Tech Stack
- Streamlit
- Google Gemini API
- Python SMTP
Then commit and push:
bashgit add README.md
git commit -m "Add README"
git push
Your project is now on GitHub! 🎉 What's your GitHub username? I can help you verify the URL!2 / 2Retrywarning: in the working copy of 'venv/Lib/site-packages/narwhals/_spark_like/utils.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'venv/Lib/site-packages/narwhals/_sql/__init__.py', LF will be replaced by CRLF the next time Git touches it
warning: in pastedSGwarning: in the working copy of 'venv/Lib/site-packages/narwhals/_spark_like/utils.py', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'venv/Lib/site-packages/narwhals/_sql/__init__.py', LF will be replaced by CRLF the next time Git touches it
warning: in pastedSGstep by step⚠️ STOP! The Problem:
Git is trying to add your venv/ folder (virtual environment) which should NOT be on GitHub. This will make your repository huge and messy.
Let's fix this step by step:

Step 1: Stop the Current Process
Press Ctrl + C in your terminal to cancel if it's still running.

Step 2: Remove Everything Git Added
bashgit rm -rf --cached .
```

This removes all files from Git's tracking (but doesn't delete them from your computer).

---

## Step 3: Create/Update `.gitignore`

Make sure your `.gitignore` file exists and has this content:

**In VS Code, open `.gitignore` and paste:**
```
# Virtual Environment (CRITICAL - DO NOT UPLOAD)
venv/
env/
ENV/
*.pyc
__pycache__/

# Streamlit Secrets (CONTAINS API KEYS!)
.streamlit/
secrets.toml

# Python
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
._*

# Test files
test_models.py

# Logs
*.log
Save it (Ctrl + S)

Step 4: Add Files Again (Correctly This Time)
bashgit add .

Step 5: Check What Will Be Uploaded
bashgit status
You should see:
✅ main.py
✅ requirements.txt
✅ agents/email_agent.py
✅ utils/email_sender.py
✅ .gitignore
You should NOT see:
❌ venv/ folder
❌ .streamlit/ folder
❌ Any files with warnings

Step 6: Commit Your Files
bashgit commit -m "Initial commit: MailMate email responder"

Step 7: Create GitHub Repository

Go to github.com
Click "+" → "New repository"
Name: MailMate
Description: "AI email response generator with Gemini"
Keep Public or make Private
DON'T check "Initialize with README"
Click "Create repository"


Step 8: Connect to GitHub
bash# Replace YOUR-USERNAME with your GitHub username
git remote add origin https://github.com/YOUR-USERNAME/MailMate.git
git branch -M main
git push -u origin main

Step 9: Verify Upload
Go to your GitHub repository. You should see:

✅ Small repository size (a few KB, not MB)
✅ Your code files
❌ NO venv/ folder


If You Still See Warnings:
Run this to see what Git is tracking:
bashgit ls-files | grep venv
If it shows venv files, run:
bashgit rm -rf --cached venv/
git commit -m "Remove venv from tracking"

Ready? Start with Step 2 and let me know what you see after Step 5! 📋RetrySGif i manually zip in and uplode to github  what all things i need to change before uploding itFiles to Remove/Change Before Zipping and Uploading:
❌ DELETE These Folders Completely:

venv/ - Virtual environment (HUGE, not needed)
.streamlit/ - Contains your API keys and passwords
__pycache__/ - Python cache files
.git/ - Git folder (if it exists)

❌ DELETE These Files:

test_models.py - Your test file
.DS_Store - Mac system file (if exists)
Any .pyc files


✅ KEEP These Files:

main.py
requirements.txt
agents/email_agent.py
utils/email_sender.py
.gitignore


📝 CREATE This File (Important!):
README.md - So others know how to use it:
markdown# MailMate - AI Email Response Generator

Automatically generate and send professional email responses using Google Gemini AI.

## Features
- AI-powered email response generation
- Multiple tone options (Professional, Friendly, Apologetic, Persuasive)
- Direct email sending via Gmail SMTP
- Clean Streamlit web interface

## Setup Instructions

### 1. Clone or Download
Download this repository and extract it.

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
**Windows:**
```bash
.\venv\Scripts\Activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Create Secrets File
Create a folder `.streamlit` and inside it create `secrets.toml`:
```
MailMate/
└── .streamlit/
    └── secrets.toml
```

Add your credentials to `secrets.toml`:
```toml
GEMINI_API_KEY = "your-gemini-api-key"
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_PASSWORD = "your-gmail-app-password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

### 6. Get API Keys

**Gemini API Key:**
- Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
- Click "Create API Key"

**Gmail App Password:**
- Go to [Google Account Security](https://myaccount.google.com/security)
- Enable 2-Step Verification
- Go to App Passwords
- Generate password for "Mail"

### 7. Run the Application
```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

## Tech Stack
- Python 3.8+
- Streamlit
- Google Gemini API
- Python SMTP/smtplib

## Security Warning
⚠️ Never commit your `secrets.toml` file or share your API keys publicly!

## License
MIT License
```

---

## 📦 **Your Final Folder Structure Should Look Like:**
```
MailMate/
├── agents/
│   └── email_agent.py
├── utils/
│   └── email_sender.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
Total size should be < 50 KB

🚀 How to Upload to GitHub Manually:
Method 1: GitHub Web Interface

Go to github.com
Click "+" → "New repository"
Name it MailMate
Click "Create repository"
Click "uploading an existing file"
Drag and drop only the files listed above (NOT the venv folder!)
Add commit message: "Initial commit"
Click "Commit changes"

Method 2: Upload ZIP

Select ONLY the files/folders listed above
Right-click → "Send to" → "Compressed (zipped) folder"
Name it MailMate.zip
Upload to GitHub via web interface


⚠️ CRITICAL Security Checklist:
Before uploading, double-check:

 NO .streamlit/ folder
 NO secrets.toml file anywhere
 NO venv/ folder
 NO API keys in any file
 .gitignore file is included
 README.md is included


🔍 Quick Verification:
Check the size of your zip file:

✅ Good: < 100 KB
⚠️ Warning: 1-10 MB (might have some unnecessary files)
❌ Bad: > 10 MB (probably has venv folder!)


Want me to help you verify before you upload? Share a screenshot of your MailMate folder! 📸RetrySGi have lossed all the file can you give me all correct filesNo problem! I'll give you all the correct files. Let's recreate everything from scratch:

📁 Step 1: Create Project Structure
Create these folders:
MailMate/
├── .streamlit/
├── agents/
└── utils/

📄 Step 2: Create All Files
File 1: main.py
pythonimport streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

st.set_page_config(page_title="Auto Email Responder", layout="wide")
st.title("📧 MailMate – Think Less, Send Smart")

email_text = st.text_area("Paste the email content you received:", height=300)
recipient_email = st.text_input("Recipient Email Address")
tone = st.selectbox("Select response tone", ["Professional", "Friendly", "Apologetic", "Persuasive"])

if st.button("Generate & Send Email"):
    if not recipient_email:
        st.warning("Please enter the recipient's email address.")
    elif not email_text:
        st.warning("Please paste the email content.")
    else:
        with st.spinner("Generating and sending email..."):
            response = generate_email_response(email_text, tone)
            send_status = send_email(recipient_email, response)
            
            st.subheader("✉️ Generated Response")
            st.markdown(response, unsafe_allow_html=True)
            
            if send_status:
                st.success(f"Email sent successfully to {recipient_email}")
            else:
                st.error("Failed to send the email.")

File 2: agents/email_agent.py
pythonimport streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    
    # Use Gemini model
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
    return response.text

File 3: utils/email_sender.py
pythonimport smtplib
import streamlit as st
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient, body):
    try:
        sender_email = st.secrets["SENDER_EMAIL"]
        sender_password = st.secrets["EMAIL_PASSWORD"]
        smtp_server = st.secrets.get("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = st.secrets.get("SMTP_PORT", 587)
        
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient
        message['Subject'] = "Response To Your Email"
        
        message.attach(MIMEText(body, "plain"))
        
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(message)
        server.quit()
        
        return True
    except Exception as e:
        print("Error sending email:", e)
        return False
```

---

### **File 4: `requirements.txt`**
```
streamlit
google-generativeai

File 5: .streamlit/secrets.toml
toml# Gemini API Key
GEMINI_API_KEY = "AIzaSyD1Ozl5If-8QAQdSdjAwV0PLuYPn9PUvIg"

# Email credentials
SENDER_EMAIL = "shlokkumar4606@gmail.com"
SENDER_PASSWORD = "dyuw tbtt ybfj olpc"

# SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

**⚠️ IMPORTANT:** Replace with your NEW API keys (the ones I showed are now public and should be regenerated!)

---

### **File 6: `.gitignore`**
```
# Virtual Environment
venv/
env/
ENV/

# Streamlit Secrets
.streamlit/
secrets.toml

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

File 7: README.md
markdown# MailMate - AI Email Response Generator

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

**Mac/Linux:**
```bash
source venv/bin/activate
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

## License
MIT License

🚀 Quick Setup Commands
Open PowerShell in a new folder and run:
powershell# Create project structure
mkdir MailMate
cd MailMate
mkdir agents, utils, .streamlit

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate

# Install dependencies
pip install streamlit google-generativeai

# Run the app
streamlit run main.py

📋 Checklist:
After creating all files:

 7 files created
 3 folders (agents, utils, .streamlit)
 Virtual environment created
 Dependencies installed
 Secrets configured with YOUR new API keys
 App runs successfully


 ⚡ Code to Run MailMate - All Commands

METHOD 1: Using Batch Files (Easiest) 🖱️
Just double-click these files:
First Time Setup:
1. Double-click: install.bat
2. Wait for completion
3. Edit secrets.toml with your API keys
4. Double-click: run.bat


### **Every Time After:**

Double-click: run.bat