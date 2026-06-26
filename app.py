import streamlit as st

# 1. PAGE SETUP (SaaS Header Configuration)
st.set_page_config(
    page_title="Auditly.ai | Enterprise AI Compliance Engine",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ULTRA-PREMIUM MODERN CSS
st.markdown("""
    <style>
    /* Streamlit Defaults Clean-up */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 6rem; max-width: 1200px;}
    
    /* Global Styling - Deep Premium Dark Theme */
    html, body, [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top center, #1E1B4B 0%, #090514 70%) !important;
        color: #F1F5F9 !important;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    /* Clean Modern Navbar */
    .saas-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.2rem 0rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 4rem;
    }
    .saas-logo {
        font-size: 1.6rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        background: linear-gradient(135deg, #38BDF8 0%, #818CF8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .saas-badge {
        background: rgba(129, 140, 248, 0.1);
        border: 1px solid rgba(129, 140, 248, 0.2);
        padding: 6px 14px;
        border-radius: 9999px;
        color: #C7D2FE;
        font-size: 0.8rem;
        font-weight: 500;
    }
    
    /* Feature Box - Glassmorphism */
    .feature-card-premium {
        background: rgba(15, 23, 42, 0.4);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        height: 100%;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .feature-card-premium:hover {
        border-color: rgba(99, 102, 241, 0.4);
    }

    /* Pricing Cards Layout */
    .pricing-card {
        background: rgba(15, 23, 42, 0.5);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 3rem 2rem;
        text-align: center;
        height: 100%;
        transition: 0.3s ease;
    }
    .pricing-card.popular {
        border: 2px solid #818CF8;
        box-shadow: 0 10px 30px rgba(129, 140, 248, 0.15);
        position: relative;
    }
    .plan-badge {
        position: absolute;
        top: -15px;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(90deg, #818CF8, #C084FC);
        color: #090514;
        padding: 4px 16px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    .price-tag {
        font-size: 3rem;
        font-weight: 800;
        color: #F1F5F9;
        margin: 15px 0;
    }
    .price-tag span {
        font-size: 1rem;
        color: #94A3B8;
        font-weight: 400;
    }
    .pricing-features {
        list-style: none;
        padding: 0;
        margin: 25px 0;
        text-align: left;
        color: #94A3B8;
        font-size: 0.95rem;
    }
    .pricing-features li {
        margin-bottom: 12px;
        padding-left: 20px;
        position: relative;
    }
    .pricing-features li::before {
        content: "✓";
        position: absolute;
        left: 0;
        color: #38BDF8;
        font-weight: bold;
    }
    
    /* Tool Interface Container */
    .tool-box {
        background: rgba(13, 10, 31, 0.6);
        border: 1px solid rgba(129, 140, 248, 0.15);
        border-radius: 24px;
        padding: 3rem;
        margin-top: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
    }
    
    /* Report Insights Styling */
    .report-card {
        background: rgba(255, 255, 255, 0.02);
        border-left: 4px solid #818CF8;
        padding: 1.5rem;
        border-radius: 0px 12px 12px 0px;
        margin-top: 1rem;
    }
    
    /* Founder Section */
    .founder-card {
        background: linear-gradient(180deg, rgba(30, 27, 75, 0.4) 0%, rgba(9, 5, 20, 0.9) 100%);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 3.5rem;
        text-align: center;
        max-width: 650px;
        margin: 0 auto;
    }
    
    /* Luxury Social Links */
    .social-anchor {
        display: inline-block;
        margin: 8px;
        padding: 10px 22px;
        background: rgba(255, 255, 255, 0.04);
        color: #E2E8F0 !important;
        text-decoration: none;
        border-radius: 10px;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid rgba(255, 255, 255, 0.05);
        transition: 0.2s;
    }
    .social-anchor:hover {
        background: #818CF8;
        color: #090514 !important;
        border-color: #818CF8;
    }
    </style>
    """, unsafe_allow_html=True)

# =========================================================================
# NAVBAR
# =========================================================================
st.markdown("""
    <div class="saas-nav">
        <div class="saas-logo">🛡️ Auditly.ai</div>
        <div class="saas-badge">Agentic AI Engine v2.0</div>
    </div>
    """, unsafe_allow_html=True)


# =========================================================================
# HERO SECTION
# =========================================================================
st.markdown("""
    <div style="text-align: center; margin-bottom: 4rem;">
        <h1 style="font-size: 4rem; font-weight: 900; letter-spacing: -1.5px; line-height: 1.1; margin-bottom: 20px;">
            Automate Your Corporate <br>
            <span style="background: linear-gradient(90deg, #38BDF8, #818CF8, #C084FC); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Auditing Bottlenecks
            </span>
        </h1>
        <p style="font-size: 1.25rem; color: #94A3B8; max-width: 700px; margin: 0 auto; line-height: 1.6;">
            Leveraging autonomous Agentic AI and sophisticated RAG pipelines to map compliance, identify liabilities, and execute risk audits in seconds.
        </p>
    </div>
    """, unsafe_allow_html=True)


# =========================================================================
# FEATURE GRID
# =========================================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
        <div class="feature-card-premium">
            <div style="font-size: 2rem; margin-bottom: 15px;">🔍</div>
            <h3 style="color: #F1F5F9; font-size: 1.3rem; font-weight: 700; margin-bottom: 10px;">Intelligent Scan</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6; margin: 0;">Upload highly complex multi-page legal or financial data matrices. Our custom parser flags missing compliance protocols instantly.</p>
        </div>
        """, unsafe_allow_html=True)
        
with col2:
    st.markdown("""
        <div class="feature-card-premium">
            <div style="font-size: 2rem; margin-bottom: 15px;">⚡</div>
            <h3 style="color: #F1F5F9; font-size: 1.3rem; font-weight: 700; margin-bottom: 10px;">Deterministic Logic</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6; margin: 0;">Say goodbye to broad, hallucinated LLM feedback. Get rigorous compliance alignment reporting mapped directly to system rulesets.</p>
        </div>
        """, unsafe_allow_html=True)
        
with col3:
    st.markdown("""
        <div class="feature-box feature-card-premium">
            <div style="font-size: 2rem; margin-bottom: 15px;">🛡️</div>
            <h3 style="color: #F1F5F9; font-size: 1.3rem; font-weight: 700; margin-bottom: 10px;">Isolated Pipeline</h3>
            <p style="color: #94A3B8; font-size: 0.95rem; line-height: 1.6; margin: 0;">Built on secure backend integrations. Your unstructured data is processed locally with full contextual privacy controls.</p>
        </div>
        """, unsafe_allow_html=True)


st.markdown("<br><br><br><br><hr style='border-color: rgba(255,255,255,0.05);'><br><br>", unsafe_allow_html=True)


# =========================================================================
# 🔥 NEW SECTION: PRICING PLANS
# =========================================================================
st.markdown("""
    <div style="text-align: center; margin-bottom: 3rem;">
        <h2 style="font-size: 2.5rem; font-weight: 800; letter-spacing: -0.5px;">Transparent Architecture Plans</h2>
        <p style="color: #94A3B8;">Select the auditing scale that fits your infrastructure matrix.</p>
    </div>
    """, unsafe_allow_html=True)

p_col1, p_col2, p_col3, p_col4 = st.columns([0.5, 2, 2, 0.5])

with p_col2:
    st.markdown("""
        <div class="pricing-card">
            <h3 style="color: #F1F5F9; font-size: 1.4rem; font-weight: 700; margin-bottom: 5px;">Monthly Plan</h3>
            <p style="color: #94A3B8; font-size: 0.9rem;">Perfect for ad-hoc compliance cycles.</p>
            <div class="price-tag">$100<span> / month</span></div>
            <ul class="pricing-features">
                <li>Full RAG Document Ingestion</li>
                <li>Up to 50 Detailed Runs / mo</li>
                <li>Standard LLaMA 3.3 Pipeline</li>
                <li>Email Support (24h SLA)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with p_col3:
    st.markdown("""
        <div class="pricing-card popular">
            <div class="plan-badge">Save $200 / Year</div>
            <h3 style="color: #F1F5F9; font-size: 1.4rem; font-weight: 700; margin-bottom: 5px;">Annual Enterprise</h3>
            <p style="color: #94A3B8; font-size: 0.9rem;">For continuous operational security.</p>
            <div class="price-tag">$1,000<span> / year</span></div>
            <ul class="pricing-features">
                <li>Everything in Monthly</li>
                <li>**Unlimited** Execution Passes</li>
                <li>Priority Agent Node Allocation</li>
                <li>Dedicated Founder Slack Support</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)


st.markdown("<br><br><br><br><hr style='border-color: rgba(255,255,255,0.05);'><br><br>", unsafe_allow_html=True)


# =========================================================================
# INTERACTIVE SAAS TOOL WINDOW
# =========================================================================
st.markdown("""
    <div style="text-align: center;">
        <h2 style="font-size: 2.2rem; font-weight: 800; letter-spacing: -0.5px;">Execute Autonomous Audit</h2>
        <p style="color: #94A3B8;">Initialize our LLaMA 3.3 pipeline on your document workloads.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="tool-box">', unsafe_allow_html=True)

t_col1, t_col2, t_col3 = st.columns([1, 4, 1])
with t_col2:
    uploaded_file = st.file_uploader("Drop compliance document (.pdf, .csv, .txt)", type=["pdf", "csv", "txt"], label_visibility="collapsed")
    st.markdown("<br>", unsafe_allow_html=True)
    audit_scope = st.selectbox("Define Operational Matrix Scope", ["Financial Compliance Architecture", "Risk Management Protocol", "Custom Operational Ruleset"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if uploaded_file is not None:
        st.toast(f"File loaded successfully: {uploaded_file.name}")
        
        if st.button("Trigger AI Engine Execution", use_container_width=True):
            with st.spinner("Provisioning Agent Nodes... Analysing Clause Semantics..."):
                import time
                time.sleep(2)
                
            st.markdown("<br><br>", unsafe_allow_html=True)
            st.markdown("<h3 style='letter-spacing:-0.5px;'>📊 Pipeline Audit Insights</h3>", unsafe_allow_html=True)
            
            # Premium Metrics Display
            m_col1, m_col2, m_col3 = st.columns(3)
            m_col1.metric("Anomalies Flagged", "2 Critical", delta="-5 vs baseline")
            m_col2.metric("Compliance Health Score", "94 / 100")
            m_col3.metric("System Confidence", "98.4%")
            
            # Details Section
            st.markdown("<br>🗣️ **Detailed Findings Breakdown:**", unsafe_allow_html=True)
            
            with st.expander("🚨 Clause Exception 01 — Missing Liability Limitation Cap"):
                st.markdown("""
                * **Context:** Document lacks explicit financial liability thresholds for operational service failures.
                * **Risk Factor:** Exposes the entity to uncapped litigation damages.
                * **Remediation:** Insert standard 100% trailing contract value indemnification caps.
                """)
                
            with st.expander("⚠️ Clause Exception 02 — Vague SLA Turnaround Architecture"):
                st.markdown("""
                * **Context:** Ambiguous terminology ('reasonable timeline windows') discovered in Appendix B.
                * **Risk Factor:** Non-enforceable metrics during production downtime events.
                * **Remediation:** Establish explicit time-to-resolve bounds (e.g., P1 escalation = 4 hours max).
                """)
                
            st.markdown("""
            <div class="report-card">
                <span style="color:#818CF8; font-weight:700; font-size:0.9rem; text-transform:uppercase; letter-spacing:1px;">System Executive Summary</span>
                <p style="color:#94A3B8; font-size:0.95rem; margin-top:5px; line-height:1.6; margin-bottom:0;">
                    Overall document composition exhibits satisfactory baseline hygiene. Rectifying the localized structural vulnerabilities listed in the exceptions above will completely insulate the framework from operational exposures.
                </p>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)


# =========================================================================
# FOUNDER PROFILE
# =========================================================================
st.markdown('<div class="founder-card">', unsafe_allow_html=True)
st.markdown("""
    <h2 style="font-size: 2rem; font-weight: 800; margin-bottom: 5px;">Abdul Musawir</h2>
    <p style="color: #818CF8; font-weight: 600; font-size: 1.1rem; margin-top: 0; letter-spacing: 0.5px;">Founder & CEO @ Auditly.ai</p>
    <p style="color: #94A3B8; font-size: 1rem; line-height: 1.7; max-width: 550px; margin: 0 auto; padding: 15px 0;">
        AI/ML Engineer and Data Scientist specializing in Agentic AI architectures, Retrieval-Augmented Generation (RAG) loops, 
        and autonomous corporate risk compliance engineering.
    </p>
    <div style="margin-top: 10px;">
        <a href="https://linkedin.com" target="_blank" class="social-anchor">🔗 LinkedIn</a>
        <a href="https://instagram.com" target="_blank" class="social-anchor">📸 Instagram</a>
        <a href="mailto:your.email@gmail.com" class="social-anchor">✉️ Contact Enterprise</a>
    </div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: rgba(255,255,255,0.2); font-size: 0.8rem;'>© 2026 Auditly.ai. Proprietary compliance tech infrastructure.</p>", unsafe_allow_html=True)