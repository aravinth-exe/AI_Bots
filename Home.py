import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="AI Bots", layout="wide")

# Load custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "LLM Text", "VectorDB", "RAG", "Image > Text", "Text > Image", "Agent"],
        icons=["house", "type", "search", "search", "image", "palette", "cpu"],
        default_index=0,
    )

# Main View
if selected == "Home":
    st.title("🔮 AI Bots")
    st.markdown("Use the left sidebar to switch between modules.")
elif selected == "LLM Text":
    st.switch_page("pages/1_LLM_Text.py")
elif selected == "VectorDB":
    st.switch_page("pages/2_VectorDB.py")
elif selected == "RAG":
    st.switch_page("pages/3_RAG.py")
elif selected == "Image > Text":
    st.switch_page("pages/4_Image_to_Text.py")
elif selected == "Text > Image":
    st.switch_page("pages/5_Text_to_Image.py")
elif selected == "Agent":
    st.switch_page("pages/6_Agent.py")