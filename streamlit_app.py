# app.py
import streamlit as st

st.set_page_config(
    page_title="TezConnect",
    page_icon="🚀",
    layout="wide",
)

# =========================
# COLORS
# =========================
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

# =========================
# GLOBAL CSS
# =========================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@700;800&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background: {C["bg"]};
        color: {C["text"]};
    }}

    .stApp {{
        background: {C["bg"]};
    }}

    .main-card {{
        background: {C["surface"]};
        border: 1px solid {C["border"]};
        border-radius: 24px;
        padding: 28px;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    .top-banner {{
        background: linear-gradient(135deg,#101628 0%,#0d1420 50%,#141020 100%);
        border: 1px solid rgba(201,168,76,0.3);
        border-radius: 22px;
        padding: 28px;
        margin-bottom: 22px;
    }}

    .card {{
        background: {C["card"]};
        border: 1px solid {C["border"]};
        border-radius: 18px;
        padding: 18px;
    }}

    .title {{
        font-size: 34px;
        font-weight: 800;
        font-family: 'Poppins', sans-serif;
        color: {C["text"]};
        margin-bottom: 5px;
    }}

    .subtitle {{
        color: {C["muted"]};
        font-size: 14px;
    }}

    .section-title {{
        font-size: 18px;
        font-weight: 700;
        margin-bottom: 14px;
        color: {C["text"]};
    }}

    .metric-card {{
        background: rgba(255,255,255,0.03);
        border: 1px solid {C["border"]};
        border-radius: 14px;
        padding: 16px;
        text-align: center;
    }}

    .metric-value {{
        font-size: 24px;
        font-weight: 800;
    }}

    .metric-label {{
        font-size: 11px;
        color: {C["muted"]};
        text-transform: uppercase;
        letter-spacing: .08em;
    }}

    .feed-card {{
        background: {C["card"]};
        border: 1px solid {C["border"]};
        border-radius: 18px;
        padding: 18px;
        margin-bottom: 16px;
    }}

    .user-name {{
        font-size: 15px;
        font-weight: 700;
    }}

    .muted {{
        color: {C["muted"]};
        font-size: 12px;
    }}

    .gold-btn button {{
        background: {C["accent"]} !important;
        color: black !important;
        border-radius: 12px !important;
        border: none !important;
        font-weight: 700 !important;
    }}

    .stTextInput input {{
        background: {C["card"]};
        border: 1px solid {C["border"]};
        color: white;
        border-radius: 12px;
    }}

    .stTextInput label {{
        color: {C["muted"]};
        font-weight: 700;
    }}

    .stSelectbox div[data-baseweb="select"] {{
        background: {C["card"]};
        border-radius: 12px;
    }}

    .css-1d391kg {{
        background: {C["surface"]};
    }}

    .sidebar-title {{
        font-size: 22px;
        font-weight: 800;
        color: white;
        margin-bottom: 25px;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# SAMPLE DATA
# =========================
sample_users = [
    {
        "name": "Priya Sharma",
        "role": "Digital Marketing Head",
        "company": "BrandBoost",
        "followers": "3.2K",
    },
    {
        "name": "Rahul Gupta",
        "role": "Angel Investor",
        "company": "GV Capital",
        "followers": "5.6K",
    },
    {
        "name": "Sneha Patil",
        "role": "Business Coach",
        "company": "GrowthMind",
        "followers": "2.1K",
    },
]

events = [
    {
        "title": "B2B Growth Summit 2026",
        "date": "Jun 15",
        "location": "Mumbai",
        "price": "₹2,999",
    },
    {
        "title": "Startup Investor Meet",
        "date": "Jun 22",
        "location": "Bangalore",
        "price": "Free",
    },
]

leads = [
    {
        "company": "TechNova Pvt Ltd",
        "need": "Marketing Agency",
        "budget": "₹80K/mo",
    },
    {
        "company": "GreenBuild Co.",
        "need": "Sales Partner",
        "budget": "₹1.2L/mo",
    },
]

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🚀 TezConnect</div>',
        unsafe_allow_html=True,
    )

    menu = st.radio(
        "",
        ["Dashboard", "Network", "Leads", "Events", "Profile"],
    )

# =========================
# LOGIN STATE
# =========================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# =========================
# LOGIN SCREEN
# =========================
if not st.session_state.logged_in:

    col1, col2, col3 = st.columns([1, 1.2, 1])

    with col2:
        st.markdown(
            """
            <div style="text-align:center; margin-top:30px;">
                <div style="
                    width:70px;
                    height:70px;
                    margin:auto;
                    border-radius:18px;
                    background:linear-gradient(135deg,#c9a84c,#a07830);
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:34px;
                    margin-bottom:20px;
                ">
                    🚀
                </div>

                <div class="title">TezConnect</div>
                <div class="subtitle">
                    B2B Professional Network · India
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown('<div class="main-card">', unsafe_allow_html=True)

        st.markdown(
            """
            <div style="margin-bottom:20px;">
                <div style="font-size:24px;font-weight:800;">
                    Welcome back 👋
                </div>
                <div class="subtitle">
                    Sign in to your TezConnect account
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        email = st.text_input("Email Address")
        password = st.text_input("Password", type="password")

        st.markdown('<div class="gold-btn">', unsafe_allow_html=True)

        if st.button("Sign In →", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="margin-top:25px;text-align:center;">
                <span class="muted">
                    10,000+ professionals joined
                </span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

# =========================
# MAIN APP
# =========================
else:

    # DASHBOARD
    if menu == "Dashboard":

        st.markdown(
            """
            <div class="top-banner">
                <div style="font-size:13px;color:#5b6480;font-weight:700;">
                    GOOD MORNING
                </div>

                <div style="
                    font-size:30px;
                    font-weight:800;
                    margin-top:6px;
                ">
                    Welcome to TezConnect
                </div>

                <div style="
                    margin-top:10px;
                    color:#c9a84c;
                    font-weight:600;
                ">
                    India's B2B Professional Network
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="section-title">Platform Metrics</div>',
            unsafe_allow_html=True,
        )

        c1, c2, c3, c4 = st.columns(4)

        metrics = [
            ("382", "Connections"),
            ("4.2K", "Profile Views"),
            ("38", "Leads"),
            ("127", "Saves"),
        ]

        for col, metric in zip([c1, c2, c3, c4], metrics):
            with col:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <div class="metric-value">
                            {metric[0]}
                        </div>

                        <div class="metric-label">
                            {metric[1]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        st.write("")

        left, right = st.columns([2, 1])

        # FEED
        with left:

            st.markdown(
                '<div class="section-title">Personalized Feed</div>',
                unsafe_allow_html=True,
            )

            for user in sample_users:

                st.markdown(
                    f"""
                    <div class="feed-card">

                        <div style="
                            display:flex;
                            justify-content:space-between;
                            margin-bottom:12px;
                        ">

                            <div>
                                <div class="user-name">
                                    {user["name"]}
                                </div>

                                <div class="muted">
                                    {user["role"]} · {user["company"]}
                                </div>
                            </div>

                            <div style="
                                color:#c9a84c;
                                font-weight:700;
                            ">
                                {user["followers"]}
                            </div>

                        </div>

                        <div style="
                            color:#d5d9e5;
                            line-height:1.7;
                            font-size:13px;
                        ">
                            Building strong business networks and helping
                            entrepreneurs scale faster through B2B
                            collaborations.
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        # RIGHT SIDE
        with right:

            st.markdown(
                '<div class="section-title">Business Leads</div>',
                unsafe_allow_html=True,
            )

            for lead in leads:

                st.markdown(
                    f"""
                    <div class="card" style="margin-bottom:12px;">
                        <div style="
                            font-size:14px;
                            font-weight:700;
                            margin-bottom:5px;
                        ">
                            {lead["company"]}
                        </div>

                        <div class="muted">
                            {lead["need"]}
                        </div>

                        <div style="
                            margin-top:10px;
                            color:#c9a84c;
                            font-weight:700;
                        ">
                            {lead["budget"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            st.markdown(
                '<div class="section-title">Upcoming Events</div>',
                unsafe_allow_html=True,
            )

            for ev in events:

                st.markdown(
                    f"""
                    <div class="card" style="margin-bottom:12px;">
                        <div style="
                            color:#c9a84c;
                            font-size:12px;
                            font-weight:700;
                            margin-bottom:8px;
                        ">
                            {ev["date"]}
                        </div>

                        <div style="
                            font-size:14px;
                            font-weight:700;
                            margin-bottom:5px;
                        ">
                            {ev["title"]}
                        </div>

                        <div class="muted">
                            📍 {ev["location"]}
                        </div>

                        <div style="
                            margin-top:10px;
                            color:#22c55e;
                            font-weight:700;
                        ">
                            {ev["price"]}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

    # NETWORK
    elif menu == "Network":

        st.markdown(
            '<div class="section-title">Professional Network</div>',
            unsafe_allow_html=True,
        )

        search = st.text_input("Search professionals")

        cols = st.columns(3)

        for i, user in enumerate(sample_users):

            with cols[i % 3]:

                st.markdown(
                    f"""
                    <div class="card">

                        <div style="
                            width:70px;
                            height:70px;
                            border-radius:50%;
                            background:linear-gradient(135deg,#c9a84c,#4f8ef7);
                            display:flex;
                            align-items:center;
                            justify-content:center;
                            margin:auto;
                            font-size:24px;
                            font-weight:800;
                            margin-bottom:14px;
                        ">
                            {user["name"][0]}
                        </div>

                        <div style="
                            text-align:center;
                            font-weight:700;
                            font-size:16px;
                        ">
                            {user["name"]}
                        </div>

                        <div class="muted" style="text-align:center;">
                            {user["role"]}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                st.button(
                    "Connect",
                    key=user["name"],
                    use_container_width=True,
                )

    # LEADS
    elif menu == "Leads":

        st.markdown(
            '<div class="section-title">Business Opportunities</div>',
            unsafe_allow_html=True,
        )

        for lead in leads:

            st.markdown(
                f"""
                <div class="card" style="margin-bottom:16px;">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">

                        <div>
                            <div style="
                                font-size:16px;
                                font-weight:700;
                            ">
                                {lead["company"]}
                            </div>

                            <div class="muted">
                                {lead["need"]}
                            </div>
                        </div>

                        <div style="
                            color:#c9a84c;
                            font-weight:800;
                        ">
                            {lead["budget"]}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    # EVENTS
    elif menu == "Events":

        st.markdown(
            '<div class="section-title">Upcoming Events</div>',
            unsafe_allow_html=True,
        )

        for ev in events:

            st.markdown(
                f"""
                <div class="card" style="margin-bottom:16px;">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                    ">

                        <div>
                            <div style="
                                color:#c9a84c;
                                font-weight:700;
                                margin-bottom:8px;
                            ">
                                {ev["date"]}
                            </div>

                            <div style="
                                font-size:18px;
                                font-weight:700;
                            ">
                                {ev["title"]}
                            </div>

                            <div class="muted">
                                📍 {ev["location"]}
                            </div>
                        </div>

                        <div style="
                            color:#22c55e;
                            font-weight:800;
                        ">
                            {ev["price"]}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

    # PROFILE
    elif menu == "Profile":

        st.markdown(
            '<div class="section-title">Edit Profile</div>',
            unsafe_allow_html=True,
        )

        with st.form("profile_form"):

            col1, col2 = st.columns(2)

            with col1:
                name = st.text_input("Full Name")

            with col2:
                role = st.text_input("Role")

            company = st.text_input("Company")
            website = st.text_input("Website")
            location = st.text_input("Location")

            bio = st.text_area("Bio")

            submitted = st.form_submit_button("Save Profile")

            if submitted:
                st.success("Profile updated successfully!")
