import json
import time
from memory_agent import memory_agent
from bi_agent import bi_agent
from action_agent import action_agent

def run_veqra_ai():
    with open("incident.json", encoding="utf-8") as f:
        incident = json.load(f)
    with open("memory_data.json", encoding="utf-8") as f:
        historical = json.load(f)

    print("\n" + "="*55)
    print("🔴 VEQRA AI — INCIDENT DETECTED")
    print(f"   {incident['client']} — {incident['montant']:,}€ — {incident['statut']}")
    print("="*55)

    print("\n🧠 Memory Agent analyzing...")
    t0 = time.time()
    memory_result = memory_agent(incident, historical)
    t1 = time.time()
    print(f"   ✅ Completed in {t1-t0:.1f}s")
    print(f"   → Similar case: {memory_result.get('reference_cas')}")
    print(f"   → Cause: {memory_result.get('cause_identifiee')}")
    print(f"   → Confidence: {memory_result.get('confiance')}")

    print("\n📊 BI Agent analyzing...")
    t0 = time.time()
    bi_result = bi_agent(incident, memory_result)
    t1 = time.time()
    print(f"   ✅ Completed in {t1-t0:.1f}s")
    print(f"   → Impact: {bi_result.get('impact_financier_estime'):,}€")
    print(f"   → SLA remaining: {bi_result.get('sla_minutes_restantes')} min")
    print(f"   → Criticality: {bi_result.get('criticite')}")

    print("\n⚡ Action Agent deciding...")
    t0 = time.time()
    action_result = action_agent(incident, memory_result, bi_result)
    t1 = time.time()
    print(f"   ✅ Completed in {t1-t0:.1f}s")
    for action in action_result.get("actions", []):
        dest = action.get('destinataire') or action.get('dashboard')
        print(f"   → {action['type']} : {dest}")

    print("\n" + "="*55)
    print("📋 VEQRA AI — EXECUTIVE SUMMARY")
    print("="*55)
    print(f"   Incident    : {incident['client']}")
    print(f"   Criticality : {bi_result.get('criticite')}")
    print(f"   Cause       : {memory_result.get('cause_identifiee')}")
    print(f"   Impact      : {bi_result.get('impact_financier_estime'):,}€")
    print(f"   SLA left    : {bi_result.get('sla_minutes_restantes')} min")
    print(f"   Priority    : {action_result.get('priorite')}")
    print(f"   Owner       : {action_result.get('responsable_final')}")
    print(f"   Resolution  : {action_result.get('resolution_estimee')}")
    print("="*55)
    print("✅ VEQRA AI — ANALYSIS COMPLETE\n")

if __name__ == "__main__":
    run_veqra_ai()