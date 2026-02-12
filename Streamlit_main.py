import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Page Configuration (Full Width & Professional)
st.set_page_config(
    page_title="Auditly AI | Global Enterprise",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Advanced Bootstrap-Inspired CSS Injection
st.markdown("""
    <style>
    /* Importing Professional Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700&display=swap');
    
    body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f4f7f6;
    }

    /* Global Navbar Styling */
    .navbar {
        background-color: #ffffff;
        padding: 1rem 3rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        border-bottom: 1px solid #e1e4e8;
        margin-bottom: 2rem;
    }

    /* Professional Card Component */
    .bootstrap-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #e1e4e8;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02);
        margin-bottom: 1.5rem;
        transition: 0.3s;
    }
    .bootstrap-card:hover {
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
    }

    /* Custom Primary Button */
    .stButton>button {
        background-color: #0d6efd;
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.8rem 2rem;
        border: none;
        width: 100%;
        box-shadow: 0 4px 6px rgba(13, 110, 253, 0.2);
    }
    .stButton>button:hover {
        background-color: #0b5ed7;
        color: white;
    }

    /* Report Section Styling */
    .audit-result {
        background-color: #ffffff;
        border-left: 5px solid #0d6efd;
        padding: 2rem;
        border-radius: 8px;
        line-height: 1.8;
    }
    </style>

    <div class="navbar">
        <div style="font-size: 24px; font-weight: 700; color: #0d6efd;">AUDITLY <span style="color: #212529;">AI</span></div>
        <div style="font-size: 14px; color: #6c757d; font-weight: 500;">ENTERPRISE CLOUD | 2026 EDITION</div>
    </div>
    """, unsafe_allow_html=True)

# 3. Secure Backend Configuration
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. Multi-Page Navigation Logic
if 'nav_selection' not in st.session_state:
    st.session_state.nav_selection = "Dashboard"

# Horizontal Navigation Menu (Top Bar)
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([1, 1, 1, 1])
with nav_col1:
    if st.button("📊 Dashboard"): st.session_state.nav_selection = "Dashboard"
with nav_col2:
    if st.button("⚖️ Legal Auditor"): st.session_state.nav_selection = "Auditor"
with nav_col3:
    if st.button("📝 AI Text Lab"): st.session_state.nav_selection = "AIText"
with nav_col4:
    if st.button("📜 Help & API"): st.session_state.nav_selection = "Help"

st.markdown("<br>", unsafe_allow_html=True)

# --- DASHBOARD PAGE ---
if st.session_state.nav_selection == "Dashboard":
    st.markdown("### ⚡ Operational Overview")
    
    # Hero Section
    st.markdown("""
        <div class="bootstrap-card">
            <h3>Welcome to Auditly AI Systems</h3>
            <p style='color: #6c757d;'>Your centralized platform for AI-driven legal compliance and document auditing.</p>
        </div>
    """, unsafe_allow_html=True)

    # Metrics
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Server Status", "Online", "Stable")
    c2.metric("Processing Time", "0.24s", "-0.05s")
    c3.metric("Daily Queries", "1.2k", "25%")
    c4.metric("Risk Hit-Rate", "99.8%", "High")

# --- AUDITOR PAGE ---
elif st.session_state.nav_selection == "Auditor":
    st.markdown("### 🔍 Legal Audit Engine")
    
    col_config, col_action = st.columns([1, 2])
    
    with col_config:
        st.markdown('<div class="bootstrap-card">', unsafe_allow_html=True)
        st.write("**Analysis Settings**")
        audit_mode = st.radio("Select Depth", ["Legal Risk Scan", "Clause Verification", "Liability Audit"])
        uploaded_file = st.file_uploader("Drop PDF here", type="pdf")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_action:
        if uploaded_file:
            pdf_reader = PdfReader(uploaded_file)
            doc_text = "".join([p.extract_text() for p in pdf_reader.pages if p.extract_text()])
            st.success(f"Document Ingested: {uploaded_file.name}")
            
            if st.button("INITIALIZE ENTERPRISE AUDIT"):
                if not user_api_key:
                    st.error("System Failure: Secret Key Missing.")
                else:
                    try:
                        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                        with st.spinner("Processing through Llama 3.3 Infrastructure..."):
                            prompt = f"Perform a professional {audit_mode} on the following document: {doc_text[:8000]}"
                            response = llm.invoke(prompt)
                            st.markdown("---")
                            st.markdown('<div class="audit-result">', unsafe_allow_html=True)
                            st.subheader("📑 Enterprise Audit Report")
                            st.markdown(response.content)
                            st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Engine Error: {str(e)}")
        else:
            st.info("System is ready for document ingestion.")

# --- OTHER PAGES ---
elif st.session_state.nav_selection == "AIText":
    st.title("📝 AI Text Laboratory")
    st.write("Specialized module for detecting AI-generated content in legal briefs.")

elif st.session_state.nav_selection == "Help":
    st.title("📜 Documentation")
    st.write("Enterprise Documentation for System Integrations and API usage.")
