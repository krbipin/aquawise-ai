"""
AquaWise AI - IBM Granite Advisor Model Connector
"""

import os
import requests

class IBMGraniteAdvisor:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("HUGGINGFACEHUB_API_TOKEN")
        self.model_url = "https://api-inference.huggingface.co/models/ibm-granite/granite-3.0-8b-instruct"

    def generate_advisory(self, user_role: str, eval_results: dict, water_params: dict, context_str: str) -> str:
        def get_fallback():
            anomalies = "\n".join([f"- {a}" for a in eval_results.get('anomalies', [])]) or "- None."
            return (
                f"### Safety Status: {eval_results.get('status')}\n"
                f"**Role:** {user_role}\n\n"
                f"**Detected Issues:**\n{anomalies}\n\n"
                "**Action Steps:**\n"
                "1. Perform secondary chemical testing.\n"
                "2. Apply standard bio-sand or RO filtration based on TDS/Turbidity.\n"
                "3. Contact local municipal ward officers."
            )

        if not self.api_key:
            return get_fallback()

        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        prompt = (
            f"Role: {user_role}\nMetrics: {water_params}\nAnomalies: {eval_results.get('anomalies')}\n"
            f"Policy Context: {context_str}\nProvide 3 actionable bio-remediation steps."
        )

        try:
            res = requests.post(self.model_url, headers=headers, json={"inputs": prompt}, timeout=10)
            if res.status_code == 200:
                out = res.json()
                return out[0]["generated_text"] if isinstance(out, list) else out.get("generated_text", get_fallback())
            return get_fallback()
        except Exception:
            return get_fallback()