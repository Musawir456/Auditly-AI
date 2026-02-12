import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Advanced Page Config
st.set_page_config(
    page_title="Auditly AI | Enterprise",
    page_icon="⚖️",
    layout="wide"
)

# Custom Styling for a Modern Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stSidebar { background-color: #1a1c24; }
    .report-box { 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 5px solid #ff4b4b;
        background-color: #262730;
    }
    h1 { color: #ff4b4b; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. Sidebar Navigation
with st.sidebar:
    st.title("🛡️ Auditly AI")
    st.write("Founder: Abdul Musawir")
    page = st.radio("Go to Page:", ["🏠 Dashboard", "🔍 Smart Auditor", "🛡️ Compliance Center"])
    st.divider()
    st.success("API Status: Connected ✅")

# Get API Key
user_api_key = st.secrets.get("GROQ_API_KEY")

# --- PAGE 1: DASHBOARD ---
if page == "🏠 Dashboard":
    st.title("🚀 Founder's Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Status", "Live")
    col2.metric("Model", "Llama 3.3")
    col3.metric("Security", "Secured")
    
    st.markdown("---")
    st.subheader("Welcome to Auditly AI")
    st.write("This platform is designed to automate the manual struggle of legal auditing. Use the sidebar to navigate to the Auditor.")

# --- PAGE 2: SMART AUDITOR ---
elif page == "🔍 Smart Auditor":
    st.title("🔍 Advanced Contract Auditor")
    st.write("Upload your document to detect red flags and risks.")
    
    # Feature Selection with Colors
    audit_type = st.pills("Select Audit Type:", ["Full Risk Audit", "AI-Text Detection", "Summary Only"])
    
    uploaded_file = st.file_uploader("Upload PDF Contract", type="pdf")
    
    if uploaded_file:
        pdf_reader = PdfReader(uploaded_file)
        text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        st.info("Document loaded successfully.")

        if st.button("Generate Professional Report"):
            if not user_api_key:
                st.error("Missing API Key.")
            else:
                try:
                    llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                    
                    # Logic based on selection
                    prompt = f"Expert Legal Auditor. Analyze this and provide Red Flags and Warnings: {text[:8000]}"
                    if audit_type == "AI-Text Detection":
                        prompt = f"Analyze if this text is AI-written: {text[:8000]}"
                    
                    with st.spinner("AI Engine is analyzing..."):
                        response = llm.invoke(prompt)
                        st.markdown(f'<div class="report-box">', unsafe_allow_html=True)
                        st.subheader("📑 Official Audit Report")
                        st.markdown(response.content)
                        st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

# --- PAGE 3: COMPLIANCE ---
elif page == "🛡️ Compliance Center":
    st.title("🛡️ Compliance & Standards")
    st.write("This section is for enterprise-level compliance checks (Coming Soon).")
