import streamlit as st

st.set_page_config(layout="wide")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📁 VectorDB")
st.markdown("This is the 📁 VectorDB module.")