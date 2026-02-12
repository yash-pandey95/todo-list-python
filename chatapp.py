
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1.5-flash')

if "history" not in st.session_state:
    st.session_state.history = [
        "system : you are a helpful assistant friend."
    ]

st.title("Chat LLM")
rst_btn = st.button("Rest History")

if rst_btn:
    st.session_state.history = [
        "system : you are a helpful assistant friend."
    ]

# display chat
for item in st.session_state.history:
    role, content = item.split(" : ")
    if role == "user":
        st.markdown(f"**You:** {content}")
    elif role == "ai":
        st.markdown(f"<span style='color:lightblue'> {content} </span>", unsafe_allow_html=True)

# Text box for user input
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Input your Prompt")
    submit_button = st.form_submit_button(label="Send")


if submit_button and user_input:
    st.session_state.history.append(f"user : {user_input}")
    if st.session_state.history and st.session_state.history[-1].split(" : ")[0] == "user":
        response = model.invoke(st.session_state.history)
        st.session_state.history.append(f"ai : {response.content}")
    st.rerun()

