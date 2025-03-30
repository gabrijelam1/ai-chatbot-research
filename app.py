import openai
import streamlit as st

# Set your OpenAI API key here or via st.secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

def get_chatbot_response(user_input):
    # Use OpenAI's new API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role