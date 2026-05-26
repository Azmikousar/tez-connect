# app.py
import streamlit as st

# =========================================
# PAGE CONFIG
# =========================================
st.set_page_config(
    page_title="TezConnect",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================
# COLORS
# =========================================
C = {
    "bg": "#07080c",
    "surface": "#0d0f18",
    "card": "#111520",
    "border": "#1c2136",
    "accent": "#c9a84c",
    "blue": "#4f8ef7",
    "green": "#22c55e",
    "purple": "#a78bfa",
    "red": "#f87171",
    "orange": "#fb923c",
    "text": "#eef0f8",
    "muted": "#5b6480",
}

# =========================================
# GLOBAL CSS
# =========================================
st.markdown(f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Inter', sans-serif;
}}

.stApp {{
    background: {C["bg"]};
    color: {C["text"]};
}}

section[data-testid="stSidebar"] {{
    display:none;
}}

.block-container {{
    padding-top: 1.5rem;
    padding-bottom: 6rem;
}}

.main-card {{
    background:{C["surface"]};
    border:1px solid {C["border"]};
    border-radius:24px;
    padding:28px;
}}

.card {{
    background:{C["card"]};
    border:1px solid {C["border"]};
    border-radius:18px;
    padding:18px;
}}

.banner {{
    background: linear-gradient(135deg,#101628 0%,#0d1420 50%,#141020 100%);
    border:1px solid rgba(201,168,76,.3);
    border-radius:22px;
    padding:28px;
}}

.metric {{
    background: rgba(255,255,255,0.03);
    border:1px solid {C["border"]};
    border-radius:14px;
    padding:16px;
    text-align:center;
}}

.metric-value {{
    font-size:24px;
    font-weight:800;
    color:{C["accent"]};
}}

.metric-label {{
    font-size:11px;
    color:{C["muted"]};
    text-transform:uppercase;
    letter-spacing:.08em;
}}

.title {{
    font-size:34px;
    font-family:'Poppins',sans-serif;
    font-weight:800;
    color:{C["text"]};
}}

.subtitle {{
    color:{C["muted"]};
    font-size:14px;
}}

.section-title {{
    font-size:20px;
    font-weight:700;
    margin-bottom:14px;
    color:{C["text"]};
}}

.feed-card {{
    background:{C["card"]};
    border:1px solid {C["border"]};
    border-radius:18px;
    padding:18px;
    margin-bottom:16px;
}}

.avatar {{
    width:52px;
    height:52px;
    border-radius:50%;
    background:linear-gradient(135deg,#c9a84c,#4f8ef7);
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:800;
    font-size:20px;
}}

.small-avatar {{
    width:42px;
    height:42px;
    border-radius:50%;
    background:linear-gradient(135deg,#22c55e,#4f8ef7);
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-weight:800;
    font-size:16px;
}}

.navbar {{
    position:fixed;
    bottom:0;
    left:0;
    right:0;
    background:{C["surface"]};
    border-top:1px solid {C["border"]};
    padding:10px 20px;
    z-index:999;
}}

.nav-inner {{
    display:flex;
    justify-content:space-around;
    align-items:center;
}}

.nav-item {{
    text-align:center;
    color:{C["muted"]};
    font-size:11px;
}}

.stButton > button {{
    width:100%;
    border-radius:12px;
    border:none;
    background:{C["accent"]};
    color:black;
    font-weight:700;
    padding:12px 0;
}}

.stTextInput input {{
    background:{C["card"]};
    border:1px solid {C["border"]};
    color:white;
    border-radius:12px;
}}

.stTextArea textarea {{
    background:{C["card"]};
    border:1px solid {C["border"]};
    color:white;
    border-radius:12px;
}}

</style>
""", unsafe_allow_html=True)

# =========================================
# SESSION STATE
# =========================================
if "page" not in st.session_state:
    st.session_state.page = "login"

# =========================================
# SAMPLE DATA
# =========================================
users = [
    {
        "name": "Priya Sharma",
        "role": "Digital Marketing Head",
        "company": "BrandBoost",
        "followers": "3.2K"
    },
    {
        "name": "Rahul Gupta",
        "role": "Angel Investor",
        "company": "GV Capital",
        "followers": "5.6K"
    },
    {
        "name": "Sneha Patil",
        "role": "Business Coach",
        "company": "GrowthMind",
        "followers": "2.1K"
    }
]

events = [
    {
        "title": "B2B Growth Summit 2026",
        "date": "Jun 15",
        "location": "Mumbai",
        "price": "₹2,999"
    },
    {
        "title": "Startup Investor Meet",
        "date": "Jun 22",
        "location": "Bangalore",
        "price": "Free"
    }
]

leads = [
    {
        "company": "TechNova Pvt Ltd",
        "need": "Marketing Agency",
        "budget": "₹80K/mo"
    },
    {
        "company": "GreenBuild Co.",
        "need": "Sales Partner",
        "budget": "₹1.2L/mo"
    }
]

# =========================================
# LOGIN PAGE
# =========================================
if st.session_state.page == "login":

    c1, c2, c3 = st.columns([1,1.2,1])

    with c2:

        st.markdown("""
        <div style="text-align:center;margin-top:30px;margin-bottom:30px;">

            <div style="
                width:80px;
                height:80px;
                border-radius:22px;
                background:linear-gradient(135deg,#c9a84c,#9c7420);
                margin:auto;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:40px;
                margin-bottom:20px;
            ">
                🚀
            </div>

            <div class="title">TezConnect</div>

            <div class="subtitle">
                B2B Professional Network · India
            </div>

        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="main-card">', unsafe_allow_html=True)

        st.markdown("""
        <div style="font-size:24px;font-weight:800;margin-bottom:5px;">
            Welcome back 👋
        </div>

        <div class="subtitle" style="margin-bottom:24px;">
            Sign in to your TezConnect account
        </div>
        """, unsafe_allow_html=True)

        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        if st.button("Sign In →"):
            st.session_state.page = "dashboard"
            st.rerun()

        st.markdown("""
        <div style="margin-top:24px;text-align:center;">
            <span style="color:#5b6480;font-size:12px;">
                10,000+ professionals joined
            </span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# DASHBOARD
# =========================================
elif st.session_state.page == "dashboard":

    st.markdown("""
    <div class="banner">

        <div style="
            font-size:12px;
            color:#5b6480;
            text-transform:uppercase;
            font-weight:700;
            letter-spacing:.08em;
        ">
            GOOD MORNING
        </div>

        <div style="
            font-size:30px;
            font-weight:800;
            margin-top:8px;
        ">
            Welcome to TezConnect
        </div>

        <div style="
            color:#c9a84c;
            margin-top:10px;
            font-weight:600;
        ">
            India's B2B Professional Network
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(
        '<div class="section-title">Platform Metrics</div>',
        unsafe_allow_html=True
    )

    m1, m2, m3, m4 = st.columns(4)

    metrics = [
        ("382", "Connections"),
        ("4.2K", "Profile Views"),
        ("38", "Leads"),
        ("127", "Saves")
    ]

    for col, metric in zip([m1,m2,m3,m4], metrics):

        with col:

            st.markdown(f"""
            <div class="metric">

                <div class="metric-value">
                    {metric[0]}
                </div>

                <div class="metric-label">
                    {metric[1]}
                </div>

            </div>
            """, unsafe_allow_html=True)

    st.write("")

    left, right = st.columns([2,1])

    # FEED
    with left:

        st.markdown(
            '<div class="section-title">Personalized Feed</div>',
            unsafe_allow_html=True
        )

        for user in users:

            initials = user["name"][0]

            st.markdown(f"""
            <div class="feed-card">

                <div style="
                    display:flex;
                    gap:14px;
                    align-items:center;
                    margin-bottom:14px;
                ">

                    <div class="avatar">
                        {initials}
                    </div>

                    <div>

                        <div style="
                            font-size:15px;
                            font-weight:700;
                        ">
                            {user["name"]}
                        </div>

                        <div style="
                            color:#5b6480;
                            font-size:12px;
                        ">
                            {user["role"]} · {user["company"]}
                        </div>

                    </div>

                </div>

                <div style="
                    color:#d7dceb;
                    line-height:1.8;
                    font-size:13px;
                ">
                    Building strong business networks and helping startups scale faster using modern B2B collaboration strategies.
                </div>

                <div style="
                    margin-top:14px;
                    color:#c9a84c;
                    font-weight:700;
                    font-size:13px;
                ">
                    👥 {user["followers"]} followers
                </div>

            </div>
            """, unsafe_allow_html=True)

    # RIGHT SIDE
    with right:

        st.markdown(
            '<div class="section-title">Business Leads</div>',
            unsafe_allow_html=True
        )

        for lead in leads:

            st.markdown(f"""
            <div class="card" style="margin-bottom:14px;">

                <div style="
                    font-size:15px;
                    font-weight:700;
                    margin-bottom:5px;
                ">
                    {lead["company"]}
                </div>

                <div style="
                    color:#5b6480;
                    font-size:12px;
                ">
                    {lead["need"]}
                </div>

                <div style="
                    color:#c9a84c;
                    font-weight:800;
                    margin-top:10px;
                ">
                    {lead["budget"]}
                </div>

            </div>
            """, unsafe_allow_html=True)

        st.markdown(
            '<div class="section-title">Upcoming Events</div>',
            unsafe_allow_html=True
        )

        for ev in events:

            st.markdown(f"""
            <div class="card" style="margin-bottom:14px;">

                <div style="
                    color:#c9a84c;
                    font-size:12px;
                    font-weight:700;
                    margin-bottom:8px;
                ">
                    {ev["date"]}
                </div>

                <div style="
                    font-size:15px;
                    font-weight:700;
                    margin-bottom:4px;
                ">
                    {ev["title"]}
                </div>

                <div style="
                    color:#5b6480;
                    font-size:12px;
                ">
                    📍 {ev["location"]}
                </div>

                <div style="
                    color:#22c55e;
                    margin-top:10px;
                    font-weight:700;
                ">
                    {ev["price"]}
                </div>

            </div>
            """, unsafe_allow_html=True)

    # BOTTOM NAVBAR
    st.markdown("""
    <div class="navbar">

        <div class="nav-inner">

            <div class="nav-item">
                🏠<br>Home
            </div>

            <div class="nav-item">
                👥<br>Network
            </div>

            <div class="nav-item">
                💼<br>Leads
            </div>

            <div class="nav-item">
                🎫<br>Events
            </div>

            <div class="nav-item">
                👤<br>Profile
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)
