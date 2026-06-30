import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

def action_agent(incident: dict, memory_result: dict, bi_result: dict) -> dict:
    prompt = f"""
You are the Action Agent of VEQRA AI.
You decide the immediate corrective actions to resolve the incident.

INCIDENT:
{json.dumps(incident, ensure_ascii=False, indent=2)}

MEMORY ANALYSIS:
{json.dumps(memory_result, ensure_ascii=False, indent=2)}

BI ANALYSIS:
{json.dumps(bi_result, ensure_ascii=False, indent=2)}

Respond ONLY in JSON:
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
        "cause_identifiee": "Missing bank details",
        "solution_appliquee": "Data Owner escalation — resolved in 6h",
        "confiance": "HIGH"
    }

    bi_result = {
        "impact_financier_estime": 420000,
        "sla_minutes_restantes": 47,
        "criticite": "CRITICAL",
        "score_urgence": 95
    }

    print("⚡ Action Agent deciding...")
    result = action_agent(incident, memory_result, bi_result)
    print(json.dumps(result, ensure_ascii=False, indent=2))