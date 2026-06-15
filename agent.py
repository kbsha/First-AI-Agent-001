from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
api_key = st.secrets.get("GROQ_API_KEY")

client = Groq(api_key=api_key)

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    print("\nAI:")
    print(response.choices[0].message.content)