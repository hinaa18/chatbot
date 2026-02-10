import streamlit as st
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyCWXFke97hWCwG_JM7lFPgvysg1uqYkqFw")

# 🤖 Load model
model = genai.GenerativeModel("gemini-2.5-flash")

# 🌐 Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gemini response
    response = model.generate_content(prompt)

    reply = response.text

    # Show bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
        
        
