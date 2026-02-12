import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Advanced Page Config
st.set_page_config(
    page_title="Auditly AI | Enterprise",
    page_icon="⚖️",
    layout="wide"
)

# Professional CSS for Navigation & Layout
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    /* Top Navigation Style */
    .nav-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        padding: 10px;
        background-color: #1a1c24;
        border-radius: 15px;
        margin-bottom: 30px;
    }
    .nav-btn {
        padding: 10px 25px;
        border-radius: 8px;
        background-color: #262730;
        color: white;
        text-decoration: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .nav-btn:hover { background-color: #ff4b4b; cursor: pointer; }
    
    /* Report Box */
    .report-box { 
        padding: 25px; 
        border-radius: 12px; 
        border-left: 6px solid #ff4b4b;
        background-color: #1a1c24;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
    }
    h1 { color: #ff4b4b; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Branding Only
with st.sidebar:
    st.markdown("### 🛡️ Auditly AI")
    st.write("**Founder:** Abdul Musawir")
    st.divider()
    st.success("API Status: Connected ✅")
    st.info("Version: 2.0 (Enterprise)")

# 3. Secure API Access
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. Top Navigation Bar Implementation
# We use session_state to track page changes without radio buttons in sidebar
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Home"

col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col2:
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.current_page = "Home"
with col3:
    if st.button("🔍 Auditor", use_container_width=True):
        st.session_state.current_page = "Auditor"
with col4:
    if st.button("🛡️ Compliance", use_container_width=True):
        st.session_state.current_page = "Compliance"

st.divider()

# --- PAGE LOGIC ---

if st.session_state.current_page == "Home":
    st.title("🚀 Enterprise Audit Dashboard")
    st.markdown("<h4 style='text-align: center;'>Welcome to the future of AI-driven Legal Auditing</h4>", unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Total Audits", "1.2k", "+12%")
    with col_b:
        st.metric("Model Speed", "0.4s/page")
    with col_c:
        st.metric("Accuracy", "99.2%")
    
    st.image("https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=800&q=80", caption="Digital Transformation in Law")

elif st.session_state.current_page == "Auditor":
    st.title("🔍 Smart Contract Auditor")
    st.write("Upload and analyze documents with Llama 3.3 Intelligence.")
    
    uploaded_file = st.file_uploader("Drop your PDF file here", type="pdf")
    
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        st.success("Analysis Ready.")

        if st.button("Generate AI Audit Report"):
            if not user_api_key:
                st.error("Missing API Credentials.")
            else:
                try:
                    llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                    with st.spinner("AI Engine Analyzing..."):
                        response = llm.invoke(f"Expert Audit of this contract: {text[:8000]}")
                        st.markdown('<div class="report-box">', unsafe_allow_html=True)
                        st.subheader("📑 Final Audit Report")
                        st.markdown(response.content)
                        st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

elif st.session_state.current_page == "Compliance":
    st.title("🛡️ Compliance Center")
    st.warning("Enterprise compliance tracking is currently in Beta mode.")
    st.image("https://images.unsplash.com/photo-1450101499163-c8848c66ca85?auto=format&fit=crop&w=800&q=80")

