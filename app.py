import streamlit as st
from groq import Groq
#from dotenv import load_dotenv
import os

#load_dotenv()


api_key = st.secrets.get("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(
    page_title="KB AI Assistant",
    page_icon="🤖"
)

st.title("🤖 KB AI Assistant")

st.write(
    "AI, Cybersecurity, Electronics and Programming Assistant"
)

question = st.text_area(
    "Ask a question:",
    height=120
)

if st.button("Ask AI"):

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
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            model="llama-3.3-70b-versatile"
        )

        answer = response.choices[0].message.content

        st.success("Response")

        st.write(answer)