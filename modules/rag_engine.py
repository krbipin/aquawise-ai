"""
AquaWise AI - Safe RAG Retrieval Engine
"""

import os
import sys
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DEFAULT_CPCB_KNOWLEDGE = """
CPCB Guidelines:
1. Class A Drinking Water: pH 6.5-8.5, DO > 6mg/L.
2. High Turbidity Remedy: Alum coagulation, bio-sand filter.
3. High Nitrates Remedy: Construct wetland, restrict fertilizers within 50m.
4. High TDS Remedy: Reverse Osmosis (RO) filtration.
"""

class WaterKnowledgeRAG:
    def __init__(self, pdf_path: str = "data/cpcb_water_rules.pdf"):
        self.embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
        self.vector_db = self._load_vector_db(pdf_path)

    def _load_vector_db(self, pdf_path: str):
        # Permanently handle missing or 0-byte empty PDF files safely
        if os.path.exists(pdf_path) and os.path.getsize(pdf_path) > 0:
            try:
                loader = PyPDFLoader(pdf_path)
                documents = loader.load_and_split(self.text_splitter)
                return FAISS.from_documents(documents, self.embeddings)
            except Exception as e:
                print(f"Warning: PDF load failed ({e}). Fallback to default knowledge base.")
        
        # Fallback to default text if PDF is missing, empty, or corrupt
        chunks = self.text_splitter.split_text(DEFAULT_CPCB_KNOWLEDGE)
        return FAISS.from_texts(chunks, self.embeddings)

    def query_context(self, query_str: str, top_k: int = 2) -> str:
        if not self.vector_db:
            return ""
        docs = self.vector_db.similarity_search(query_str, k=top_k)
        return "\n---\n".join([d.page_content for d in docs])