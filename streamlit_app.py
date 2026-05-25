import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Tez Connect",
    layout="wide"
)

# Title
st.title("🚀 Tez Connect")
st.subheader("B2B Networking Marketplace")

# Sidebar
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go To",
    [
        "Home",
        "Business Directory",
        "Marketplace",
        "Post Requirement",
        "AI Assistant"
    ]
)

# Home Page
if menu == "Home":
    st.header("Welcome to Tez Connect")

    st.write("""
    Connect with:
    - Manufacturers
    - Suppliers
    - Distributors
    - Startups
    - Service Providers
    """)

    st.success("India's Smart B2B Networking Platform")

# Business Directory
elif menu == "Business Directory":

    st.header("Business Directory")

    businesses = pd.DataFrame({
        "Company": [
            "ABC Textiles",
            "Fast Packaging",
            "Digital Boost Agency"
        ],
        "Industry": [
            "Textiles",
            "Packaging",
            "Marketing"
        ],
        "Location": [
            "Bangalore",
            "Mumbai",
            "Delhi"
        ]
    })

    st.dataframe(businesses)

# Marketplace
elif menu == "Marketplace":

    st.header("Marketplace")

    st.info("Latest Business Requirements")

    st.card = st.container()

    with st.card:
        st.write("📦 Need 5000 Packaging Boxes")
        st.button("Send Quote")

# Post Requirement
elif menu == "Post Requirement":

    st.header("Post Your Requirement")

    requirement = st.text_area(
        "Describe Your Requirement"
    )

    if st.button("Submit"):
        st.success("Requirement Posted Successfully")

# AI Assistant
elif menu == "AI Assistant":

    st.header("AI Business Assistant")

    question = st.text_input(
        "Ask Business Question"
    )

    if question:
        st.write(
            f"AI Suggestion: Connect with suppliers related to '{question}'"
        )
