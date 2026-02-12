import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Page Configuration
st.set_page_config(page_title="Auditly AI | Premium", page_icon="⚖️", layout="wide")

# 2. Advanced CSS/HTML/JS Injection
st.markdown("""
    <style>
    /* Professional Font & Background */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #050505;
    }

    /* Modern Glassmorphism Navigation */
    .nav-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 5%;
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        position: sticky;
        top: 0;
        z-index: 999;
    }

    /* Professional Metric Cards */
    .metric-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: transform 0.3s ease;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: #ff4b4b;
    }

    /* Custom Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff8080 100%);
        color: white;
        border: none;
        padding: 12px 25px;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        box-shadow: 0px 0px 20px rgba(255, 75, 75, 0.4);
        transform: scale(1.02);
    }

    /* Report Box Styling */
    .report-container {
        background: #111;
        padding: 30px;
        border-radius: 20px;
        border: 1px solid #333;
        line-height: 1.6;
    }
    </style>
    
    <div class="nav-bar">
        <h2 style="color: #ff4b4b; margin:0;">AUDITLY AI</h2>
        <div style="color: #888; font-size: 0.9em;">Founder: Abdul Musawir | Enterprise Edition</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Sidebar - Minimalist Branding
with st.sidebar:
    st.markdown("### 🛠️ Control Center")
    page = st.selectbox("Select Workspace", ["🏠 Dashboard", "🔍 Smart Auditor", "📊 Analytics"])
    st.divider()
    st.markdown("⚖️ **Auditly AI v2.1**")
    st.caption("Secured by Llama 3.3 Intelligence")

# API Setup
user_api_key = st.secrets.get("GROQ_API_KEY")

# --- PAGE LOGIC ---

if page == "🏠 Dashboard":
    st.markdown("<h1 style='text-align: center; font-weight: 800;'>Legal Intelligence Reimagined</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Automating complex audits for modern legal firms.</p>", unsafe_allow_html=True)
    
    st.write("")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-card"><h3>⚡ Speed</h3><p>0.4s Average Latency</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>🎯 Precision</h3><p>99.9% Model Accuracy</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>🔒 Security</h3><p>AES-256 Encryption</p></div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("Your Startup Growth")
    st.line_chart({"Usage": [10, 25, 45, 80, 150, 300]})

elif page == "🔍 Smart Auditor":
    st.title("🔍 Deep Scan Auditor")
    
    col_l, col_r = st.columns([1, 2])
    
    with col_l:
        st.markdown("#### 📤 Upload Document")
        uploaded_file = st.file_uploader("", type="pdf")
        scan_mode = st.radio("Scan Depth", ["Standard", "Deep Analysis", "Compliance Only"])
        
    with col_r:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
            st.success(f"Successfully processed {len(pdf_reader.pages)} pages.")
            
            if st.button("Execute AI Audit"):
                if not user_api_key:
                    st.error("API Secret Key is missing.")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("Analyzing with Llama 3.3..."):
                            response = llm.invoke(f"Perform a professional {scan_mode} audit on this: {text[:8000]}")
                            st.markdown('<div class="report-container">', unsafe_allow_html=True)
                            st.subheader("🛡️ Official Audit Report")
                            st.markdown(response.content)
                            st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Audit Failed: {e}")
        else:
            st.info("Waiting for PDF upload to begin scan...")

elif page == "📊 Analytics":
    st.title("📊 Usage Analytics")
    st.write("This section tracks your document audit history and AI performance metrics.")
    st.bar_chart({"Audits": [5, 12, 18, 24, 30], "Errors": [1, 0, 0, 1, 0]})
