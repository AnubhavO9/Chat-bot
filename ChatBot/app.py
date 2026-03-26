import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Ask something")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": reply})

for msg in st.session_state.messages:
    st.write(f"**{msg['role']}**: {msg['content']}")