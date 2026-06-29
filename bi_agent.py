import json
from openai import OpenAI

client = OpenAI(
    api_key="sk-ws-H.PYYLYD.o2lX.MEYCIQDz5wNXaeLYt2gSgD6TBIvPzcMlBWc7BHkppiSSzS0ymwIhANBD04QPHr3GczCEqyYQlaIQSBT-Bs_yRA5v1O6bo1S1",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

def bi_agent(incident: dict, memory_result: dict) -> dict:
    prompt = f"""
Tu es le BI Agent de VEQRA AI.
Tu analyses l'impact financier et la criticité des incidents enterprise.

INCIDENT :
{json.dumps(incident, ensure_ascii=False, indent=2)}

ANALYSE MEMORY AGENT :
{json.dumps(memory_result, ensure_ascii=False, indent=2)}

Réponds UNIQUEMENT en JSON :
{{
  "impact_financier_estime": 420000,
  "methode_calcul": "...",
  "sla_minutes_restantes": 47,
  "criticite": "CRITIQUE",
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
        "cause_identifiee": "RIB bancaire manquant",
        "solution_appliquee": "Escalade Data Owner — résolu en 6h",
        "confiance": "HAUTE"
    }
    
    print("📊 BI Agent en cours d'analyse...")
    result = bi_agent(incident, memory_result)
    print(json.dumps(result, ensure_ascii=False, indent=2))