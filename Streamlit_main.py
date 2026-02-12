import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Page Configuration
st.set_page_config(page_title="Auditly AI | CEO Dashboard", layout="wide")

st.title("⚖️ Auditly AI: Smart Contract Auditor")
st.write("Founder & CEO: Abdul Musawir")

# 2. Sidebar - Secure & Professional
with st.sidebar:
    st.title("Auditly AI ⚙️")
    st.success("System Status: Active ✅")
    st.markdown("---")
    st.write("This startup uses Llama 3.3 to analyze legal risks instantly.")

# 3. Securely Accessing the API Key
# We use .get() to prevent the app from crashing with a KeyError
user_api_key = st.secrets.get("GROQ_API_KEY")

# 4. File Uploader
uploaded_file = st.file_uploader("Upload your Contract (PDF)", type="pdf")

if uploaded_file:
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    
    st.success("File uploaded successfully!")
    st.subheader("Document Preview:")
    st.write(text[:500] + "...") 

    if st.button("Start Audit"):
        # Check if the secret key actually exists
        if not user_api_key:
            st.error("Error: GROQ_API_KEY not found in Streamlit Secrets. Please add it in the app settings.")
        elif not text.strip():
            st.error("The uploaded PDF seems to be empty.")
        else:
            try:
                # Using the latest Llama 3.3 model as planned
                llm = ChatGroq(
                    groq_api_key=user_api_key, 
                    model_name="llama-3.3-70b-versatile"
                )
                
                contract_segment = text[:8000] 
                query = f"Analyze this contract and provide: 1. RED FLAGS 2. WARNINGS 3. EXECUTIVE SUMMARY. Text: {contract_segment}"
                
                with st.spinner("AI is analyzing the document..."):
                    response = llm.invoke(query)
                    st.subheader("🚩 Professional Audit Report:")
                    st.markdown(response.content)
            except Exception as e:
                st.error(f"System Error: {str(e)}")
