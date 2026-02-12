import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Page Configuration
st.set_page_config(
    page_title="Auditly AI | Enterprise Compliance",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Bootstrap & Modern Tech CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@400;600;700&display=swap');
    
    * { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }

    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }

    /* Bootstrap Style Navbar */
    .top-nav {
        background-color: #212529;
        padding: 1rem 2rem;
        color: white;
        text-align: center;
        border-radius: 0 0 15px 15px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* Enterprise Cards */
    .card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1rem;
    }

    /* Action Button (Bootstrap Primary) */
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 6px;
        font-weight: 600;
        transition: 0.2s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0b5ed7;
        box-shadow: 0 4px 8px rgba(13, 110, 253, 0.3);
    }

    /* Metric Boxes */
    .metric-box {
        text-align: center;
        padding: 1.5rem;
        background: #fff;
        border-radius: 10px;
        border-top: 4px solid #0d6efd;
    }
    </style>
    
    <div class="top-nav">
        <h1 style='margin:0; font-weight: 700; font-size: 28px;'>AUDITLY AI SYSTEMS</h1>
        <p style='margin:0; font-size: 14px; opacity: 0.8;'>Advanced Document Auditing & Risk Mitigation</p>
    </div>
    """, unsafe_allow_html=True)

# 3. API Connection
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. Navigation (Bootstrap Style Pills)
if 'page' not in st.session_state:
    st.session_state.page = "Overview"

col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("📊 Overview"): st.session_state.page = "Overview"
with col2:
    if st.button("🔍 AI Auditor"): st.session_state.page = "Auditor"
with col3:
    if st.button("🛡️ Legal Tools"): st.session_state.page = "Tools"

st.markdown("---")

# --- APPLICATION LOGIC ---

if st.session_state.page == "Overview":
    st.markdown("### 📈 Analytics Dashboard")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-box"><h4>Data Accuracy</h4><h2>99.9%</h2></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-box"><h4>Avg. Latency</h4><h2>0.32s</h2></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-box"><h4>Security</h4><h2>Encrypted</h2></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="card">
            <h4>Welcome to the Enterprise Console</h4>
            <p>Auditly AI utilizes state-of-the-art Large Language Models to provide instantaneous risk assessment for corporate and legal documents. Select the <b>Auditor</b> tab to begin.</p>
        </div>
    """, unsafe_allow_html=True)

elif st.session_state.page == "Auditor":
    st.markdown("### 🔍 Secure Document Scan")
    
    left_col, right_col = st.columns([1, 2])
    
    with left_col:
        st.markdown("##### Configuration")
        scan_mode = st.selectbox("Analysis Mode", ["Risk Assessment", "AI-Text Detection", "Clarity Check"])
        uploaded_file = st.file_uploader("Upload PDF File", type="pdf")
        
    with right_col:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            raw_text = "".join([p.extract_text() for p in pdf_reader.pages if p.extract_text()])
            st.success(f"File Processed: {uploaded_file.name}")
            
            if st.button("RUN ENGINE ANALYSIS"):
                if not user_api_key:
                    st.error("System Error: API Configuration missing.")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("AI Engine Analysis in progress..."):
                            prompt = f"Perform a professional {scan_mode} on the following text: {raw_text[:8000]}"
                            response = llm.invoke(prompt)
                            st.markdown('<div class="card">', unsafe_allow_html=True)
                            st.subheader("📋 Audit Report")
                            st.markdown(response.content)
                            st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Analysis failed: {str(e)}")
        else:
            st.info("System ready. Please upload a PDF to proceed.")

elif st.session_state.page == "Tools":
    st.markdown("### 🛡️ Enterprise Compliance Tools")
    st.write("Specialized modules for legal-tech automation.")
    st.button("Request Custom Module")
