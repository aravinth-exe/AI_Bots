import streamlit as st
from streamlit_option_menu import option_menu
import importlib

# Config
st.set_page_config(page_title="AI Bots", layout="wide", initial_sidebar_state="expanded")

# Hide default sidebar
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] { display: none !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=['LLM Chatbot', 'VectorDB', 'RAG', 'Image > Text', 'Text > Image', 'Agent'],
        icons=["type", "search", "search", "image", "palette", "cpu"],
        default_index=0
    )

# Mapping menu to module
page_modules = {
    "LLM Chatbot": "pages.llm_text",
    "VectorDB": "pages.vector_db",
    "RAG": "pages.rag",
    "Image > Text": "pages.image_to_text",
    "Text > Image": "pages.text_to_image",
    "Agent": "pages.agent"
}

# Dynamically import and run the selected page
module_name = page_modules.get(selected)
if module_name:
    page = importlib.import_module(module_name)
    if hasattr(page, "app"):
        page.app()
    else:
        st.error(f"Module '{module_name}' does not have an `app()` function.")
