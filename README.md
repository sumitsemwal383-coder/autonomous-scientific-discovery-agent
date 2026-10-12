# Autonomous Multimodal Scientific Discovery Agent
### Enterprise-Level Project: Data Science & Machine Learning — Project 1
**Zaalima Development Pvt. Ltd. | SOP Version 1.1 Team-Based Execution**

---

## 🔬 Project Overview

The **Autonomous Multimodal Scientific Discovery Agent** is an end-to-end self-directed AI researcher that:
1. **Scrapes & Ingests**: Queries ArXiv preprints and PubMed articles via live APIs, indexing dense vector representations into a vector database (Milvus/Pinecone compatible).
2. **Formulates Hypotheses**: Uses Retrieval-Augmented Generation (RAG) to generate novel, falsifiable scientific hypotheses ($H_0$ and $H_1$) strictly grounded in peer-reviewed literature.
3. **Executes in Sandbox**: Synthesizes Python experimental code and executes it within an AST-hardened Docker / subprocess execution sandbox with active breakout prevention.
4. **Self-Debugs via RL**: Implements a verbal Reinforcement Learning (Reflexion) feedback loop that analyzes error traces and autonomously rewrites defective code.
5. **Statistical Critic**: Rigorously evaluates empirical metrics, auditing $p$-values ($p < 0.05$), 95% Confidence Intervals, Cohen's $d$ effect sizes, and sample size power.
6. **Synthesizes LaTeX Papers**: Generates publication-ready academic manuscripts (`.tex`) and BibTeX citations (`.bib`).
7. **Live Supervisor Dashboard**: Provides a real-time Streamlit web console to trace logic trees, citations, execution telemetry, and cost metrics.

---

## 📁 Repository Structure

