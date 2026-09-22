import os
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
