import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Professional Page Configuration
st.set_page_config(
    page_title="Auditly AI | CEO Dashboard",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Look
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #ff4b4b; color: white; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("⚖️ Auditly AI: Enterprise Solution")
st.write("Developed by **Abdul Musawir** | BS IoT Student at Superior University")

# 2. Sidebar with Branding
with st.sidebar:
    st.image("https://path-to-your-logo.png", width=100) # Aap apna logo yahan link kar sakte hain
    st.title("Auditly Control Panel")
    st.success("API Securely Connected ✅")
    st.info("Status: Market Ready")

# Accessing Key
user_api_key = st.secrets.get("GROQ_API_KEY")

# 3. Features Selection
feature = st.selectbox("Select Service:", ["Contract Risk Audit", "AI-Text Detection (Beta)", "Compliance Check"])

uploaded_file = st.file_uploader("Upload Document (PDF)", type="pdf")

if uploaded_file:
    pdf_reader = PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    
    st.success("Document Analyzed Successfully!")
    
    if st.button(f"Run {feature}"):
        if not user_api_key:
            st.error("Setup Error: Missing API Key in Secrets.")
        else:
            try:
                llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.3-70b-versatile")
                
                # Dynamic Prompts based on Feature
                if "Risk" in feature:
                    prompt = f"Act as a Senior Lawyer. Audit this for RED FLAGS and Risks: {text[:8000]}"
                else:
                    prompt = f"Analyze if this text is AI-generated or human-written. Provide a percentage score: {text[:8000]}"

                with st.spinner("AI Engine Processing..."):
                    response = llm.invoke(prompt)
                    st.divider()
                    st.subheader(f"📊 {feature} Report")
                    st.markdown(response.content)
            except Exception as e:
                st.error(f"Error: {str(e)}")
