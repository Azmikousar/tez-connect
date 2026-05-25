import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import io
import base64

# ─── COLOR PALETTE & STYLES ───
C = {
    "bg": "#07080c", "surface": "#0d0f18", "card": "#111520", "border": "#1c2136",
    "accent": "#c9a84c", "accentSoft": "#c9a84c18", "accentMid": "#c9a84c33",
    "blue": "#4f8ef7", "blueSoft": "#4f8ef714", "green": "#22c55e", "greenSoft": "#22c55e14",
    "purple": "#a78bfa", "purpleSoft": "#a78bfa14", "red": "#f87171", "redSoft": "#f8717114",
    "orange": "#fb923c", "orangeSoft": "#fb923c14",
    "text": "#eef0f8", "muted": "#5b6480", "subtle": "#1e2540"
}

avatarColors = ["#c9a84c", "#4f8ef7", "#22c55e", "#f87171", "#a78bfa", "#fb923c"]
CATEGORIES = ["Entrepreneur", "Business Owner", "Startup", "Freelancer", "Digital Marketer", "Coach & Trainer", "Investor", "Influencer", "Agency", "Student", "Recruiter", "Professional"]

# ─── INJECT GLOBAL CUSTOM CSS FOR THEME ───
st.set_page_config(page_title="TezConnect", page_icon="⚡", layout="centered")

st.markdown(f"""
    <link href="https://fonts.googleapis.com/css2?family=Syne:wght@600;700;800&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        .stApp {{
            background-color: {C['bg']};
            color: {C['text']};
            font-family: 'DM Sans', sans-serif;
        }}
        h1, h2, h3, .syne-text {{
            font-family: 'Syne', sans-serif !important;
        }}
        /* Glowing Cards Styling */
        .glow-card {{
            background-color: {C['card']};
            border: 1px solid {C['border']};
            border-radius: 18px;
            padding: 20px;
            margin-bottom: 14px;
            transition: all 0.22s;
        }}
        .glow-card:hover {{
            background-color: #141828;
            border-color: {C['accent']}44;
        }}
        .hot-card {{
            box-shadow: 0 0 20px {C['red']}14;
            border-color: {C['red']}44;
        }}
        /* Badges */
        .badge {{
            font-family: 'Syne', sans-serif;
            font-size: 10px;
            font-weight: 700;
            padding: 2px 9px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: inline-block;
        }}
    </style>
""", unsafe_allowed_html=True)

# ─── SESSION STATE INITIALIZATION ───
if "is_logged_in" not in st.session_state:
    st.session_state.is_logged_in = False
if "auth_view" not in st.session_state:
    st.session_state.auth_view = "login"
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "", "role": "", "company": "", "category": "", "website": "", "whatsapp": "", "bio": "", "location": "",
        "photo": None, "skills": [], "services": [], "experience": [], "portfolio": []
    }

# ─── HELPER FUNCTIONS ───
def get_avatar_html(name, photo_b64=None, size=40, idx=0, online=False):
    initials = "".join([n[0] for n in name.split()]).upper()[:2] if name else "?"
    bg_gradient = f"linear-gradient(135deg, {avatarColors[idx%6]}, {avatarColors[(idx+2)%6]})"
    
    avatar_content = f'<img src="data:image/png;base64,{photo_b64}" style="width:100%;height:100%;object-fit:cover;"/>' if photo_b64 else initials
    online_dot = f'<div style="position:absolute;bottom:1px;right:1px;width:10px;height:10px;background:{C["green"]};border-radius:50%;border:2px solid {C["bg"]};"></div>' if online else ''
    
    return f"""
    <div style="position:relative; display:inline-block; width:{size}px; height:{size}px;">
        <div style="width:{size}px; height:{size}px; border-radius:50%; overflow:hidden;
            background:{'none' if photo_b64 else bg_gradient}; display:flex; align-items:center; justify-content:center;
            font-size:{size*0.36}px; font-weight:800; color:#fff; font-family:'Syne'; border:2px solid {C['border']};">
            {avatar_content}
        </div>
        {online_dot}
    </div>
    """

# Mock Data Constants
sample_users = [
    {"name": "Priya Sharma", "role": "Digital Marketing Head", "company": "BrandBoost", "category": "Digital Marketer", "location": "Delhi", "followers": "3.2K", "connections": "891"},
    {"name": "Rahul Gupta", "role": "Angel Investor", "company": "GV Capital", "category": "Investor", "location": "Bangalore", "followers": "5.6K", "connections": "1.2K"},
    {"name": "Sneha Patil", "role": "Business Coach", "company": "GrowthMind", "category": "Coach & Trainer", "location": "Pune", "followers": "2.1K", "connections": "543"}
]

