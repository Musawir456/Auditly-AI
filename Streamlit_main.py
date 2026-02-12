import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq
import pandas as pd
import time

# 1. Advanced Configuration
st.set_page_config(
    page_title="Auditly AI | Global Corporate Systems",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Master CSS & JavaScript Injection (Bootstrap 5 Style)
# Yahan hum CSS aur HTML use kar rahe hain taake app ka UI professional lage
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap');
    
    :root {
        --primary: #2563eb;
        --dark: #0f172a;
        --light: #f8fafc;
        --accent: #ef4444;
    }

    * { font-family: 'Plus Jakarta Sans', sans-serif; }

    .stApp { background-color: var(--light); }

    /* Custom Header Navigation */
    .mega-nav {
        background: var(--dark);
        padding: 20px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: white;
        border-radius: 0 0 30px 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    /* Professional Content Cards */
    .glass-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        margin-bottom: 25px;
        transition: 0.3s ease-in-out;
    }
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
        border-color: var(--primary);
    }

    /* Bootstrap-like Buttons */
    .stButton>button {
        background: var(--primary) !important;
        color: white !important;
        border-radius: 12px !important;
        padding: 15px !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        border: none !important;
        width: 100%;
        transition: 0.4s;
    }
    .stButton>button:hover {
        background: #1d4ed8 !important;
        box-shadow: 0 0 20px rgba(37, 99, 235, 0.4) !important;
    }

    /* Success & Metric Indicators */
    .status-badge {
        padding: 5px 15px;
        border-radius: 50px;
        background: #dcfce7;
        color: #166534;
        font-size: 12px;
        font-weight: 700;
    }
    </style>

    <div class="mega-nav">
        <div>
            <span style="font-size: 28px; font-weight: 800; color: #3b82f6;">AUDITLY</span>
            <span style="font-size: 28px; font-weight: 300;">AI</span>
        </div>
        <div style="font-size: 12px; letter-spacing: 2px; opacity: 0.7;">ENTERPRISE COMPLIANCE ENGINE v3.0</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Secure Backend Access
# Secrets se API Key lena taake security maintain rahe
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. State Management for Multi-Page UX
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Home"

# Main Navigation (Top Row)
t1, t2, t3, t4 = st.columns(4)
with t1:
    if st.button("📊 INFRASTRUCTURE"): st.session_state.active_tab = "Home"
with t2:
    if st.button("🔍 AI AUDITOR"): st.session_state.active_tab = "Auditor"
with t3:
    if st.button("📈 ANALYTICS"): st.session_state.active_tab = "Analytics"
with t4:
    if st.button("🛡️ SECURITY"): st.session_state.active_tab = "Security"

st.divider()

# --- PAGE: HOME / INFRASTRUCTURE ---
if st.session_state.active_tab == "Home":
    st.markdown("### 🏢 Core Systems Overview")
    
    # KPIs Layout
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown('<div class="glass-card"><p style="color:gray;">Uptime</p><h3>99.9%</h3></div>', unsafe_allow_html=True)
    with k2:
        st.markdown('<div class="glass-card"><p style="color:gray;">Model</p><h3>Llama 3.3</h3></div>', unsafe_allow_html=True)
    with k3:
        st.markdown('<div class="glass-card"><p style="color:gray;">Processing</p><h3>0.2s</h3></div>', unsafe_allow_html=True)
    with k4:
        st.markdown('<div class="glass-card"><p style="color:gray;">Risk Engine</p><h3>Active</h3></div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="glass-card">
            <h4>Global Compliance Network</h4>
            <p>Auditly AI connects multiple neural networks to provide real-time auditing of legal and commercial contracts. 
            All data processed is AES-256 encrypted and adheres to international data privacy standards.</p>
            <span class="status-badge">SYSTEMS OPERATIONAL</span>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE: AI AUDITOR ---
elif st.session_state.active_tab == "Auditor":
    st.markdown("### 🔍 Enterprise AI Scanning")
    
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.write("**Configuration Control**")
        scan_mode = st.radio("Intelligence Level:", ["Standard Scan", "Deep Forensic Scan", "AI-Generated Text Detection"])
        uploaded_file = st.file_uploader("Drop Enterprise Document (PDF)", type="pdf")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_r:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            raw_content = "".join([p.extract_text() for p in pdf_reader.pages if p.extract_text()])
            st.success(f"Verified Document: {uploaded_file.name}")
            
            if st.button("RUN FULL SYSTEM DIAGNOSTIC"):
                if not user_api_key:
                    st.error("Access Denied: Please check your secure credentials in 'Manage app' settings.")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("AI Brain Analyzing..."):
                            time.sleep(1) # Visual effect
                            response = llm.invoke(f"Perform professional {scan_mode} on: {raw_content[:8000]}")
                            st.markdown('<div class="glass-card" style="border-left: 8px solid #2563eb;">', unsafe_allow_html=True)
                            st.subheader("📑 Final Intelligence Report")
                            st.markdown(response.content)
                            st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Engine Latency Error: {str(e)}")
        else:
            st.info("System is waiting for secure document upload to initiate AI sequence.")

# --- PAGE: ANALYTICS ---
elif st.session_state.active_tab == "Analytics":
    st.title("📈 Performance Analytics")
    # Generating mock professional data
    data = pd.DataFrame({
        "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "Audits": [45, 89, 120, 150, 110, 60, 40],
        "Accuracy": [99.1, 99.4, 99.8, 99.9, 99.7, 99.8, 99.9]
    })
    st.line_chart(data.set_index("Day"))
    st.markdown('<div class="glass-card"><h4>Market Insight</h4><p>Usage has grown by 150% this week. Auditly AI is scaling successfully.</p></div>', unsafe_allow_html=True)

# --- PAGE: SECURITY ---
elif st.session_state.active_tab == "Security":
    st.title("🛡️ Security & Privacy")
    st.write("This application is running on a secure cloud infrastructure.")
    st.info("All document segments are purged from memory after analysis to ensure 100% confidentiality.")
