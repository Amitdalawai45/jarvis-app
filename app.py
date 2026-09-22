import os
import time
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", page_icon="🐍", layout="centered")

st.title("🐍 JARVIS AI ")
st.caption("Created by AMIT DALAWAI — Accessible Everywhere")

GEMINI_API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

st.title("🤖 JARVIS AI Assistant")import os
import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="JARVIS AI", page_icon="🤖", layout="centered")

st.title("🤖 JARVIS AI Assistant")
st.caption("Created by AMIT DALAWAI — Accessible Everywhere")

GEMINI_API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

model = None

sys_instruction = (
    "You are JARVIS, an advanced personal AI assistant. "
    "If anyone asks who created, built, or developed you, proudly state that you were created and built by Amit Dalawai. "
    "Detect the language (English, Hindi, Marathi) and reply in that same language. "
    "Keep answers polite, helpful, and concise."
)

if not GEMINI_API_KEY:
    st.warning("⚠️ API Key not detected. Please configure GEMINI_API_KEY in Streamlit Secrets.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=sys_instruction
        )
    except Exception as e:
        st.error(f"Error configuring AI: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello sir! I am JARVIS. How can I help you today?"}
    ]

# Render existing conversation history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ONLY ONE st.chat_input allowed in the entire app script
if prompt := st.chat_input("Ask JARVIS anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if model:
        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    gemini_history = []
                    for msg in st.session_state.messages[:-1]:
                        role = "user" if msg["role"] == "user" else "model"
                        gemini_history.append({"role": role, "parts": [msg["content"]]})
                    
                    chat_session = model.start_chat(history=gemini_history)
                    response_stream = chat_session.send_message(prompt, stream=True)
                
                reply = st.write_stream(response_stream)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
            except Exception as err:
                error_msg = str(err)
                if "429" in error_msg:
                    reply = "⚠️ Rate limit reached (Quota exceeded). Please wait 15–20 seconds before sending another message."
                else:
                    reply = f"Trouble reaching servers: {err}"
                st.error(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error("Cannot process request: Gemini model is not initialized.")
st.caption("Created by AMIT DALAWAI — Accessible Everywhere")

GEMINI_API_KEY = None
if "GEMINI_API_KEY" in st.secrets:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

model = None

sys_instruction = (
    "You are JARVIS, an advanced personal AI assistant. "
    "If anyone asks who created, built, or developed you, proudly state that you were created and built by Amit Dalawai. "
    "Detect the language (English, Hindi, Marathi) and reply in that same language. "
    "Keep answers polite, helpful, and concise."
)

if not GEMINI_API_KEY:
    st.warning("⚠️ API Key not detected. Please configure GEMINI_API_KEY in Streamlit Secrets.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Using gemini-2.5-flash for fast, reliable, low-latency responses
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=sys_instruction
        )
    except Exception as e:
        st.error(f"Error configuring AI: {e}")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello sir! I am JARVIS. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask JARVIS anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    if model:
        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    gemini_history = []
                    for msg in st.session_state.messages[:-1]:
                        role = "user" if msg["role"] == "user" else "model"
                        gemini_history.append({"role": role, "parts": [msg["content"]]})
                    
                    chat_session = model.start_chat(history=gemini_history)
                    response_stream = chat_session.send_message(prompt, stream=True)
                
                # Stream the response tokens smoothly
                reply = st.write_stream(response_stream)
                st.session_state.messages.append({"role": "assistant", "content": reply})
                
            except Exception as err:
                error_msg = str(err)
                if "429" in error_msg:
                    reply = "⚠️ Rate limit reached (Quota exceeded). Please wait 15–20 seconds before sending another message."
                else:
                    reply = f"Trouble reaching servers: {err}"
                st.error(reply)
                st.session_state.messages.append({"role": "assistant", "content": reply})
    else:
        st.error("Cannot process request: Gemini model is not initialized.")
model = None

# Define System Instruction
sys_instruction = (
    "You are JARVIS, an advanced personal AI assistant. "
    "If anyone asks who created, built, or developed you, proudly state that you were created and built by Amit Dalawai. "
    "Detect the language (English, Hindi, Marathi) and reply in that same language. "
    "Keep answers polite, helpful, and concise."
)

if not GEMINI_API_KEY:
    st.warning("⚠️ API Key not detected. Please configure GEMINI_API_KEY in Streamlit Secrets.")
else:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        # Initialize model with system instructions
        model = genai.GenerativeModel(
            model_name="gemini-3.5-flash-lite",
            system_instruction=sys_instruction
        )
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
            with st.spinner("processing..."):
                reply = ""
                for attempt in range(2):
                    try:
                        # Convert Streamlit message history to Gemini chat history format
                        gemini_history = []
                        for msg in st.session_state.messages[:-1]: # Exclude the latest prompt as it will be sent via send_message
                            role = "user" if msg["role"] == "user" else "model"
                            gemini_history.append({"role": role, "parts": [msg["content"]]})
                        
                        # Start chat session with history
                        chat_session = model.start_chat(history=gemini_history)
                        res = chat_session.send_message(prompt)
                        
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
