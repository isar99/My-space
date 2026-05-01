from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.2-1B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

st.header("AI Teacher")

user_input = st.text_input("Enter your lecture notes:")

if st.button("Generate Summary"):
    # Create summarization prompt
    prompt = f"Summarize the following lecture notes in 10 lines:\n{user_input}\n"
    result = model.invoke(prompt)
    st.markdown(f"<div style='color:green; white-space: pre-wrap;'>{result.content}</div>",
                unsafe_allow_html=True)

if st.button("Generate Short Notes"):
    prompt = f"Generate short notes for the following lecture notes in 5 lines:\n{user_input}\n"
    result = model.invoke(prompt)
    st.markdown(f"<div style='color:orange; white-space: pre-wrap;'>{result.content}</div>",
                unsafe_allow_html=True)

if st.button("Generate Quiz Questions"):
    prompt = f"Generate 5 quiz questions for the following lecture notes:\n{user_input}\n"
    result = model.invoke(prompt)
    st.markdown(f"<div style='color:blue; white-space: pre-wrap;'>{result.content}</div>",
                unsafe_allow_html=True)

if st.button("Generate Flashcards"):
    prompt = f"Generate 5 flashcards for the following lecture notes:\n{user_input}\n"
    result = model.invoke(prompt)
    st.markdown(f"<div style='color:purple; white-space: pre-wrap;'>{result.content}</div>",
                unsafe_allow_html=True)
