import streamlit as st
from openai import OpenAI
import os

# Load API key securely
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

def get_chatbot_response(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, something went wrong."

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("💬 AI Chatbot")

user_input = st.text_input("Enter your message:")

if user_input:
    st.write("🧠 User asked:", user_input)
    chatbot_response = get_chatbot_response(user_input)

    # Optional: override for sensitive topics
    if "balance" in user_input.lower():
        chatbot_response = """
        🔐 Please check your balance by logging into your account securely or call 0800-123-4567.
        """
    elif "fraud" in user_input.lower():
        chatbot_response = """
        ⚠️ Report fraud immediately via our hotline at 0800-123-4567. No sensitive data should be shared here.
        """

    st.markdown(chatbot_response)
