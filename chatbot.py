import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🩺 Medical Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Hi, I'm your Doctor, how can I help you?")

if st.button("Ask"):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional doctor chatbot. Provide simple, clear medical advice suitable for Pakistani users. Remind them to consult an actual doctor for verification."},
                {"role": "user", "content": user_input}
            ]
        )

        answer = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": answer})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Doctor Bot:** {msg['content']}")
