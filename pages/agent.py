import streamlit as st

def app():
    st.set_page_config(page_title="Agent", layout="wide")
    st.title("🧠 Intelligent Agent")
    query = st.text_input("Ask the agent anything:")
    if st.button("Ask"):
        st.success(f"Agent response for: {query}")
