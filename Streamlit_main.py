import streamlit as st
from PyPDF2 import PdfReader

# Page title aur startup branding
st.set_page_config(page_title="Auditly AI | CEO Dashboard", layout="wide")

st.title("⚖️ Auditly AI: Smart Contract Auditor")
st.write("Founder & CEO: Abdul Musawir")

# Sidebar for API Key
with st.sidebar:
    st.header("Settings")
    user_api_key = st.text_input("Groq API Key dalein:", type="password")
    st.info("Ye key aapko Groq Console se milegi.")

# File Uploader
uploaded_file = st.file_uploader("Apna Contract (PDF) yahan upload karein", type="pdf")

if uploaded_file:
    # PDF se text nikalne ka logic
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    st.success("File upload ho gayi!")
    st.subheader("Document Preview:")
    st.write(text[:500] + "...") # Pehle 500 alfaz ka preview
    from langchain_groq import ChatGroq

if st.button("Audit Shuru Karein"):
    if not user_api_key:
        st.error("Pehle sidebar mein API Key dalein!")
    else:
        # AI Model setup
        llm = ChatGroq(groq_api_key=user_api_key, model_name="llama-3.1-70b-versatile")
        
        # Professional Lawyer Prompt
        query = f"Aap ek expert lawyer hain. Is contract mein 3 main 'Red Flags' (khatre) dhoondo: {text[:3000]}"
        
        with st.spinner("AI Analysis kar raha hai..."):
            response = llm.invoke(query)
            st.subheader("🚩 Audit Report (Red Flags):")
            st.markdown(response.content)