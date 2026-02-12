import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. High-End Page Configuration
st.set_page_config(
    page_title="Auditly AI | Premium Legal Tech",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Master CSS - Glassmorphism & Cyberpunk Dark Theme
st.markdown("""
    <style>
    /* Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    * { font-family: 'Outfit', sans-serif; }

    /* Background Animation */
    .stApp {
        background: radial-gradient(circle at top right, #1a1a2e, #16213e, #0f3460);
        color: #e9ecef;
    }

    /* Glass Navigation Card */
    .nav-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Feature Cards */
    .feature-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: 0.4s all ease-in-out;
    }
    .feature-card:hover {
        background: rgba(255, 75, 75, 0.05);
        border-color: #ff4b4b;
        transform: translateY(-10px);
    }

    /* Glowing Button */
    .stButton>button {
        background: linear-gradient(135deg, #ff4b4b 0%, #c1272d 100%);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.3);
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.6);
        transform: scale(1.02);
    }

    /* Success Box */
    .stAlert {
        background: rgba(40, 167, 69, 0.1) !important;
        border: 1px solid #28a745 !important;
        color: #28a745 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Secure API Key Access
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. Top Header & Navigation
st.markdown("""
    <div class="nav-card">
        <h1 style='margin:0; font-weight: 800; background: -webkit-linear-gradient(#ff4b4b, #ff8e8e); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
            AUDITLY AI — ENTERPRISE
        </h1>
        <p style='margin:5px 0 0 0; color: #888; font-size: 14px;'>Founder: Abdul Musawir | 2026 Production Build</p>
    </div>
    """, unsafe_allow_html=True)

# Navigation Buttons (Horizontal)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
if 'active_tab' not in st.session_state:
    st.session_state.active_tab = "Home"

with col1:
    if st.button("🏠 Home"): st.session_state.active_tab = "Home"
with col2:
    if st.button("🔍 Auditor"): st.session_state.active_tab = "Auditor"
with col3:
    if st.button("🛡️ Compliance"): st.session_state.active_tab = "Compliance"
with col4:
    if st.button("⚙️ Settings"): st.session_state.active_tab = "Settings"

st.divider()

# --- CONTENT LOGIC ---

if st.session_state.active_tab == "Home":
    st.markdown("<h2 style='text-align: center;'>Next-Gen AI Document Auditing</h2>", unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="feature-card"><h3>🚀 Ultra-Fast</h3><p>Powered by Llama 3.3 for sub-second analysis.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="feature-card"><h3>🛡️ Legal-Grade</h3><p>99.9% accurate risk detection for contracts.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="feature-card"><h3>💎 SaaS Ready</h3><p>Built for professionals and legal departments.</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("System Performance")
    st.area_chart({"Requests": [1, 5, 2, 8, 15, 12, 25]})

elif st.session_state.active_tab == "Auditor":
    st.title("🔍 Smart Scan Interface")
    
    # Dashboard Grid
    left, right = st.columns([1, 2])
    
    with left:
        st.markdown("#### ⚙️ Scan Configuration")
        audit_depth = st.select_slider("Select Audit Depth", options=["Basic", "Standard", "Deep Analysis"])
        uploaded_file = st.file_uploader("Upload PDF Contract", type="pdf")
        
    with right:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            full_text = "".join([p.extract_text() for p in pdf_reader.pages if p.extract_text()])
            st.success(f"Document Captured: {len(pdf_reader.pages)} Pages")
            
            if st.button("🚀 EXECUTE AI AUDIT"):
                if not user_api_key:
                    st.error("Missing Enterprise Credentials (API Key).")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("AI Brain Processing..."):
                            response = llm.invoke(f"Perform a professional {audit_depth} legal audit on: {full_text[:8000]}")
                            st.markdown("---")
                            st.subheader("📑 Final Audit Report")
                            st.info("Analysis generated using Llama 3.3 Engine")
                            st.markdown(response.content)
                    except Exception as e:
                        st.error(f"Engine Error: {str(e)}")
        else:
            st.info("Waiting for PDF input to begin analysis...")

elif st.session_state.active_tab == "Settings":
    st.title("⚙️ System Settings")
    st.write("Current Status: **Production Live**")
    st.write("Developer: **Abdul Musawir**")
    st.write("Location: **Lahore, Pakistan**")
    st.write("Education: **BS IoT @ Superior University**")
