import streamlit as st
import openai
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("🩺 Medical Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.text_input("Enter your medical question:")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful professional doctor chatbot for Pakistani users. Answer clearly in simple English suitable for Pakistani audiences."},
            {"role": "user", "content": user_input},
        ]
    )
    answer = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": answer})

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**Bot:** {msg['content']}")

> Replace `"your-api-key"` with your actual OpenAI API key.

---

### **Step 2: Add `requirements.txt` file**

Create a file named `requirements.txt` with the following content:

```plaintext
streamlit
openai
