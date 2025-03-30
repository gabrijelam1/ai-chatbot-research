import openai
import streamlit as st

# Set your OpenAI API key here or via st.secrets
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

def get_chatbot_response(user_input):
    # Use OpenAI's API to generate a response
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

# Streamlit interface
st.title("AI Chatbot")

user_input = st.text_input("Enter your message:")

if user_input:
    # Generate a response
    chatbot_response = get_chatbot_response(user_input)

    # Customize response for secure interactions
    if "balance" in user_input.lower():
        chatbot_response = """
            To assist you with checking your balance, please visit our official website and log in securely. 
            You can also contact our customer support at 1-800-123-4567 for further assistance. 
            Is there anything else I can help you with today?
        """
    elif "fraud" in user_input.lower():
        chatbot_response = """
            If you suspect fraudulent activity on your account, please report it immediately by contacting our customer support at 1-800-123-4567 or via the secure portal. 
            How else may I assist you?
        """

    # Display the chatbot's response
    st.write(chatbot_response)
