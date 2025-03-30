import openai
import streamlit as st

# Set your OpenAI API key securely
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

def get_chatbot_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.7,
            max_tokens=150
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error: {e}")
        return "Sorry, something went wrong."

st.set_page_config(page_title="AI Chatbot", layout="centered")
st.title("💬 AI Chatbot")

user_input = st.text_input("Enter your message:")

if user_input:
    st.write("🧠 User asked:", user_input)
    chatbot_response = get_chatbot_response(user_input)

    if "balance" in user_input.lower():
        chatbot_response = """
        🔐 For your security, please check your balance by logging into our official banking app or website.  
        📞 Or call support at **0800-123-4567**.
        """
    elif "fraud" in user_input.lower():
        chatbot_response = """
        ⚠️ To report fraud, contact our 24/7 hotline at **0800-123-4567**.  
        🔒 We don’t collect sensitive info here.
        """

    st.markdown(chatbot_response)
