import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

st.set_page_config(
    page_title="KB AI Assistant",
    page_icon="🤖",
    layout="wide"
)

load_dotenv()

api_key = None

try:
    api_key = st.secrets["GROQ_API_KEY"]
except Exception:
    api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found.")
    st.stop()

client = Groq(api_key=api_key)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    padding-top: 0rem;
}

.hero {
    background: linear-gradient(135deg,#0f172a,#1e293b);
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2rem;
    color: #cbd5e1;
}

.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
}

.stTextArea textarea {
    border-radius: 15px !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.title("🤖 KB AI")

    st.markdown("---")

    st.markdown("""
### Expertise

- AI & Agents
- Cybersecurity
- Electronics
- Programming
- Research
""")

    st.markdown("---")

    st.info("Powered by Groq + Llama 3")

# ---------- HERO ----------
st.markdown("""
<div class="hero">
<h1>🤖 KB AI Assistant</h1>
<p>AI • Cybersecurity • Electronics • Programming</p>
</div>
""", unsafe_allow_html=True)

# ---------- STATS ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AI Models", "Llama 3")

with col2:
    st.metric("Speed", "Fast")

with col3:
    st.metric("Focus", "Learning")

st.markdown("---")

# ---------- QUICK PROMPTS ----------
st.subheader("🚀 Quick Prompts")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("Explain AI Agents"):
        st.session_state.prompt = "Explain AI agents"

with c2:
    if st.button("Cybersecurity Basics"):
        st.session_state.prompt = "Teach me cybersecurity basics"

with c3:
    if st.button("ESP32 Project"):
        st.session_state.prompt = "Give me an ESP32 project idea"

# ---------- CHAT ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

prompt = st.chat_input("Ask KB AI anything...")

if "prompt" in st.session_state:
    prompt = st.session_state.prompt
    del st.session_state.prompt

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.spinner("Thinking..."):

        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are KB AI Assistant.

                    Help users learn:
                    - AI
                    - Cybersecurity
                    - Electronics
                    - Programming

                    Explain clearly and simply.
                    """
                }
            ] + st.session_state.messages,
            model="llama-3.3-70b-versatile"
        )

        answer = response.choices[0].message.content

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])