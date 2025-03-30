import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
api_key = st.secrets["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)

# Session state to store chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful and responsible banking assistant. Do not request personal or sensitive information."}
    ]

# Page config
st.set_page_config(page_title="Banking Chatbot", layout="centered")
st.title("🏦 Banking AI Chatbot")
st.caption("Ask about account balance, lost cards, or fraud (demo only)")

# Chat display
for msg in st.session_state.messages[1:]:  # skip system message
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input from user
if prompt := st.chat_input("How can I assist you today?"):
    # Display user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenAI
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages,
            temperature=0.7,
            max_tokens=150
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = "❌ Sorry, something went wrong."
        st.error(f"Error: {e}")

    # Handle custom secure responses
    if "balance" in prompt.lower():
        reply = """
        🔐 For your security, please check your balance in our official banking app or website.  
        📞 Or call customer support at **0800-123-4567**.
        """
    elif "fraud" in prompt.lower():
        reply = """
        ⚠️ To report suspicious activity, please call our 24/7 fraud hotline at **0800-123-4567**.  
        This chatbot does not handle personal or sensitive data.
        """

    # Display assistant response
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
