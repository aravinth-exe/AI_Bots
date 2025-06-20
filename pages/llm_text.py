import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_community.llms import Ollama

# Init chat memory + LangChain only once
@st.cache_resource
def get_chat_chain():
    llm = Ollama(model="deepseek-r1")  # or "deepseek-r1", "llama3", etc.
    memory = ConversationBufferMemory()
    return ConversationChain(llm=llm, memory=memory)

# Streamlit page function
def app():
    st.title("🤖 LLM Chatbot (LangChain + Ollama)")

    # Store chat history in session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input prompt
    user_input = st.chat_input("Say something...")

    # Initialize chain
    chain = get_chat_chain()

    # Handle user input
    if user_input:
        # Get response
        response = chain.run(user_input)

        # Save to history
        st.session_state.chat_history.append(("user", user_input))
        st.session_state.chat_history.append(("ai", response))

    # Display chat messages
    for sender, msg in st.session_state.chat_history:
        if sender == "user":
            with st.chat_message("user"):
                st.write(msg)
        else:
            with st.chat_message("ai"):
                st.write(msg)
