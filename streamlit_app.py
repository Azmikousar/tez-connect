import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Tez Connect",
    page_icon="🚀",
    layout="wide"
)
# -----------------------------
# Sample Data
# -----------------------------

businesses = [
    {
        "Company": "ABC Textiles",
        "Industry": "Manufacturing",
        "Location": "Bangalore",
        "Services": "Cotton Fabrics, Textile Export",
        "Verified": "Yes"
    },
    {
        "Company": "FreshMart Pvt Ltd",
        "Industry": "Food Supply",
        "Location": "Mysore",
        "Services": "Organic Food Distribution",
        "Verified": "Yes"
    },
    {
        "Company": "Growthify Agency",
        "Industry": "Marketing",
        "Location": "Mumbai",
        "Services": "Digital Marketing, Branding",
        "Verified": "No"
    },
]

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
if menu == "Home":
    st.title("🚀 Tez Connect")
    st.subheader("B2B Networking Marketplace")

    st.markdown(
        """
        Welcome to **Tez Connect**, a platform where businesses can:

        - Connect with suppliers
        - Find distributors
        - Discover business opportunities
        - Post marketplace requirements
        - Network with startups and enterprises
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Businesses", "10,000+")

    with col2:
        st.metric("Verified Companies", "5,000+")

    with col3:
        st.metric("Marketplace Leads", "50,000+")

    st.divider()

    st.subheader("🌟 Featured Businesses")

    df = pd.DataFrame(businesses)
    st.dataframe(df, use_container_width=True)



