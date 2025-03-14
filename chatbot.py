import streamlit as st
import openai

openai.api_key = "your-actual-api-key"

st.title("🩺 Medical Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Hi, I am Your Doctor, How May I Help You?")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a professional doctor chatbot for Pakistani users. Answer in simple English suitable for Pakistani patients."},
            {"role": "user", "content": user_input},
        ]
    )
    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Doctor Bot:** {msg['content']}")
