import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone, custom_prompt=""):
    """
    Generate email response with custom instructions
    
    Args:
        email_text: The original email content
        tone: The desired tone (Professional, Friendly, etc.)
        custom_prompt: Additional custom instructions
    """
    
    # Build the prompt
    base_prompt = f"""You are an AI email assistant. Write a professional email reply.

TONE: {tone}

ORIGINAL EMAIL:
{email_text}

"""
    
    # Add custom instructions if provided
    if custom_prompt and custom_prompt.strip():
        base_prompt += f"""
SPECIAL INSTRUCTIONS:
{custom_prompt}

"""
    
    base_prompt += """
REQUIREMENTS:
- Write a complete, well-formatted email reply
- Match the requested tone
- Be clear and concise
- Include appropriate greeting and closing
- Follow any special instructions provided

EMAIL REPLY:
"""
    
    # Generate response
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(base_prompt)
    return response.text