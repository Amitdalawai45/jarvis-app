import os
import time
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

st.title("🤖 JARVIS AI Assistant")
st.caption("Powered by Google Gemini — Accessible Everywhere")

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
        model = genai.GenerativeModel("gemini-3.5-flash-lite")
    except Exception as e:
        st.error(f"Error configuring AI: {e}")

# Step A: Initialize message history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello sir! I am JARVIS. How can I help you today?"}
    ]

# Step B: Render existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Step C: Handle new user prompts
if prompt := st.chat_input("Ask JARVIS anything..."):
    # 1. Append user query to memory and display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if model:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                reply = ""
                for attempt in range(2):
                    try:
                        sys_prompt = (
                            "You are JARVIS, an advanced personal AI assistant. "
                            "If anyone asks who created, built, or developed you, proudly state that you were created and built by Amit Dalawai. "
                            "Detect the language (English, Hindi, Marathi) and reply in that same language. "
                            "Keep answers polite, helpful, and concise."
                        )
                        res = model.generate_content(f"{sys_prompt}\nUser Query: {prompt}")
                        reply = res.text
                        break
                    except Exception as err:
                        if "429" in str(err) and attempt == 0:
                            time.sleep(10)
                            continue
                        reply = f"Trouble reaching servers: {err}"

                st.write(reply)
                # 2. Append assistant answer to memory
                st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error("Cannot process request: Gemini model is not initialized.")