# ─── SCREEN: AUTHENTICATION (LOGIN / SIGNUP) ───
def render_auth_screen():
    st.markdown("<div style='text-align: center; margin-top: 30px;'>", unsafe_allowed_html=True)
    st.markdown(f'<div style="width: 50px; height: 50px; border-radius: 14px; background: linear-gradient(135deg,{C["accent"]},#a07830); display: flex; align-items: center; justify-content: center; font-size: 24px; margin: 0 auto 12px;">⚡</div>', unsafe_allowed_html=True)
    
    if st.session_state.auth_view == "login":
        st.markdown(f"<h2 class='syne-text' style='text-align:center;'>Welcome Back</h2>", unsafe_allowed_html=True)
        st.markdown(f"<p style='color:{C['muted']}; text-align:center; font-size:13px;'>Secure your next high-value B2B deal</p>", unsafe_allowed_html=True)
        
        email = st.text_input("Email Address *", placeholder="name@company.com")
        password = st.text_input("Password *", type="password", placeholder="••••••••")
        
        if st.button("Sign In →", use_container_width=True):
            if email and password:
                st.session_state.profile["name"] = "Azmi"  # Default fallback name
                st.session_state.is_logged_in = True
                st.rerun()
            else:
                st.error("Please fill in all fields.")
                
        st.markdown(f"<p style='text-align:center; font-size:13px; color:{C['muted']}'>New to TezConnect? </p>", unsafe_allowed_html=True)
        if st.button("Reach out & Join", use_container_width=True):
            st.session_state.auth_view = "signup"
            st.rerun()
            
    else:
        st.markdown(f"<h2 class='syne-text' style='text-align:center;'>Create Account</h2>", unsafe_allowed_html=True)
        st.markdown(f"<p style='color:{C['muted']}; text-align:center; font-size:13px;'>Join India's premier B2B creative community</p>", unsafe_allowed_html=True)
        
        name = st.text_input("Full Name *", placeholder="e.g. Azmi Kousar")
        category = st.selectbox("Business Category", [""] + CATEGORIES)
        email = st.text_input("Email Address *", placeholder="name@company.com")
        password = st.text_input("Password *", type="password", placeholder="••••••••")
        
        if st.button("Register Account 🚀", use_container_width=True):
            if name and email and password:
                st.session_state.profile["name"] = name
                st.session_state.profile["category"] = category
                st.session_state.is_logged_in = True
                st.rerun()
            else:
                st.error("Name, Email, and Password are required.")
                
        st.markdown(f"<p style='text-align:center; font-size:13px; color:{C['muted']}'>Already have an account?</p>", unsafe_allowed_html=True)
        if st.button("Sign In Instead", use_container_width=True):
            st.session_state.auth_view = "login"
            st.rerun()

