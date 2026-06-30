# VEQRA AI — Multi-Agent Incident Resolution Platform

> **Qwen Cloud Hackathon** — Real-time resolution of critical enterprise incidents through AI agent orchestration powered by **Qwen3-235B**

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

**Scenario: 120,000 € VIP leasing incident resolved in 13 seconds**

```
🔴 INCIDENT DETECTED
   MERIDIAN FINANCE SA — 120,000 € — OVERDUE

🧠 Memory Agent ...  ✅ 4.2s  → Similar case INC-2026-0731 | Cause: Missing RIB | Confidence: HIGH
📊 BI Agent      ...  ✅ 4.8s  → Impact: 420,000 € | SLA remaining: 47 min | Criticality: CRITICAL
⚡ Action Agent  ...  ✅ 4.1s  → TEAMS_TASK: Data Owner | EMAIL: Management | POWER_BI_UPDATE: Dashboard

✅ ANALYSIS COMPLETE — 13.1s
```

---

## Project Description

VEQRA AI is a multi-agent orchestration platform designed for financial enterprises. It automatically detects, analyzes, and resolves critical incidents (payment delays, contractual blockers, leasing anomalies) by combining three specialized AI agents coordinated by a central orchestrator.

**Problem solved:** an undetected or poorly escalated VIP leasing incident can cost hundreds of thousands of euros and break a strategic client relationship. VEQRA AI compresses the human response cycle (hours → seconds) by simultaneously leveraging historical memory, financial analysis, and decision-making.

---

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  orchestrator.py                │
│                 (Single entry point)            │
└────────────┬───────────────────────────────────┘
             │  loads incident.json + memory_data.json
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

| Layer | Role |
|---|---|
| **Orchestrator** | Loads data, calls the agents in sequence, produces the final report |
| **Memory Agent** | Finds similar cases in the history, identifies the root cause |
| **BI Agent** | Calculates the financial impact, criticality, remaining SLA, urgency score |
| **Action Agent** | Decides and generates corrective actions (Teams, Email, Power BI) |
| **Dashboard** | Real-time HTML visualization of the incident and agent statuses |

All agents call **Qwen3-235B-A22B** via the DashScope API (OpenAI-compatible mode) and respond in structured JSON.

---

## Technologies Used

| Technology | Usage |
|---|---|
| **Qwen3-235B-A22B** | Language model — reasoning for each agent |
| **Alibaba Cloud DashScope** | Inference API (OpenAI-compatible) |
| **Python 3.11+** | Agent runtime |
| **openai SDK** | HTTP client for DashScope |
| **HTML / CSS / JS** | Visualization dashboard |
| **JSON** | Inter-agent input/output format |

---

## File Structure

```
VEQRA-AI/
├── orchestrator.py       # Entry point — orchestrates the 3 agents
├── memory_agent.py       # Memory agent — similar case search
├── bi_agent.py           # BI agent — financial and criticality analysis
├── action_agent.py       # Action agent — decision and escalation
├── dashboard.html        # Real-time visualization interface
├── incident.json         # Current incident data
├── memory_data.json      # History of resolved incidents
└── .gitignore
```

---

## Installation

### Prerequisites

- Python 3.11+
- An [Alibaba Cloud / DashScope](https://dashscope.aliyuncs.com/) account with Qwen3 access

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/nabilfattouch1/VEQRA-AI.git
cd VEQRA-AI

# 2. Install dependencies
pip install openai

# 3. Configure the API key
export DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

> Set this environment variable before running any agent — the `api_key` value is loaded from `DASHSCOPE_API_KEY`, never hardcoded.

---

## Usage

### Run the full demo

```bash
python orchestrator.py
```

### Run a single agent

```bash
python memory_agent.py   # Memory analysis only
python bi_agent.py       # Financial analysis only
python action_agent.py   # Action generation only
```

### Modify the incident scenario

Edit `incident.json` to test another case:

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

### Open the dashboard

Open `dashboard.html` directly in your browser — no server required.

---

## Demo — Incident Detail

| Field | Value |
|---|---|
| **Incident ID** | INC-2026-0847 |
| **Client** | MERIDIAN FINANCE SA |
| **Amount** | 120,000 € |
| **Status** | OVERDUE |
| **Due date** | June 25, 2026 |
| **Detection** | June 29, 2026 |
| **SLA** | 4h (3h12 already elapsed) |

**Results produced by VEQRA AI:**

| Agent | Key Result | Time |
|---|---|---|
| Memory Agent | Similar case: INC-2026-0731 — Cause: Missing RIB — Confidence: HIGH | ~4s |
| BI Agent | Estimated impact: 420,000 € — Criticality: CRITICAL — Urgency score: 95/100 | ~5s |
| Action Agent | TEAMS_TASK → Data Owner, EMAIL → Management, POWER_BI_UPDATE → Leasing Dashboard | ~4s |
| **Total** | **Full analysis + action plan** | **~13s** |

---

## Qwen Cloud Hackathon

This project was developed for the **Qwen Cloud Hackathon**, organized by Alibaba Cloud. It demonstrates the ability of Qwen3-235B to power a production-grade multi-agent system for critical enterprise use cases.

---

## Author

**Nabil Fattouch** — [github.com/nabilfattouch1](https://github.com/nabilfattouch1)
