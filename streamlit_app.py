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
        # Professional Footer
st.markdown("---")

footer = """
<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #ffffff;
color: gray;
text-align: center;
padding: 10px;
font-size: 14px;
border-top: 1px solid #e6e6e6;
}

.footer a {
color: #1f77b4;
text-decoration: none;
margin: 0 10px;
}

.footer a:hover {
text-decoration: underline;
}
</style>

<div class="footer">
© 2026 <b>TEZ CONNECT</b>. ALL RIGHTS RESERVED.
|
<a href="#">Privacy Policy</a>
|
<a href="#">Terms of Service</a>
</div>
"""

st.markdown(footer, unsafe_allow_html=True)
# Contact Information Section

st.markdown("## 📞 CONTACT INFO")

st.markdown("""
📧 **support@tezconnect.in**

📞 **+91 73961 80986**

📞 **+91 97031 80986**

📍 **Plot No. 45, 3rd Floor, Cyber Heights,  
Hitech City Main Road,  
Madhapur, Hyderabad – 500081,  
Telangana, India**
""")