```
autonomous-scientific-discovery-agent/
│
├── .github/workflows/
│   ├── agent-ci.yml                 # Automated CI testing pipeline
│   └── sandbox-security-test.yml     # Automated penetration testing CI
│
├── config/
│   ├── settings.py                  # Global configurations, API endpoints, thresholds
│   └── agent_config.yaml            # Declarative agent role definitions
│
├── data/
│   ├── cache/                       # Cached ArXiv & PubMed preprints
│   ├── holdout_papers/              # Gold standard benchmark ground truth
│   ├── vector_store/                # Persistent vector database store
│   └── synthesis/                   # Generated LaTeX papers and .bib files
│
├── docker/
│   ├── Dockerfile.sandbox           # Hardened sandbox image definition
│   └── docker-compose.yml           # Multi-container orchestration (Milvus, Redis, Sandbox)
│
├── src/
│   ├── agents/
│   │   ├── base_agent.py            # Base abstract agent lifecycle interface
│   │   ├── literature_reviewer.py   # Week 1: ArXiv & PubMed Literature Reviewer Agent
│   │   ├── hypothesis_generator.py  # Week 1-2: Grounded RAG Hypothesis Generator Agent
│   │   ├── code_executor_agent.py   # Week 1-2: Sandboxed Code Executor Agent
│   │   ├── critic_agent.py          # Week 3: Statistical Critic Agent (p-values, CIs, Cohen's d)
│   │   └── orchestrator.py          # Core multi-agent state graph orchestrator
│   │
│   ├── ingestion/
│   │   ├── arxiv_pipeline.py        # Real ArXiv Atom API query parser
│   │   ├── pubmed_pipeline.py       # NCBI Entrez E-utilities PubMed connector
│   │   └── multimodal_parser.py     # Week 3: PDF chart and figure visual parser
│   │
│   ├── rag/
│   │   ├── embeddings.py            # Dense semantic embedding generator
│   │   ├── vector_db.py             # Vector database with Milvus/Pinecone adapters
│   │   └── retriever.py             # Literature retriever & citation grounder
│   │
│   ├── sandbox/
│   │   ├── secure_sandbox.py        # AST static security audit & breakout defense
│   │   ├── docker_sandbox.py        # Containerized Docker runner
│   │   └── execution_result.py      # Structured telemetry result dataclass
│   │
│   ├── rl/
│   │   ├── reward_model.py          # Multi-objective RL reward function
│   │   └── feedback_loop.py         # Reflexion self-debugging engine
│   │
│   ├── memory/
│   │   └── context_manager.py       # Week 3: Context window & token budget manager
│   │
│   ├── synthesis/
│   │   ├── latex_generator.py       # Week 4: LaTeX scientific manuscript compiler
│   │   └── templates/
│   │       └── research_paper.tex.jinja # Publication-ready LaTeX template
│   │
│   └── evaluation/
│       └── benchmark_evaluator.py   # Week 4: Holdout paper grading roadmap
│
├── dashboard/
│   └── app.py                       # Week 4: Live Streamlit supervisor monitoring console
│
├── tests/
│   ├── test_sandbox_security.py     # Active breakout prevention test suite (100% pass)
│   ├── test_critic_agent.py         # Statistical critic validation tests
│   ├── test_orchestrator.py         # End-to-end multi-agent & RL self-debugging tests
│   ├── test_ingestion.py            # ArXiv & PubMed connector tests
│   └── test_synthesis.py           # LaTeX generation tests
│
├── docs/
│   ├── ARCHITECTURE.md              # Detailed architecture & dataflow specification
│   ├── SOP_COMPLIANCE.md            # Zaalima Development SOP Version 1.1 compliance
│   └── WORK_DISTRIBUTION.md         # Team roles and week-wise task allocations
│
├── scripts/
│   ├── run_pipeline.py              # Command-line launcher for discovery cycles
│   ├── run_security_audit.py        # Penetration testing script
│   └── setup_git_branches.py        # Zaalima SOP Git branch initialization
│
├── RESEARCH_AND_ARCHITECTURE_REPORT.md # Official Deliverable: Research & Architecture Report
├── requirements.txt                 # Project dependencies
└── README.md                        # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Installation
Clone or open the repository directory:
```bash
cd C:\Users\sumit\.gemini\antigravity\scratch\autonomous-scientific-discovery-agent
pip install -r requirements.txt
```

### 2. Run Autonomous Discovery via CLI
Execute an end-to-end research cycle from the command line:
```bash
python scripts/run_pipeline.py --topic "multi-agent reinforcement learning reasoning" --max-papers 4
```

To test the **Reinforcement Learning Self-Debugging Feedback Loop**:
```bash
python scripts/run_pipeline.py --topic "iterative language model reflexion" --simulate-debug
```

### 3. Launch the Live Supervisor Monitoring Dashboard (Streamlit)
Launch the interactive web console:
```bash
streamlit run dashboard/app.py
```
Open your browser at `http://localhost:8501`. From the dashboard, supervisors can:
- Trigger autonomous discovery runs with customized research topics;
- Trace the agent's real-time state machine and execution event logs;
- Explore indexed ArXiv & PubMed preprints and vector similarity scores;
- Inspect sandbox execution stdout, stderr, and AST breakout audit status;
- Audit the Statistical Critic's p-values, 95% CIs, and empirical distribution plots;
- Preview and download the generated academic LaTeX manuscript (`.tex`) and BibTeX references;
- Review discovery grades against holdout human-authored papers.

### 4. Run the Test Suite
Verify all components:
```bash
# Sandbox Breakout Prevention Tests (100% Pass)
python tests/test_sandbox_security.py

# Statistical Critic Tests
python tests/test_critic_agent.py

# Multi-Agent Orchestrator & RL Self-Debugging Tests
python tests/test_orchestrator.py

# LaTeX Manuscript Generation Tests
python tests/test_synthesis.py

# Automated Penetration Testing
python scripts/run_security_audit.py
```

### 5. Zaalima SOP Git Branch Setup
Initialize compliant role branches and commits meeting Zaalima's 10-day and 20-day review rules:
```bash
python scripts/setup_git_branches.py
```

---

## 🏆 Zaalima SOP Version 1.1 Compliance Summary
- **Month 1 Review Cycle**: Project 1 completed across Weeks 1 to 4.
- **Mid-Project Review (Week 2)**: Multi-agent orchestration, vector database ingestion, containerized sandbox, and breakout prevention validated.
- **Final Project Review (Week 4)**: Multimodal ingestion, Statistical Critic Agent, Streamlit supervisor dashboard, LaTeX paper synthesis, and official Research & Architecture Report delivered.
