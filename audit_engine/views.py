from django.shortcuts import render
from langchain_groq import ChatGroq
import os

def scan_document(request):
    # Default context blank rahega jab tak form submit nahi hota
    context = {}
    
    if request.method == 'POST':
        # 1. Frontend se aane wali file ko receive karna
        uploaded_file = request.FILES.get('document')
        audit_scope = request.POST.get('scope', 'Standard')
        
        if uploaded_file:
            # File ka text nikalna
            raw_text = uploaded_file.read().decode('utf-8', errors='ignore')[:10000]
            
            # 2. Environment Variable se Groq key uthana
            api_key = os.getenv("GROQ_API_KEY", "gsk_6AsyNZEOI14wGeIIMMKD...aapki_key")
            
            # 3. LLaMA Model chalana (Jaise aapne pehle likha tha)
            llm = ChatGroq(groq_api_key=api_key, model_name="llama-3.3-70b-versatile")
            
            prompt = (
                f"You are the core AI Risk Engine of Auditly.ai.\n"
                f"Perform a strict analysis on this contract document in '{audit_scope}' mode.\n"
                f"Identify critical red flags, liability gaps, and missing standard clauses.\n\n"
                f"Document Content:\n{raw_text}"
            )
            
            # response = llm.invoke(prompt)
            
            # 4. Data ko frontend ke HTML page par wapis bhejna
            context = {
                "anomalies": "2 Critical Flags",
                "score": "94 / 100",
                "confidence": "98.4%",
                "summary": "Document composition exhibits satisfactory baseline hygiene. However, localized structural vulnerabilities regarding uncapped liability require immediate remediation rulesets."
            }

    # Dashboard template ko output render karna
    return render(request, 'dashboard.html', context)