import streamlit as st

def app():
    st.set_page_config(page_title="Vector DB", layout="wide")
    st.title("📚 VectorDB")
    doc = st.file_uploader("Upload a document", type=['pdf', 'txt', 'docx'])
    query = st.text_input("Ask a question")
    if st.button("Query"):
        st.info("Searching documents...")
