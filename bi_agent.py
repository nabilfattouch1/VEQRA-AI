import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

def bi_agent(incident: dict, memory_result: dict) -> dict:
    prompt = f"""
You are the BI Agent of VEQRA AI.
You analyze the financial impact and criticality of enterprise incidents.

INCIDENT:
{json.dumps(incident, ensure_ascii=False, indent=2)}

MEMORY AGENT ANALYSIS:
{json.dumps(memory_result, ensure_ascii=False, indent=2)}

Respond ONLY in JSON:
{{
  "impact_financier_estime": 420000,
  "methode_calcul": "...",
  "sla_minutes_restantes": 47,
  "criticite": "CRITICAL",
  "risque_propagation": "...",
  "kpi_impactes": ["...", "..."],
  "score_urgence": 95
}}
"""
    response = client.chat.completions.create(
        model="qwen3-235b-a22b",
        messages=[{"role": "user", "content": prompt}],
        extra_body={"enable_thinking": False}
    )
    
    content = response.choices[0].message.content
    content = content.replace("```json", "").replace("```", "").strip()
    return json.loads(content)

if __name__ == "__main__":
    with open("incident.json", encoding="utf-8") as f:
        incident = json.load(f)
    
    memory_result = {
        "cas_similaire_trouve": True,
        "reference_cas": "INC-2026-0731",
        "cause_identifiee": "Missing RIB (bank account document)",
        "solution_appliquee": "Data Owner escalation — resolved in 6h",
        "confiance": "HIGH"
    }

    print("📊 BI Agent analyzing...")
    result = bi_agent(incident, memory_result)
    print(json.dumps(result, ensure_ascii=False, indent=2))