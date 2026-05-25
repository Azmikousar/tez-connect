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
# Professional Contact Information Section

st.markdown("""
<style>
.contact-box {
    background-color: #f8f9fa;
    padding: 30px;
    border-radius: 15px;
    border: 1px solid #e6e6e6;
    margin-top: 30px;
    margin-bottom: 30px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

.contact-title {
    font-size: 28px;
    font-weight: bold;
    color: #0f172a;
    margin-bottom: 20px;
}

.contact-item {
    font-size: 16px;
    color: #374151;
    margin-bottom: 12px;
    line-height: 1.7;
}

.contact-label {
    font-weight: bold;
    color: #111827;
}
</style>

<div class="contact-box">

<div class="contact-title">
📞 CONTACT INFO
</div>

<div class="contact-item">
<span class="contact-label">📧 Email:</span>
support@tezconnect.in
</div>

<div class="contact-item">
<span class="contact-label">📞 Phone:</span>
+91 73961 80986
</div>

<div class="contact-item">
<span class="contact-label">📞 Support:</span>
+91 97031 80986
</div>

<div class="contact-item">
<span class="contact-label">📍 Address:</span><br>
Plot No. 45, 3rd Floor, Cyber Heights,<br>
Hitech City Main Road,<br>
Madhapur, Hyderabad – 500081,<br>
Telangana, India
</div>

</div>
""", unsafe_allow_html=True)
# Professional Solutions Section

st.markdown("""
<style>

.solutions-container {
    margin-top: 40px;
    margin-bottom: 30px;
}

.solutions-title {
    font-size: 32px;
    font-weight: bold;
    color: #0f172a;
    margin-bottom: 25px;
    text-align: center;
}

.solution-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    margin-bottom: 18px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.05);
    transition: 0.3s;
}

.solution-card:hover {
    box-shadow: 0px 4px 14px rgba(0,0,0,0.08);
    transform: translateY(-2px);
}

.solution-text {
    font-size: 18px;
    color: #374151;
    font-weight: 500;
}

</style>

<div class="solutions-container">

<div class="solutions-title">
🚀 SOLUTIONS
</div>

<div class="solution-card">
<div class="solution-text">
📈 Social Media Marketing & Lead Generation
</div>
</div>

<div class="solution-card">
<div class="solution-text">
🔍 Google Business Ads & SEO Services
</div>
</div>

<div class="solution-card">
<div class="solution-text">
💬 WhatsApp Marketing & Automations
</div>
</div>

<div class="solution-card">
<div class="solution-text">
🌐 Custom Websites & Mobile Apps Development
</div>
</div>

<div class="solution-card">
<div class="solution-text">
🏢 Custom ERP Software Implementations
</div>
</div>

<div class="solution-card">
<div class="solution-text">
🌐 IoT Systems & Technology Integration
</div>
</div>

<div class="solution-card">
<div class="solution-text">
🎨 Content Creation & Branding Services
</div>
</div>

</div>
""", unsafe_allow_html=True)





