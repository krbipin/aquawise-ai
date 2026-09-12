# 💧 AquaWise AI: Smart Water Assessment & Community Advisory System

> **1M1B – IBM SkillsBuild AI + Sustainability Virtual Internship (July–September 2026)**  
> *In Collaboration with IBM SkillsBuild & AICTE*

---

## 📌 Project Overview
**AquaWise AI** is an intelligent, low-cost water quality evaluation and contextual advisory system built to democratize clean water access. In many rural, peri-urban, and agricultural communities, local residents and smallholder farmers lack simple ways to interpret physical and chemical water quality parameters (such as pH, Turbidity, TDS, Nitrates, and Dissolved Oxygen). 

AquaWise AI combines deterministic chemical risk assessment with **IBM Granite LLM** and **Retrieval-Augmented Generation (RAG)** to provide immediate, persona-specific remediation advice aligned with official water safety standards.

---

## 🎯 Sustainable Development Goals (SDG) Alignment
* **Primary SDG:** **SDG 6 — Clean Water and Sanitation**
  * *Target 6.3:* Improve water quality by reducing pollution and hazardous chemical leaching.
  * *Target 6.b:* Support community participation in local water management.
* **Secondary SDGs:**
  * **SDG 3:** Good Health and Well-Being (Preventing waterborne contamination).
  * **SDG 11:** Sustainable Cities and Communities (Building local environmental resilience).

---

## 🚀 Key Features
* **Rule-Based Diagnostic Engine:** Instantly evaluates 5 key water parameters against WHO & CPCB baseline safety thresholds to generate a Water Quality Index (WQI) score (0–100) and risk classification.
* **Contextual Policy Retrieval (RAG):** Uses **FAISS** and **Hugging Face Embeddings** to query official CPCB water guidelines and bio-remediation protocols.
* **Persona-Based AI Advisories:** Uses **IBM Granite 3.0** to deliver tailored, plain-language action plans for:
  * 🏡 **Domestic Residents** (Drinking, cooking & household utility advice)
  * 🌾 **Smallholder Farmers** (Crop irrigation & soil health guidance)
  * 🏛️ **Municipal Field Officers** (Community management & testing protocols)
* **Streamlit Web Dashboard:** Interactive, lightweight, and deployable on free cloud tiers.

---

## 🏗️ System Architecture

```text
[ User Parameters Input (Streamlit UI) ]
                   │
                   ├──► 1. Rule Evaluator (modules/evaluator.py)
                   │       └─► Computes WQI Score & Contamination Anomalies
                   │
                   ├──► 2. RAG Engine (modules/rag_engine.py)
                   │       └─► Retrieves CPCB/WHO Rules via FAISS Vector Store
                   │
                   └──► 3. IBM Granite LLM (modules/llm_advisor.py)
                           └─► Generates Contextual Actionable Advisory
```
---

## 🛠️ Technology Stack
* **Frontend:** Streamlit (Python)
* **LLM Engine:** IBM Granite 3.0 (via Hugging Face Inference API / Local Fallback Logic)
* **Vector Store & Embeddings:** FAISS + `sentence-transformers/all-MiniLM-L6-v2`
* **Data & Logic:** Python 3.10+, Pandas, LangChain


  ---


  ## 📁 Repository Folder Structure

* **`.streamlit/`**: Streamlit configuration files (e.g., `secrets.toml` for storing API keys).
* **`modules/`**: Core backend logic and processing files:
  * **`evaluator.py`**: Rule-based logic for Water Quality Index (WQI) score calculation.
  * **`rag_engine.py`**: FAISS vector store and CPCB water policy context retrieval module.
  * **`llm_advisor.py`**: Prompt engine and IBM Granite LLM integration handler.
* **`app.py`**: Main application script running the Streamlit web dashboard.
* **`requirements.txt`**: List of Python library dependencies for project setup and cloud deployment.
* **`README.md`**: Project documentation, setup guide, and evaluation overview.


----
## ⚖️ Responsible AI Considerations

* **Fairness & Accessibility:** Designed to translate complex physical and chemical water quality data into plain, accessible language without technical jargon, making it usable for non-technical community members and rural farmers.
* **Transparency & Explainability:** Employs a clear hybrid approach:
  * Deterministic rule-based evaluation to provide transparent, standardized safety scores.
  * Retrieved CPCB policy fragments shown explicitly to users alongside AI-generated advisories.
* **Ethics & Safety First:** Includes explicit disclaimers emphasizing that the system provides decision-support guidance and does not replace certified laboratory testing or official government health notices.
* **Privacy & Data Protection:** Designed with privacy by default—processes water sample metrics statelessly without collecting or storing personally identifiable information (PII) or user location data.
* **Human Oversight (Human-in-the-Loop):** Empowers municipal field officers and community leaders with AI insights while keeping critical water management decisions strictly under human authority.
* **AI Limitations Disclosed:** Clearly communicates system boundary limits, including reliance on user-input accuracy and potential generic output in borderline scenarios.


---
## 📄 License

Developed for educational, research, and community impact purposes as part of the **1M1B – IBM SkillsBuild AI + Sustainability Virtual Internship (July–September 2026)** in collaboration with AICTE.
