"""
AquaWise AI - Water Quality Evaluator Engine
"""

def evaluate_water_quality(ph: float, turbidity: float, tds: float, nitrates: float, dissolved_oxygen: float = 6.0):
    anomalies = []
    score = 100

    if ph < 6.5:
        anomalies.append(f"Acidic pH ({ph}): Risks pipe leaching and toxicity.")
        score -= 25 if ph < 5.5 else 15
    elif ph > 8.5:
        anomalies.append(f"Alkaline pH ({ph}): Causes mineral scaling.")
        score -= 20 if ph > 9.5 else 10

    if turbidity > 5.0:
        anomalies.append(f"High Turbidity ({turbidity} NTU): Microbial contamination risk.")
        score -= 20

    if tds > 2000.0:
        anomalies.append(f"Severe TDS ({tds} mg/L): Requires RO treatment.")
        score -= 35
    elif tds > 500.0:
        anomalies.append(f"Elevated TDS ({tds} mg/L): Moderate hardness.")
        score -= 15

    if nitrates > 45.0:
        anomalies.append(f"High Nitrates ({nitrates} mg/L): Agricultural pollution risk.")
        score -= 30

    if dissolved_oxygen < 4.0:
        anomalies.append(f"Low Dissolved Oxygen ({dissolved_oxygen} mg/L): Organic load high.")
        score -= 20

    final_score = max(0, score)
    if final_score >= 80:
        status, risk = "SAFE", "Low"
    elif 50 <= final_score < 80:
        status, risk = "MODERATE CONCERN", "Medium"
    else:
        status, risk = "CRITICAL DANGER", "High"

    return {
        "score": final_score,
        "status": status,
        "risk_level": risk,
        "anomalies": anomalies
    }