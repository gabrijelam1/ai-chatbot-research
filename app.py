import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import build_prompt

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
client = OpenAI(api_key=api_key)

# Streamlit UI
st.title("💬 Banking Chatbot Prototype")

user_input = st.text_input("Ask me anything about banking services:")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful, ethical banking assistant."},
                {"role": "user", "content": build_prompt(user_input)}
            ],
            max_tokens=300,
            temperature=0.3
        )

        st.write(response.choices[0].message.content)
