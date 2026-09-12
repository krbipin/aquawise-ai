import streamlit as st
import os
import sys

# Safe Import Engine for FPDF
try:
    from fpdf import FPDF
except ModuleNotFoundError:
    os.system(f"{sys.executable} -m pip install fpdf2")
    from fpdf import FPDF

from modules.evaluator import evaluate_water_quality
from modules.rag_engine import WaterKnowledgeRAG
from modules.llm_advisor import IBMGraniteAdvisor

st.set_page_config(page_title="AquaWise AI", page_icon="💧", layout="wide")
st.title("💧 AquaWise AI Dashboard")

@st.cache_resource
def init_rag():
    return WaterKnowledgeRAG()

rag_engine = init_rag()

st.sidebar.header("Sample Parameters")
user_role = st.sidebar.selectbox("User Role:", ["Domestic Resident", "Smallholder Farmer", "Municipal Ward Officer"])
ph = st.sidebar.slider("pH Level", 0.0, 14.0, 7.2)
turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 20.0, 3.5)
tds = st.sidebar.number_input("TDS (mg/L)", 0.0, 3000.0, 420.0)
nitrates = st.sidebar.number_input("Nitrates (mg/L)", 0.0, 150.0, 12.0)
dissolved_oxygen = st.sidebar.slider("Dissolved Oxygen (mg/L)", 0.0, 14.0, 6.5)

def build_pdf(eval_data, output_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", 'B', 14)
    pdf.cell(0, 10, "AquaWise AI - Water Advisory Report", ln=True, align='C')
    pdf.ln(5)
    
    pdf.set_font("Helvetica", 'B', 10)
    pdf.cell(0, 6, f"Status: {eval_data['status']} | Score: {eval_data['score']}/100 | Risk: {eval_data['risk_level']}", ln=True)
    pdf.ln(5)
    
    pdf.set_font("Helvetica", size=10)
    # Non-ASCII / Latin characters ko safely sanitize karein
    safe_text = str(output_text).encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(0, 5, safe_text)
    
    # FPDF2 / FPDF return type handling (Bytes/Bytearray to Bytes)
    pdf_output = pdf.output()
    if isinstance(pdf_output, (bytes, bytearray)):
        return bytes(pdf_output)
    return str(pdf_output).encode('latin-1')

if st.button("Analyze & Generate Advisory"):
    params = {"ph": ph, "turbidity": turbidity, "tds": tds, "nitrates": nitrates, "dissolved_oxygen": dissolved_oxygen}
    eval_res = evaluate_water_quality(ph, turbidity, tds, nitrates, dissolved_oxygen)

    col1, col2, col3 = st.columns(3)
    col1.metric("Status", eval_res["status"])
    col2.metric("Score", f"{eval_res['score']}/100")
    col3.metric("Risk Level", eval_res["risk_level"])

    context = rag_engine.query_context(f"Remediation for pH {ph}, turbidity {turbidity}")
    advisor = IBMGraniteAdvisor()
    advisory = advisor.generate_advisory(user_role, eval_res, params, context)

    st.markdown("### Actionable Advisory")
    st.markdown(advisory)

    pdf_bytes = build_pdf(eval_res, advisory)
    st.download_button("📄 Download PDF Report", data=pdf_bytes, file_name="AquaWise_Report.pdf", mime="application/pdf")