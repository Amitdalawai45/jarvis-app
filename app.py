import os
import streamlit as st
import google.generativeai as genai

# Page setup for mobile and desktop screens
st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

st.title("🤖 JARVIS AI Assistant")
st.caption("Powered by Google Gemini — Accessible Everywhere")

# Retrieve API key securely from Streamlit Secrets or Environment
GEMINI_API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

model = None

if not GEMINI_API_KEY:
    st.warning("⚠️ API Key not detected. Please configure GEMINI_API_KEY in Streamlit Secrets.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Directly target the active gemini-3.6-flash model
        model = genai.GenerativeModel("gemini-3.6-flash")
    except Exception as e:
        st.error(f"Error configuring AI: {e}")

# Initialize message history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello sir! I am JARVIS. How can I help you today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input bar
if prompt := st.chat_input("Ask JARVIS anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate assistant response
    if model:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    sys_prompt = (
                        "You are JARVIS, a helpful personal AI assistant. "
                        "Detect the language (English, Hindi, Marathi) and reply in the same language. "
                        "Keep your response concise, polite, and helpful."
                    )
                    res = model.generate_content(f"{sys_prompt}\nUser Query: {prompt}")
                    reply = res.text
                except Exception as err:
                    reply = f"Trouble reaching servers: {err}"

                st.write(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error("Cannot process request: Gemini model is not initialized.")
