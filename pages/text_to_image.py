import streamlit as st

def app():
    st.set_page_config(page_title="Text to Image", layout="wide")
    st.title("🎨 Text to Image Generation")
    desc = st.text_input("Describe your image:")
    if st.button("Generate Image"):
        st.image("https://via.placeholder.com/400x200.png?text=Generated+Image", caption="Result")
