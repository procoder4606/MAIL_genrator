import streamlit as st
from agents.email_agent import generate_email_response
from utils.email_sender import send_email

# Page configuration
st.set_page_config(
    page_title="MailMate - AI Email Assistant",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        font-weight: bold;
        padding: 0.75rem;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .success-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .error-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .info-box {
        padding: 1rem;
        border-radius: 8px;
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        color: #0c5460;
    }
    h1 {
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #7f8c8d;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📧 MailMate")
st.markdown('<p class="subtitle">AI-Powered Email Response Generator</p>', unsafe_allow_html=True)

# Sidebar with instructions
with st.sidebar:
    st.header("📖 How to Use")
    
    st.markdown("### 1️⃣ Input Email")
    st.caption("Paste the email you received")
    
    st.markdown("### 2️⃣ Set Recipient")
    st.caption("Enter the email address to send to")
    
    st.markdown("### 3️⃣ Choose Settings")
    st.caption("Select tone and add custom instructions")
    
    st.markdown("### 4️⃣ Generate & Send")
    st.caption("AI creates and sends the response")
    
    st.divider()
    
    st.header("🎯 Response Tones")
    st.markdown("""
    **Professional**  
    Formal business communication
    
    **Friendly**  
    Warm, casual, approachable
    
    **Apologetic**  
    Expressing regret or sorry
    
    **Persuasive**  
    Convincing, sales-oriented
    """)
    
    st.divider()
    
    st.header("💡 Quick Tips")
    st.markdown("""
    - Be specific in custom instructions
    - Keep instructions clear and concise
    - Review generated email before sending
    - Use advanced options for complex needs
    """)

# Main content area
col_main1, col_main2 = st.columns([2, 1])

with col_main1:
    # Input email section
    st.subheader("📥 Original Email")
    email_text = st.text_area(
        "Paste the email content you received:",
        height=250,
        placeholder="Copy and paste the entire email here...",
        help="Include the full email text for best results"
    )
    
    # Character count
    if email_text:
        st.caption(f"📊 Characters: {len(email_text)} | Words: {len(email_text.split())}")

with col_main2:
    # Recipient section
    st.subheader("📬 Recipient Details")
    recipient_email = st.text_input(
        "Recipient Email Address:",
        placeholder="example@email.com",
        help="Enter the email address where the response will be sent"
    )
    
    # Email validation
    if recipient_email:
        if "@" in recipient_email and "." in recipient_email:
            st.success("✓ Valid email format")
        else:
            st.error("✗ Invalid email format")
    
    st.divider()
    
    # Tone selection
    st.subheader("🎭 Response Tone")
    tone = st.selectbox(
        "Select the tone for your response:",
        ["Professional", "Friendly", "Apologetic", "Persuasive"],
        help="Choose the appropriate tone based on your relationship and context"
    )
    
    # Tone description
    tone_descriptions = {
        "Professional": "Formal, business-appropriate language",
        "Friendly": "Warm, casual, and personable",
        "Apologetic": "Expresses regret and understanding",
        "Persuasive": "Convincing and action-oriented"
    }
    st.caption(f"💬 {tone_descriptions[tone]}")

# Custom instructions section
st.divider()
st.subheader("✍️ Custom Instructions")

col_inst1, col_inst2 = st.columns(2)

with col_inst1:
    custom_prompt = st.text_input(
        "Quick Instructions:",
        placeholder="e.g., Keep it under 100 words, Add meeting request...",
        help="Brief instructions for customizing the response"
    )

with col_inst2:
    # Preset instruction templates
    preset_instructions = st.selectbox(
        "Or choose a template:",
        [
            "None",
            "Request a meeting",
            "Ask for more information",
            "Provide pricing details",
            "Decline politely",
            "Express gratitude",
            "Request deadline extension",
            "Follow up on previous email"
        ]
    )
    
    if preset_instructions != "None":
        custom_prompt = preset_instructions

# Advanced options (collapsible)
with st.expander("⚙️ Advanced Options", expanded=False):
    col_adv1, col_adv2 = st.columns(2)
    
    with col_adv1:
        detailed_prompt = st.text_area(
            "Detailed Custom Instructions:",
            height=150,
            placeholder="""Add specific requirements:
- Mention specific dates or times
- Include pricing information
- Add specific contact details
- Request specific actions
- Set tone for different sections""",
            help="Provide detailed instructions for complex requirements"
        )
    
    with col_adv2:
        st.markdown("**Additional Settings:**")
        
        email_length = st.select_slider(
            "Response Length:",
            options=["Very Short", "Short", "Medium", "Long", "Very Long"],
            value="Medium",
            help="Control the length of the generated response"
        )
        
        include_greeting = st.checkbox("Include greeting", value=True)
        include_closing = st.checkbox("Include closing signature", value=True)
        add_cta = st.checkbox("Add call-to-action", value=False)
        
        if add_cta:
            cta_text = st.text_input("Call-to-action text:", placeholder="Schedule a call")

# Generate button
st.divider()

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    generate_button = st.button(
        "🚀 Generate & Send Email",
        type="primary",
        use_container_width=True
    )

# Generation and sending logic
if generate_button:
    # Validation
    if not recipient_email:
        st.error("⚠️ Please enter a recipient email address")
    elif not email_text:
        st.error("⚠️ Please paste the email content")
    elif "@" not in recipient_email or "." not in recipient_email:
        st.error("⚠️ Please enter a valid email address")
    else:
        # Build final prompt with all options
        final_prompt = ""
        
        if custom_prompt:
            final_prompt += f"{custom_prompt}\n"
        
        if detailed_prompt:
            final_prompt += f"{detailed_prompt}\n"
        
        # Add length instruction
        length_instructions = {
            "Very Short": "Keep the response under 50 words.",
            "Short": "Keep the response under 100 words.",
            "Medium": "Write a moderately sized response (100-200 words).",
            "Long": "Write a detailed response (200-300 words).",
            "Very Long": "Write a comprehensive response (300+ words)."
        }
        final_prompt += f"\n{length_instructions[email_length]}\n"
        
        if not include_greeting:
            final_prompt += "Do not include a greeting.\n"
        
        if not include_closing:
            final_prompt += "Do not include a closing signature.\n"
        
        if add_cta and 'cta_text' in locals():
            final_prompt += f"Include this call-to-action: {cta_text}\n"
        
        # Generate response
        with st.spinner("🤖 AI is crafting your email response..."):
            try:
                response = generate_email_response(email_text, tone, final_prompt)
                
                # Display generated response
                st.divider()
                st.subheader("✉️ Generated Email Response")
                
                # Response box with styling
                st.markdown(
                    f'<div class="info-box">{response.replace(chr(10), "<br>")}</div>',
                    unsafe_allow_html=True
                )
                
                # Word count
                st.caption(f"📊 Response Length: {len(response.split())} words | {len(response)} characters")
                
                # Send email
                st.divider()
                with st.spinner("📤 Sending email..."):
                    send_status = send_email(recipient_email, response)
                    
                    if send_status:
                        st.markdown(
                            f'<div class="success-box">✅ <strong>Email sent successfully!</strong><br>Sent to: {recipient_email}</div>',
                            unsafe_allow_html=True
                        )
                        st.balloons()
                    else:
                        st.markdown(
                            '<div class="error-box">❌ <strong>Failed to send email</strong><br>Please check your email settings in secrets.toml</div>',
                            unsafe_allow_html=True
                        )
                
            except Exception as e:
                st.markdown(
                    f'<div class="error-box">❌ <strong>Error generating response</strong><br>{str(e)}</div>',
                    unsafe_allow_html=True
                )

# Footer
st.divider()
col_footer1, col_footer2, col_footer3 = st.columns(3)

with col_footer1:
    st.caption("🤖 Powered by Google Gemini AI")

with col_footer2:
    st.caption("📧 Secure email delivery via SMTP")

with col_footer3:
    st.caption("🔒 Your data stays private")
