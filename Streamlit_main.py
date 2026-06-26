import streamlit as st
import requests
import pandas as pd

# ---------------------------------------------------
# ⚖️ GLOBAL BRANDING & GLOBAL CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="Auditly AI | Enterprise Intelligence Hub",
    page_icon="⚖️",
    layout="wide"
)

DJANGO_BACKEND_URL = "http://127.0.0.1:8000/api/v1/scan/"

# ---------------------------------------------------
# 🎨 BRAND THEME: FUTURISTIC NEON DIGITAL CIRCUIT
# ---------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&display=swap');

* { font-family: 'Outfit', sans-serif; }

.stApp {
    background: radial-gradient(circle at 50% 30%, #0B132B 0%, #030712 100%);
    color: #f8fafc;
}

/* Premium Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050B14 0%, #0B132B 100%) !important;
    border-right: 2px solid rgba(0, 240, 255, 0.2) !important;
}

/* Glassmorphism Cards */
.metric-card {
    background: rgba(11, 19, 43, 0.45);
    border: 1px solid rgba(0, 240, 255, 0.2);
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    backdrop-filter: blur(10px);
}

/* Neon Glow Buttons */
.stButton>button {
    background: linear-gradient(90deg, #00F0FF, #8A2BE2);
    color: white !important;
    border-radius: 10px;
    padding: 14px 28px;
    font-weight: 700;
    font-size: 15px;
    border: none;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    width: 100%;
    box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
    transition: 0.3s ease;
}
.stButton>button:hover {
    box-shadow: 0 0 30px rgba(138, 43, 226, 0.8);
    transform: translateY(-2px);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 🛰️ DYNAMIC SIDEBAR CONTROL CENTER
# ---------------------------------------------------
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 10px 0;">
        <img src="https://img.icons8.com/nolan/96/scale.png" style="width:65px; filter: drop-shadow(0 0 10px #00F0FF);">
        <div style="font-size: 24px; font-weight: 800; color: #00F0FF; letter-spacing: 1px; margin-top:10px;">Auditly AI</div>
        <div style="font-size: 12px; color: #94a3b8; font-family: monospace;">Enterprise Suite</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Active Navigation Icons
    st.markdown("🔴 **Dashboard**")
    st.markdown("🔍 **Smart Auditor**")
    st.markdown("📊 **Market Analytics**")
    st.markdown("🔐 **Security Hub**")
    
    st.divider()
    
    # System Telemetry Handshake Badge
    st.markdown("""
    <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid #00F0FF; padding: 12px; border-radius: 10px; font-family: monospace; font-size: 12px;">
        <span style="color: #39FF14;">●</span> System: Connected to Django Core
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    st.caption("© 2026 Auditly Global Systems")

# ---------------------------------------------------
# 🏢 MAIN COCKPIT: PLATFORM METRICS
# ---------------------------------------------------
st.markdown("<h1 style='color: #f8fafc; font-weight: 800; font-size: 38px; margin-top:0;'>Global Risk Command Center</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 4-Column Cockpit Counters Layout
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">Global Uptime</p><p style="color:white; font-size:28px; font-weight:700; margin:5px 0;">99.99%</p><span style="color:#39FF14; font-size:12px;">↑ Stable</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">Neural Engine</p><p style="color:white; font-size:28px; font-weight:700; margin:5px 0;">Django + LLM</p><span style="color:#39FF14; font-size:12px;">↑ Distributed</span></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">API Latency</p><p style="color:white; font-size:28px; font-weight:700; margin:5px 0;">95ms</p><span style="color:#f43f5e; font-size:12px;">↓ -45ms (Optimized)</span></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="metric-card"><p style="color:#94a3b8; font-size:12px; margin:0;">Active Audits</p><p style="color:white; font-size:28px; font-weight:700; margin:5px 0;">4,120</p><span style="color:#39FF14; font-size:12px;">↑ +12%</span></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------------------------------------
# 📂 CENTRAL PLATFORM WORKING MATRIX
# ---------------------------------------------------
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown('<div class="metric-card" style="border-color: rgba(138, 43, 226, 0.4);">', unsafe_allow_html=True)
    st.markdown("<h3 style='color:#00F0FF; margin-top:0; font-weight:700;'>⚖️ Smart Legal Compliance</h3>", unsafe_allow_html=True)
    st.write("Auditly AI uses decentralized Django endpoints to parse incoming financial and legal structures, ensuring full sandboxed validation against active compliance matrix grids.")
    
    # Simple File Uploader Element
    uploaded_file = st.file_uploader("Upload Target PDF Layout Document", type="pdf", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Execute Secure Audit Runtime"):
            with st.spinner("Streaming binary payload to secure Django architecture..."):
                try:
                    files_payload = {'file': (uploaded_file.name, uploaded_file.getvalue(), 'application/pdf')}
                    response = requests.post(DJANGO_BACKEND_URL, files=files_payload)
                    
                    if response.status_code == 200:
                        st.session_state['audit_result'] = response.json().get('analysis')
                    else:
                        st.error(f"Engine Fault Signal: HTTP Code {response.status_code}")
                except requests.exceptions.ConnectionError:
                    st.error("Connection Refused: Make sure your Django terminal server is live.")

with col_right:
    if 'audit_result' in st.session_state:
        st.markdown('<div class="metric-card" style="border-color: #39FF14; min-height: 250px;">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#39FF14; margin-top:0; font-weight:700;'>✓ Compliance Telemetry Report</h3>", unsafe_allow_html=True)
        st.write(st.session_state['audit_result'])
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="metric-card" style="min-height: 250px;">', unsafe_allow_html=True)
        st.markdown("<h3 style='color:#8A2BE2; margin-top:0; font-weight:700;'>🌐 Infrastructure Status</h3>", unsafe_allow_html=True)
        st.write("Enterprise data nodes are active. Django middleware handles token protection layers, securing all multi-tenant operations via localized vector pipelines.")
        st.markdown('</div>', unsafe_allow_html=True)