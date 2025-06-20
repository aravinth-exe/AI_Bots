import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.chat_history import InMemoryChatMessageHistory

@st.cache_resource
def load_model():
    return OllamaLLM(model="deepseek-r1")

def app():
    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [SystemMessage(content="Reply in English only.")]

    # Rebuild LangChain memory
    memory = InMemoryChatMessageHistory()
    for msg in st.session_state.chat_history:
        memory.add_message(msg)

    # Title
    st.title("🤖 Simple LLM Chatbot")

    # Chat input
    user_input = st.chat_input("Say something...", key="unique_input_key")

    # Handle input
    if user_input:
        llm = load_model()
        memory.add_user_message(user_input)
        st.session_state.chat_history.append(HumanMessage(content=user_input))

        response = llm.invoke(memory.messages)

        memory.add_ai_message(response)
        st.session_state.chat_history.append(AIMessage(content=response))

    # Show messages
    for msg in memory.messages:
        if isinstance(msg, SystemMessage):
            continue  # Don't display system prompt
        with st.chat_message("user" if isinstance(msg, HumanMessage) else "ai"):
            st.write(msg.content)
