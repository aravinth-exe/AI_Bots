import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

# Load model once
@st.cache_resource
def load_model():
    return OllamaLLM(model="deepseek-r1")

# App entry
def app():
    st.title("🤖 Simple LLM Chatbot")

    # Step 1: Initialize session chat history once
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            SystemMessage(content="You are a helpful assistant. Always respond only in English.")
        ]

    # Step 2: Build memory from saved messages
    memory = InMemoryChatMessageHistory()
    for msg in st.session_state.chat_history:
        memory.add_message(msg)

    # Step 3: Get user input
    user_input = st.chat_input("Say something...", key="unique_input_key")

    # Step 4: Handle response
    if user_input:
        llm = load_model()
        memory.add_user_message(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        response = llm.invoke(memory.messages)
        memory.add_ai_message(response)
        st.session_state.chat_history.append(AIMessage(content=response))

    # Step 5: Render chat (skip system messages)
    for msg in memory.messages:
        if isinstance(msg, SystemMessage):
            continue
        role = "user" if isinstance(msg, HumanMessage) else "ai"
        with st.chat_message(role):
            st.write(msg.content)

# Run app
if __name__ == "__main__":
    app()
