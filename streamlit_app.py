import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Tez Connect",
    page_icon="🚀",
    layout="wide"
)
# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.title("🚀 Tez Connect")

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Business Directory",
        "Marketplace",
        "Post Requirement",
        "AI Business Assistant",
        "Profile"
    ]
)



