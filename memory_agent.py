import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
)

def memory_agent(incident: dict, historical_cases: list) -> dict:
    prompt = f"""
Tu es le Memory Agent de VEQRA AI, une plateforme d'orchestration d'agents IA pour entreprises.
Tu analyses les incidents critiques et tu retrouves les cas similaires dans l'historique.

INCIDENT EN COURS :
{json.dumps(incident, ensure_ascii=False, indent=2)}

CAS HISTORIQUES DISPONIBLES :
{json.dumps(historical_cases, ensure_ascii=False, indent=2)}

Analyse et réponds UNIQUEMENT en JSON avec cette structure :
{{
  "cas_similaire_trouve": true,
  "reference_cas": "INC-XXXX-XXXX",
  "date_cas_similaire": "YYYY-MM-DD",
  "cause_identifiee": "...",
  "solution_appliquee": "...",
  "confiance": "HAUTE",
  "recommandation": "..."
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
    with open("memory_data.json", encoding="utf-8") as f:
        historical = json.load(f)
    
    print("🧠 Memory Agent en cours d'analyse...")
    result = memory_agent(incident, historical)
    print(json.dumps(result, ensure_ascii=False, indent=2))