# ─── SCREEN: DASHBOARD ───
def render_dashboard():
    profile = st.session_state.profile
    
    # Welcome Banner
    st.markdown(f"""
    <div style="background: linear-gradient(135deg,#101628 0%,#0d1420 50%,#141020 100%); border: 1px solid {C['accent']}33; border-radius: 20px; padding: 20px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center; gap: 14px;">
            {get_avatar_html(profile['name'], size=52, online=True)}
            <div>
                <div style="font-size: 12px; color: {C['muted']}; font-weight: 600; letter-spacing: 0.06em; text-transform: uppercase;">Good morning 👋</div>
                <div style="font-family: 'Syne'; font-weight: 800; color: {C['text']}; font-size: 20px; line-height: 1.1;">Welcome, {profile['name']}</div>
                <div style="font-size: 11px; color: {C['accent']}; font-weight: 600; margin-top: 2px;">{profile['role'] or 'B2B Professional'} {' · ' + profile['company'] if profile['company'] else ''}</div>
            </div>
        </div>
    </div>
    """, unsafe_allowed_html=True)
    
    # Stats Grid
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown(f"<div class='glow-card' style='text-align:center; padding:10px;'><span style='font-size:18px;'>🔗</span><br/><b style='color:{C['blue']}; font-size:16px;'>382</b><br/><span style='font-size:9px; color:{C['muted']};'>CONNECTIONS</span></div>", unsafe_allowed_html=True)
    with col2: st.markdown(f"<div class='glow-card' style='text-align:center; padding:10px;'><span style='font-size:18px;'>👁️</span><br/><b style='color:{C['accent']}; font-size:16px;'>4.2K</b><br/><span style='font-size:9px; color:{C['muted']};'>VIEWS</span></div>", unsafe_allowed_html=True)
    with col3: st.markdown(f"<div class='glow-card' style='text-align:center; padding:10px;'><span style='font-size:18px;'>🎯</span><br/><b style='color:{C['green']}; font-size:16px;'>38</b><br/><span style='font-size:9px; color:{C['muted']};'>LEADS</span></div>", unsafe_allowed_html=True)
    with col4: st.markdown(f"<div class='glow-card' style='text-align:center; padding:10px;'><span style='font-size:18px;'>⭐</span><br/><b style='color:{C['purple']}; font-size:16px;'>127</b><br/><span style='font-size:9px; color:{C['muted']};'>SAVES</span></div>", unsafe_allowed_html=True)

    # Core Content
    st.markdown("<h3 class='syne-text' style='font-size:16px;'>Platform Goals</h3>", unsafe_allowed_html=True)
    for goal in primaryGoals:
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:12px; padding:10px; background:#ffffff05; border:1px solid {goal['color']}22; border-radius:12px; margin-bottom:8px;">
            <div style="width:34px; height:34px; border-radius:10px; background:{goal['color']}18; display:flex; align-items:center; justify-content:center; font-size:16px;">{goal['icon']}</div>
            <div>
                <div style="font-weight:700; color:{C['text']}; font-size:12px;">{goal['title']}</div>
                <div style="font-size:11px; color:{C['muted']};">{goal['desc']}</div>
            </div>
        </div>
        """, unsafe_allowed_html=True)

# ─── SCREEN: NETWORK ───
def render_network():
    st.markdown("<h3 class='syne-text'>Discover Professionals</h3>", unsafe_allowed_html=True)
    search = st.text_input("🔍 Search professionals, roles...", placeholder="Search...")
    
    for u in sample_users:
        if search.lower() in u['name'].lower() or search.lower() in u['role'].lower():
            st.markdown(f"""
            <div class='glow-card'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <div style='display:flex; gap:12px; align-items:center;'>
                        {get_avatar_html(u['name'], size=46)}
                        <div>
                            <b style='color:{C['text']}; font-size:14px;'>{u['name']} ✓</b>
                            <div style='color:{C['muted']}; font-size:11px;'>{u['role']} · {u['company']}</div>
                            <span class='badge' style='background:{C['blue']}22; color:{C['blue']};'>{u['category']}</span>
                        </div>
                    </div>
                    <div style='text-align:right; font-size:11px; color:{C['muted']};'>
                        <div><b>Conn:</b> {u['connections']}</div>
                        <div><b>Follows:</b> {u['followers']}</div>
                    </div>
                </div>
            </div>
            """, unsafe_allowed_html=True)

# ─── SCREEN: LEADS ───
def render_leads():
    st.markdown("<h3 class='syne-text'>Business Opportunities</h3>", unsafe_allowed_html=True)
    
    opps = [
        {"title": "Co-Founder (Tech) Needed", "company": "HealthAI Startup", "budget": "Equity", "urgent": True},
        {"title": "B2B SaaS Sales Partner", "company": "CloudFlow Inc.", "budget": "₹50K/mo", "urgent": False},
        {"title": "Content Agency for FinTech", "company": "PaySecure", "budget": "₹1.2L/mo", "urgent": True}
    ]
    
    for o in opps:
        urgency_badge = f"<span class='badge' style='background:{C['red']}; color:#000;'>Urgent</span>" if o['urgent'] else ""
        st.markdown(f"""
        <div class="glow-card {'hot-card' if o['urgent'] else ''}">
            <div style='display:flex; justify-content:space-between;'>
                <div>
                    <div style='margin-bottom:4px;'>{urgency_badge}</div>
                    <b style='font-size:14px; color:{C['text']};'>{o['title']}</b>
                    <div style='font-size:11px; color:{C['muted']};'>{o['company']}</div>
                </div>
                <div style='color:{C['accent']}; font-weight:800; font-size:13px;'>{o['budget']}</div>
            </div>
        </div>
        """, unsafe_allowed_html=True)

# ─── SCREEN: PROFILE & EDIT SCREEN ───
def render_profile():
    profile = st.session_state.profile
    
    edit_mode = st.toggle("✏️ Edit Mode Setup")
    
    if edit_mode:
        st.markdown("<h3 class='syne-text'>Update Workspace Profile</h3>", unsafe_allowed_html=True)
        profile["name"] = st.text_input("Full Name *", value=profile["name"])
        profile["role"] = st.text_input("Job Title / Role *", value=profile["role"], placeholder="e.g. Lead Designer")
        profile["company"] = st.text_input("Company Name", value=profile["company"])
        profile["bio"] = st.text_area("Bio / Professional Story", value=profile["bio"])
        profile["whatsapp"] = st.text_input("WhatsApp Link/Number", value=profile["whatsapp"])
        profile["website"] = st.text_input("Website Link", value=profile["website"])
        
        if st.button("💾 Complete Setup"):
            st.success("Aura Studio profile configs saved successfully!")
            st.rerun()
    else:
        # Profile View
        st.markdown(f"""
        <div style='text-align:center; padding: 20px 0;'>
            {get_avatar_html(profile['name'], size=80)}
            <h2 class='syne-text' style='margin-bottom:2px;'>{profile['name'] or 'Your Name'}</h2>
            <div style='color:{C['accent']}; font-size:13px; font-weight:600;'>{profile['role'] or 'Creative Consultant'}</div>
            <div style='color:{C['muted']}; font-size:11px;'>{profile['company'] or 'Aura Visuals Design Studio'}</div>
        </div>
        <div class='glow-card'>
            <h4 class='syne-text' style='margin:0 0 6px 0; font-size:13px; color:{C['accent']};'>ABOUT / WORK PROFILE</h4>
            <p style='font-size:12px; color:#c5c9db; line-height:1.6;'>{profile['bio'] or 'A dedicated professional offering modern, clean, and purposeful creative digital solutions.'}</p>
        </div>
        """, unsafe_allowed_html=True)
        
        if profile['whatsapp']:
            st.link_button(f"💬 Reach out via WhatsApp", f"https://wa.me/{profile['whatsapp']}", use_container_width=True)
            
        st.markdown("<br/>", unsafe_allowed_html=True)
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.is_logged_in = False
            st.session_state.auth_view = "login"
            st.rerun()

# ─── HARDCODED DATA COMPILING FOR PLATFORM GOALS ───
primaryGoals = [
    {"icon": "🌐", "title": "Business Networking Ecosystem", "desc": "Connect entrepreneurs, investors & professionals nationwide", "color": C["blue"]},
    {"icon": "🤝", "title": "B2B Collaborations", "desc": "Increase high-value business partnerships & deals", "color": C["green"]},
    {"icon": "⚡", "title": "Simplify Networking", "desc": "One platform for all your professional connections", "color": C["accent"]},
    {"icon": "🎯", "title": "Lead Generation", "desc": "Generate qualified business leads every day", "color": C["orange"]}
]

# ─── MAIN APP ROUTER ───
def main():
    if not st.session_state.is_logged_in:
        render_auth_screen()
    else:
        # Header Layout
        st.markdown(f"""
        <div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid {C['border']}; padding-bottom: 12px; margin-bottom: 20px;">
            <div style="display: flex; align-items: center; gap: 10px;">
                <div style="width:32px; height:32px; border-radius:9px; background:linear-gradient(135deg,{C['accent']},#a07830); display:flex; align-items:center; justify-content:center; font-size:16px;">⚡</div>
                <div>
                    <div style="font-family:'Syne'; font-weight:800; font-size:18px; color:{C['accent']}; line-height:1;">TezConnect</div>
                    <div style="font-size:8px; color:{C['muted']}; letter-spacing:0.18em; text-transform:uppercase;">B2B Network</div>
                </div>
            </div>
        </div>
        """, unsafe_allowed_html=True)
        
        # Bottom Navigation Alternative using Option-Menu framework layout styling
        selected_nav = option_menu(
            menu_title=None,
            options=["Dashboard", "Network", "Leads", "Profile"],
            icons=["grid-fill", "globe", "target", "person-fill"],
            menu_icon="cast",
            default_index=0,
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": C["surface"], "border": f"1px solid {C['border']}", "border-radius": "12px"},
                "icon": {"color": C["muted"], "font-size": "14px"}, 
                "nav-link": {"font-size": "11px", "text-align": "center", "margin": "0px", "color": C["text"], "font-family": "Syne"},
                "nav-link-selected": {"background-color": C["accentSoft"], "color": C["accent"], "border-bottom": f"2px solid {C['accent']}"},
            }
        )
        
        st.markdown("<br/>", unsafe_allowed_html=True)
        
        if selected_nav == "Dashboard":
            render_dashboard()
        elif selected_nav == "Network":
            render_network()
        elif selected_nav == "Leads":
            render_leads()
        elif selected_nav == "Profile":
            render_profile()

if __name__ == "__main__":
    main()
