# Work Distribution Document
**Zaalima Development Pvt. Ltd. — Team Project Execution**
**Project 1: Autonomous Multimodal Scientific Discovery Agent**

---

### Team Allocation Overview

| Team Role | Assigned Member / Specialist | Primary Responsibilities | Dedicated Git Branch |
|---|---|---|---|
| **Team Lead / Systems Architect** | Lead Engineer | Overall orchestration, multi-agent state graph, Git branch management, and CI/CD pipelines | `main` |
| **Data Ingestion & RAG Engineer** | Member 1 (Literature Specialist) | ArXiv & PubMed API connectors, vector database integration (Milvus/Pinecone), citation grounder | `feature/literature-reviewer` |
| **Reasoning & Synthesis Specialist** | Member 2 (Hypothesis Specialist) | Grounded hypothesis formulation, academic LaTeX synthesis engine, and BibTeX generator | `feature/hypothesis-generator` |
| **Sandbox & Security Engineer** | Member 3 (Systems & RL Specialist) | Docker sandbox environment, AST security filter, breakout prevention, and RL self-debugging loop | `feature/code-executor-sandbox` |
| **Statistical & Multimodal Specialist** | Member 4 (ML & Critic Specialist) | Statistical Critic Agent ($p$-values, CIs, Cohen's $d$, power), multimodal PDF chart parser, Streamlit UI | `feature/critic-agent-statistics` |

---

### Week-Wise Task Distribution

#### Week 1 (Implementation Phase 1)
- **Member 1**: Build automated data ingestion pipelines for ArXiv Atom API and NCBI PubMed E-utilities.
- **Member 2**: Structure vector database schema and dense embedding pipeline.
- **Member 3**: Implement base agent interfaces and state machine orchestration architecture.
- **Member 4**: Establish Git repository, branch rules, and initial CI workflow.

#### Week 2 (Implementation Phase 2)
- **Member 1**: Implement Retrieval-Augmented Generation (RAG) to ground hypotheses strictly in peer-reviewed literature.
- **Member 2**: Formulate testable scientific hypotheses ($H_0$ and $H_1$) and experimental variable specifications.
- **Member 3**: Develop containerized Docker execution sandbox and static AST security filter to actively prevent breakouts.
- **Member 4**: Integrate Reinforcement Learning self-debugging feedback loop with multi-objective reward modeling.
- **All Members**: Mid-Project Review validation (Operational framework, vector DB, breakout prevention verified).

#### Week 3 (Implementation Phase 3)
- **Member 1**: Upgrade ingestion engine for multimodal scientific data (PDF charts, loss curves, distribution plots).
- **Member 2**: Develop context window memory management (sliding window + summarization) for multi-day tasks.
- **Member 3**: Optimize sandbox runtime isolation and execution telemetry dumping.
- **Member 4**: Implement Statistical Critic Agent evaluating $p$-values, confidence intervals, effect sizes, and power.

#### Week 4 (Implementation Phase 4)
- **Member 1**: Build holdout paper benchmark evaluation roadmap comparing agent discoveries against human literature.
- **Member 2**: Implement LaTeX scientific paper synthesis module with Jinja2 templating and BibTeX references.
- **Member 3**: Develop live Streamlit supervisor monitoring dashboard (logic tree, citations, costs, metrics).
- **Member 4**: Compile comprehensive Autonomous Scientific Agent Research & Architecture Report.
- **All Members**: Final Project Review delivery and evaluation defense.
