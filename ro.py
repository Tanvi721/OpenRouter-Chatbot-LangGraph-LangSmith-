import streamlit as st
from graph import workflow
from langsmith_setup import setup_langsmith

# Initialize LangSmith
setup_langsmith()

st.set_page_config(
    page_title="OpenRouter Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("💬 OpenRouter Chatbot (LangGraph + LangSmith)")

# Create chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Chat display
for chat in st.session_state["history"]:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Show user's message
    st.session_state["history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Process using LangGraph workflow
    result = workflow.invoke({"message": user_input})
    reply = result["reply"]

    # Show bot message
    st.session_state["history"].append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)
