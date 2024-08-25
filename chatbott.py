import streamlit as st
import openai

# Initialize the OpenAI API with your Gemini key
openai.api_key = "AIzaSyClNJXGxMPPwBwqPhK8Rmk9sFRFPtfW_pY"

st.title("Gemini Chatbot")
st.write("This is a ChatGPT-like chatbot powered by the Gemini model.")

# Initialize session state to store the chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []

def generate_response(prompt):
    # Call the OpenAI API to get the response
    response = openai.ChatCompletion.create(
        model="gemini",  # Assuming "gemini" is the model name
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# User input section
user_input = st.text_input("You:", key="input")

if st.button("Send"):
    if user_input:
        # Append user input to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        # Get the bot's response
        bot_response = generate_response(user_input)
        
        # Append bot's response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        
        # Clear the input box
        st.session_state.input = ""

# Display the chat history
for message in st.session_state.messages:
    role = "You" if message["role"] == "user" else "Gemini"
    st.write(f"**{role}:** {message['content']}")

