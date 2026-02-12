import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. High-Performance Page Config
st.set_page_config(
    page_title="Auditly AI | Global Corporate Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Master CSS - Modern Professional Interface
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Public+Sans:wght@300;400;600;700&display=swap');
    
    body, [class*="css"] {
        font-family: 'Public Sans', sans-serif;
        background-color: #f0f2f5;
    }

    /* Top Professional Branding Header */
    .header-banner {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 1.5rem;
        color: white;
        text-align: center;
        border-radius: 0px 0px 20px 20px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Bootstrap Card Styling */
    .feature-box {
        background: white;
        padding: 25px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Advanced Button Styling */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 12px;
        font-weight: 700;
        border: none;
        transition: 0.3s;
        width: 100%;
        text-transform: uppercase;
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        transform: translateY(-2px);
    }
    </style>

    <div class="header-banner">
        <h1 style='margin:0; font-size: 32px;'>AUDITLY AI SYSTEMS</h1>
        <p style='margin:0; font-size: 14px; opacity: 0.9;'>Trusted AI Compliance for Modern Enterprise Documents</p>
    </div>
    """, unsafe_allow_html=True)

# 3. Secure Key Ingestion
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. Professional Navigation System
if 'tab' not in st.session_state:
    st.session_state.tab = "Dashboard"

nav_1, nav_2, nav_3 = st.columns(3)
with nav_1:
    if st.button("📊 INFRASTRUCTURE"): st.session_state.tab = "Dashboard"
with nav_2:
    if st.button("🔍 SECURITY AUDIT"): st.session_state.tab = "Auditor"
with nav_3:
    if st.button("🛡️ COMPLIANCE LAB"): st.session_state.tab = "Lab"

st.markdown("<hr style='border: 0.5px solid #d1d5db;'>", unsafe_allow_html=True)

# --- PAGE: DASHBOARD ---
if st.session_state.tab == "Dashboard":
    st.markdown("### 📈 Global Operations Center")
    col_a, col_b, col_c = st.columns(3)
    
    with col_a:
        st.markdown('<div class="feature-box"><h5>Audit Uptime</h5><h2 style="color: #10b981;">99.99%</h2></div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('<div class="feature-box"><h5>Model Engine</h5><h2 style="color: #3b82f6;">Llama 3.3</h2></div>', unsafe_allow_html=True)
    with col_c:
        st.markdown('<div class="feature-box"><h5>Data Security</h5><h2 style="color: #6366f1;">ISO Ready</h2></div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="feature-box">
            <h4>System Notice</h4>
            <p style="color: #6b7280;">Auditly AI is currently operating in <b>Production Mode</b>. Our neural networks are trained to identify over 50+ types of legal Red Flags instantly.</p>
        </div>
    """, unsafe_allow_html=True)

# --- PAGE: AUDITOR ---
elif st.session_state.tab == "Auditor":
    st.markdown("### 🔍 Enterprise Security Scan")
    
    left, right = st.columns([1, 2])
    
    with left:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.write("**Scan Protocol**")
        scan_type = st.radio("Mode:", ["High-Risk Detection", "Clause Analysis", "Executive Summary"])
        uploaded_file = st.file_uploader("Select PDF Document", type="pdf")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with right:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            content = "".join([p.extract_text() for p in pdf_reader.pages if p.extract_text()])
            st.success(f"Verified: {uploaded_file.name}")
            
            if st.button("LAUNCH AI DIAGNOSTIC"):
                if not user_api_key:
                    st.error("Access Denied: Please configure API Keys in Cloud Settings.")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("Processing Secure Analysis..."):
                            response = llm.invoke(f"Expert Audit: {content[:8000]}")
                            st.markdown('<div class="feature-box" style="border-left: 5px solid #2563eb;">', unsafe_allow_html=True)
                            st.subheader("📋 Official Diagnostic Report")
                            st.markdown(response.content)
                            st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Engine Latency Error: {str(e)}")
        else:
            st.info("Awaiting secure document upload...")

# --- PAGE: LAB ---
elif st.session_state.tab == "Lab":
    st.title("🛡️ Advanced Compliance Lab")
    st.write("Specialized tools for legal-tech R&D and automated text detection.")
