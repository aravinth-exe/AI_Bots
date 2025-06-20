import streamlit as st

def app():
    st.set_page_config(page_title="Image to Text", layout="wide")
    st.title("🖼️ Image Captioning")
    img = st.file_uploader("Upload an image", type=['png', 'jpg'])
    if img:
        st.image(img, width=300)
        st.write("Caption: *A placeholder caption here.*")
