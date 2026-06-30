# VEQRA AI — Multi-Agent Incident Resolution Platform

> **Hackathon Qwen Cloud** — Résolution d'incidents critiques enterprise en temps réel par orchestration d'agents IA propulsés par **Qwen3-235B**

---

## 🏆 Hackathon Submission Requirements

| Requirement | Link |
|---|---|
| 📄 License | [LICENSE](./LICENSE) (MIT) |
| 🏗️ Technical Architecture | [ARCHITECTURE.md](./ARCHITECTURE.md) |
| ☁️ Alibaba Cloud Proof | [ALIBABA_CLOUD_PROOF.md](./ALIBABA_CLOUD_PROOF.md) |
| 🎯 Track | **MemoryAgent** |

---

## Demo

**Scénario : Incident leasing VIP 120 000 € résolu en 13 secondes**

```
🔴 INCIDENT DÉTECTÉ
   MERIDIAN FINANCE SA — 120 000 € — OVERDUE

🧠 Memory Agent ...  ✅ 4.2s  → Cas similaire INC-2026-0731 | Cause : RIB bancaire manquant | Confiance : HAUTE
📊 BI Agent      ...  ✅ 4.8s  → Impact : 420 000 € | SLA restant : 47 min | Criticité : CRITIQUE
⚡ Action Agent  ...  ✅ 4.1s  → TEAMS_TASK : Data Owner | EMAIL : Direction | POWER_BI_UPDATE : Dashboard

✅ ANALYSE COMPLÈTE — 13.1s
```

---

## Description du projet

VEQRA AI est une plateforme d'orchestration multi-agents conçue pour les entreprises financières. Elle détecte, analyse et résout automatiquement les incidents critiques (retards de paiement, blocages contractuels, anomalies leasing) en combinant trois agents IA spécialisés coordonnés par un orchestrateur central.

**Problème résolu :** un incident leasing VIP non détecté ou mal escaladé peut coûter des centaines de milliers d'euros et briser une relation client stratégique. VEQRA AI compresse le cycle de réponse humain (heures → secondes) en mobilisant simultanément la mémoire historique, l'analyse financière et la prise de décision.

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  orchestrator.py                │
│              (Point d'entrée unique)            │
└────────────┬───────────────────────────────────┘
             │  charge incident.json + memory_data.json
             │
     ┌───────▼────────────────────────────────────┐
     │                                            │
     ▼                ▼                   ▼       │
┌──────────┐   ┌──────────┐      ┌──────────────┐ │
│  Memory  │   │    BI    │      │    Action    │ │
│  Agent   │──▶│  Agent   │─────▶│    Agent     │ │
└──────────┘   └──────────┘      └──────────────┘ │
     │               │                   │        │
     └───────────────┴───────────────────┘        │
                     │                            │
               Executive Summary ◀────────────────┘
                 + dashboard.html
```

| Couche | Rôle |
|---|---|
| **Orchestrateur** | Charge les données, appelle les agents en séquence, produit le rapport final |
| **Memory Agent** | Retrouve les cas similaires dans l'historique, identifie la cause racine |
| **BI Agent** | Calcule l'impact financier, la criticité, le SLA restant, le score d'urgence |
| **Action Agent** | Décide et génère les actions correctives (Teams, Email, Power BI) |
| **Dashboard** | Visualisation HTML temps réel de l'incident et du statut des agents |

Tous les agents appellent **Qwen3-235B-A22B** via l'API DashScope (mode compatible OpenAI) et répondent en JSON structuré.

---

## Technologies utilisées

| Technologie | Usage |
|---|---|
| **Qwen3-235B-A22B** | Modèle de langage — raisonnement de chaque agent |
| **Alibaba Cloud DashScope** | API d'inférence (compatible OpenAI) |
| **Python 3.11+** | Runtime des agents |
| **openai SDK** | Client HTTP vers DashScope |
| **HTML / CSS / JS** | Dashboard de visualisation |
| **JSON** | Format d'entrée/sortie inter-agents |

---

## Structure des fichiers

```
VEQRA-AI/
├── orchestrator.py       # Point d'entrée — orchestre les 3 agents
├── memory_agent.py       # Agent mémoire — recherche de cas similaires
├── bi_agent.py           # Agent BI — analyse financière et criticité
├── action_agent.py       # Agent action — décision et escalade
├── dashboard.html        # Interface de visualisation temps réel
├── incident.json         # Données de l'incident en cours
├── memory_data.json      # Historique des incidents résolus
└── .gitignore
```

---

## Installation

### Prérequis

- Python 3.11+
- Un compte [Alibaba Cloud / DashScope](https://dashscope.aliyuncs.com/) avec accès Qwen3

### Étapes

```bash
# 1. Cloner le repo
git clone https://github.com/nabilfattouch1/VEQRA-AI.git
cd VEQRA-AI

# 2. Installer les dépendances
pip install openai

# 3. Configurer la clé API
export DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

> Remplacez la valeur de `api_key` dans chaque agent par votre clé, ou mieux — chargez-la depuis une variable d'environnement.

---

## Utilisation

### Lancer la démo complète

```bash
python orchestrator.py
```

### Lancer un agent individuellement

```bash
python memory_agent.py   # Analyse mémorielle seule
python bi_agent.py       # Analyse financière seule
python action_agent.py   # Génération d'actions seule
```

### Modifier le scénario d'incident

Éditez `incident.json` pour tester un autre cas :

```json
{
  "id": "INC-2026-0847",
  "type": "LEASING_VIP",
  "client": "MERIDIAN FINANCE SA",
  "montant": 120000,
  "statut": "OVERDUE",
  "sla_heures": 4,
  "heures_ecoulees": 3.2
}
```

### Ouvrir le dashboard

Ouvrez `dashboard.html` directement dans votre navigateur — aucun serveur requis.

---

## Démo — Détail de l'incident

| Champ | Valeur |
|---|---|
| **ID incident** | INC-2026-0847 |
| **Client** | MERIDIAN FINANCE SA |
| **Montant** | 120 000 € |
| **Statut** | OVERDUE |
| **Échéance** | 25 juin 2026 |
| **Détection** | 29 juin 2026 |
| **SLA** | 4h (3h12 déjà écoulées) |

**Résultats produits par VEQRA AI :**

| Agent | Résultat clé | Temps |
|---|---|---|
| Memory Agent | Cas similaire : INC-2026-0731 — Cause : RIB bancaire manquant — Confiance : HAUTE | ~4s |
| BI Agent | Impact estimé : 420 000 € — Criticité : CRITIQUE — Score urgence : 95/100 | ~5s |
| Action Agent | TEAMS_TASK → Data Owner, EMAIL → Direction, POWER_BI_UPDATE → Dashboard leasing | ~4s |
| **Total** | **Analyse complète + plan d'action** | **~13s** |

---

## Hackathon Qwen Cloud

Ce projet a été développé dans le cadre du **Hackathon Qwen Cloud**, organisé par Alibaba Cloud. Il démontre la capacité de Qwen3-235B à alimenter un système multi-agents de niveau production pour des cas d'usage enterprise critiques.

---

## Auteur

**Nabil Fattouch** — [github.com/nabilfattouch1](https://github.com/nabilfattouch1)
