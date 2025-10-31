import streamlit as st
import requests
from settings import settings

st.title("AI chatbot with Groq API")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Enter your prompt :")

if st.button("Clear Chat"):
    st.session_state.chat_history = []
    URL = f"{settings.API_URL}/clear-convo"
    requests.delete(URL)

if st.button("Send") and user_input:
    st.session_state.chat_history.append(("You", user_input))
    URL = f"{settings.API_URL}/chat"
    reponse = requests.post(URL, json={"message": user_input})

    bot_reply = reponse.json().get("Answer", "Error: No response from API")

    st.session_state.chat_history.append(("Bot", bot_reply))

    print(bot_reply)

    for sender, msg in st.session_state.chat_history:
        if sender == "You":
            st.markdown(
                f"<p><b style='color:#1E90FF;'>You:</b> {msg}</p>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<p><b style='color:#32CD32;'>Bot:</b> {msg}</p>",
                unsafe_allow_html=True,
            )
