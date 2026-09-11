# 🩺 Veda-Lens: Longitudinal Clinical Intelligence & Medical Copilot

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![React 18](https://img.shields.io/badge/React_18-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Python 3.11](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy_2.0-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Overview

**Veda-Lens** is a next-generation clinical decision-support and longitudinal patient trajectory system. In traditional healthcare workflows, patient records are scattered across fragmented paper prescriptions, diagnostic lab reports, emergency department summaries, and discharge notes. Clinicians spend valuable consultation time piecing together historical context.

Veda-Lens solves this by synthesizing unstructured clinical encounters into an **interactive, chronological medical timeline**. Powered by domain-driven micro-modules and a multi-tiered clinical guardrail engine, Veda-Lens enables rapid medical record ingestion, timeline visualization, pharmacovigilance screening, and evidence-grounded AI copilot queries.

---

## 🔬 Core Architectural Capabilities

`
                  ┌────────────────────────────────────────────────────────┐
                  │                 Veda-Lens Web Portal                   │
                  │        (React 18 · TypeScript · Vite · Tailwind)       │
                  └───────────────────────────┬────────────────────────────┘
                                              │ REST / JSON (Async)
                                              ▼
                  ┌────────────────────────────────────────────────────────┐
                  │             Veda-Lens Core FastAPI Gateway             │
                  └───────┬──────────────┬──────────────┬──────────────┬───┘
                          │              │              │              │
                          ▼              ▼              ▼              ▼
     ┌──────────────────────┐ ┌──────────────────┐ ┌────────────────────┐ ┌──────────────────┐
     │   Patient & MRN      │ │ Medical Ingestion│ │ Longitudinal Event │ │ Pharmacological  │
     │   Identity Manager   │ │ & Optical Parser │ │ Trajectory Engine  │ │ Interaction Core │
     └──────────┬───────────┘ └────────┬─────────┘ └─────────┬──────────┘ └────────┬─────────┘
                │                      │                     │                     │
                └──────────────────────┴──────────┬──────────┴─────────────────────┘
                                                  │
                                                  ▼
                  ┌────────────────────────────────────────────────────────┐
                  │              Audited Clinical Copilot                  │
                  │   (PHI Redaction · Grounded RAG · Source Citation)     │
                  └───────────────────────────────┬────────────────────────┘
                                                  │
                                                  ▼
                  ┌────────────────────────────────────────────────────────┐
                  │             Persistent Storage Tier (Async)            │
                  │          SQLite / aiosqlite · Audit Logs · Vault       │
                  └────────────────────────────────────────────────────────┘
`

### 1. ⏱️ Longitudinal Patient Trajectory Engine
- Unifies outpatient visits, inpatient admissions, surgical procedures, and diagnostic labs into a coherent chronological timeline.
- Dynamic filtering by encounter type, severity grade, and chronological milestones.
- Highlights trajectory deviations, repeated hospital visits, and chronic disease progressions.

### 2. 🛡️ Multi-Layer Clinical Safety Firewall
- **De-Identification & PHI Scrubbing:** Automatically scrubs personally identifiable details before AI inference.
- **Strict Grounding Floor:** Every copilot response is strictly pinned to authenticated medical events and laboratory attachments.
- **Hallucination Prevention:** Fallbacks prevent speculative diagnoses when source documentation lacks sufficient corroboration.

### 3. 💊 Pharmacological Intelligence & Interaction Engine
- Parses complex multi-drug prescriptions and posology (dosage, frequency, delivery routes).
- Screens for cross-drug adverse reactions, contraindicated co-prescriptions, and duplicate therapeutic classes.
- Maintains historical medication adherence records across patient episodes.

### 4. ⚡ High-Throughput Async Architecture
- Clean Domain-Driven Design (DDD) with decoupled modular boundaries:
  - patients: Medical Record Number (MRN) lifecycle, demographics, and clinical status.
  - ingestion: Asynchronous processing of incoming diagnostic files, PDFs, and scanned charts.
  - 	imeline: Event extraction, chronology assembly, and severity weighting.
  - medicine_engine: Pharmacological database lookup, interactions, and dosage checks.
  - ssistant: Grounded clinical conversational engine with session context management.

---

## 🗂️ Project Organization

`	ext
Veda-Lens/
├── backend/
│   ├── app/
│   │   ├── api/v1/                # Route definitions & API controllers
│   │   ├── core/                  # Configuration, security, base exceptions
│   │   ├── database/              # Async database sessions & migrations
│   │   ├── modules/
│   │   │   ├── assistant/         # Clinical Copilot & grounded RAG
│   │   │   ├── clinical_engine/   # Diagnostic classification & triage rules
│   │   │   ├── ingestion/         # File parsing, uploads & OCR workers
│   │   │   ├── medicine_engine/   # Drug interactions & prescription parsing
│   │   │   ├── patients/          # MRN registry & patient records
│   │   │   └── timeline/          # Chronological event synthesis
│   │   ├── observability/         # Structured logger, audit trails & metrics
│   │   └── shared/                # Middleware, pagination & helpers
│   ├── tests/                     # Unit and integration test suites
│   ├── requirements.txt           # Production Python dependencies
│   └── build_backend.py           # Database seeder and setup utility
└── frontend/
    ├── src/
    │   ├── components/            # Reusable UI widgets & design system
    │   ├── features/
    │   │   ├── assistant/         # AI Copilot drawer & chat view
    │   │   ├── auth/              # Secure clinician login & onboarding
    │   │   ├── patients/          # Patient roster & detail trajectory views
    │   │   └── timeline/          # Visual clinical event stream
    │   ├── layouts/               # Dashboard layout & navigation shell
    │   ├── services/              # Axios API service endpoints
    │   └── theme/                 # Custom Tailwind theme & color palettes
    ├── package.json               # Frontend dependencies & scripts
    └── vite.config.ts             # Vite build configuration
`

---

## 🚀 Quickstart Guide

### Prerequisites
- **Python:** 3.10 or 3.11
- **Node.js:** 18.x or 20.x (with 
pm or pnpm)

---

### Backend Setup

1. **Navigate to the backend directory:**
   `ash
   cd backend
   `

2. **Create and activate a virtual environment:**
   `ash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   `

3. **Install dependencies:**
   `ash
   pip install -r requirements.txt
   `

4. **Set up environment variables:**
   `ash
   cp .env.example .env
   `
   *Configure your SECRET_KEY, DATABASE_URL, and optional OPENAI_API_KEY.*

5. **Initialize database and seed demo clinical records:**
   `ash
   python build_backend.py
   `

6. **Launch the FastAPI development server:**
   `ash
   uvicorn app.main:create_app --factory --reload --port 8000
   `
   *Interactive API documentation is accessible at http://localhost:8000/docs.*

---

### Frontend Setup

1. **Navigate to the frontend directory:**
   `ash
   cd ../frontend
   `

2. **Install frontend dependencies:**
   `ash
   npm install
   `

3. **Start the Vite development server:**
   `ash
   npm run dev
   `
   *The application interface will launch at http://localhost:5173.*

---

## 🔒 Security, Compliance & Data Governance

- **Role-Based Access Control (RBAC):** Restricts clinical records to authorized care providers.
- **Audit Logging:** Logs every chart read, edit, and AI inference request with tamper-resistant audit metadata.
- **Zero Raw PII Persistence:** De-identification utilities safeguard patient privacy across telemetry and analytics layers.

---

## 👤 Author & Maintainer

**Nazish Khan**
- **GitHub:** [@nazishkhan10](https://github.com/nazishkhan10)
- **Email:** [nazish400210@gmail.com](mailto:nazish400210@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) - feel free to build and expand upon this codebase.
