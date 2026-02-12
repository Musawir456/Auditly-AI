import streamlit as st
from PyPDF2 import PdfReader
from langchain_groq import ChatGroq

# 1. Page Configuration
st.set_page_config(page_title="Auditly AI | CEO Dashboard", layout="wide")

st.title("⚖️ Auditly AI: Smart Contract Auditor")
st.write("Founder & CEO: Abdul Musawir")

# 2. Sidebar for Settings
with st.sidebar:
    st.header("Settings")
    user_api_key = st.text_input("Enter Groq API Key:", type="password")
    st.info("Get your API key from the Groq Console.")
with st.sidebar:
    st.title("Settings ⚙️")
    api_key = st.text_input("Enter Groq API Key:", type="password")
    
    st.markdown("---")
    st.markdown("### ❓ Need a Key?")
    st.write("1. [Get it here](https://console.groq.com/keys)")
    st.write("2. Create a new API Key.")
    st.write("3. Paste it in the box above.")
    

# 3. File Uploader
uploaded_file = st.file_uploader("Upload your Contract (PDF)", type="pdf")

if uploaded_file:
    # PDF Extraction Logic
    pdf_reader = PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        content = page.extract_text()
        if content:
            text += content
    
    st.success("File uploaded successfully!")
    st.subheader("Document Preview:")
    st.write(text[:500] + "...") 

    # 4. Audit Button & AI Logic
    if st.button("Start Audit"):
        if not user_api_key:
            st.error("Please enter your Groq API Key in the sidebar!")
        elif not text.strip():
            st.error("The uploaded PDF seems to be empty or unreadable.")
        else:
            try:
                # Latest Model for 2026: Llama 3.3 70B
                llm = ChatGroq(
                    groq_api_key=user_api_key, 
                    model_name="llama-3.3-70b-versatile"
                )
                
                # Context limit management
                contract_segment = text[:8000] 
                
                query = f"""
                You are an Expert Legal Auditor. Analyze the following contract text:
                {contract_segment}
                
                Please provide a detailed report in 3 professional sections:
                1. 🔴 RED FLAGS: (Critical risks or dangerous clauses)
                2. 🟡 WARNINGS: (Items that require careful review)
                3. 🟢 EXECUTIVE SUMMARY: (A brief overview of the document)
                """
                
                with st.spinner("AI is analyzing the document..."):
                    response = llm.invoke(query)
                    st.subheader("🚩 Professional Audit Report:")
                    st.markdown(response.content)
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
