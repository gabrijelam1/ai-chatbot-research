import streamlit as st
from openai import OpenAI
import os

# Load OpenAI API key from Streamlit secrets or .env
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


client = OpenAI(api_key=api_key)

st.set_page_config(page_title="Banking Chatbot", page_icon="💬")
st.title("💬 AI Chatbot Research Prototype")

st.markdown("Ask about banking topics like *lost card*, *balance*, or *fraud*. This assistant is designed with responsible AI principles aligned with GDPR & the AI Act.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# User input
if user_input := st.chat_input("Type your message here..."):
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Build prompt
    messages = [
        {
            "role": "system",
            "content": (
                "You are a responsible banking assistant. "
                "Answer clearly and concisely. "
                "If the user reports a lost card or other concern, provide help "
                "and then ask: 'Is there anything else I can help you with?' "
                "Suggest 2–3 follow-up options like 'Check my balance', 'Report fraud', or 'No, thank you.'"
            ),
        }
    ] + st.session_state.messages

    # Get response from GPT
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.4
    )

    reply = response.choices[0].message.content.strip()
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})

