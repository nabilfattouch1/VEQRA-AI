import json
from openai import OpenAI

client = OpenAI(
    api_key="sk-ws-H.PYYLYD.o2lX.MEYCIQDz5wNXaeLYt2gSgD6TBIvPzcMlBWc7BHkppiSSzS0ymwIhANBD04QPHr3GczCEqyYQlaIQSBT-Bs_yRA5v1O6bo1S1",
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

def action_agent(incident: dict, memory_result: dict, bi_result: dict) -> dict:
    prompt = f"""
Tu es l'Action Agent de VEQRA AI.
Tu décides les actions correctives immédiates pour résoudre l'incident.

INCIDENT :
{json.dumps(incident, ensure_ascii=False, indent=2)}

ANALYSE MEMORY :
{json.dumps(memory_result, ensure_ascii=False, indent=2)}

ANALYSE BI :
{json.dumps(bi_result, ensure_ascii=False, indent=2)}

Réponds UNIQUEMENT en JSON :
{{
  "priorite": "P1",
  "actions": [
    {{
      "type": "TEAMS_TASK",
      "destinataire": "...",
      "message": "...",
      "deadline": "..."
    }},
    {{
      "type": "EMAIL",
      "destinataire": "...",
      "sujet": "...",
      "corps": "..."
    }},
    {{
      "type": "POWER_BI_UPDATE",
      "dashboard": "...",
      "statut": "..."
    }}
  ],
  "resolution_estimee": "...",
  "escalade_requise": true,
  "responsable_final": "..."
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
    
    bi_result = {
        "impact_financier_estime": 420000,
        "sla_minutes_restantes": 47,
        "criticite": "CRITIQUE",
        "score_urgence": 95
    }
    
    print("⚡ Action Agent en cours de décision...")
    result = action_agent(incident, memory_result, bi_result)
    print(json.dumps(result, ensure_ascii=False, indent=2))