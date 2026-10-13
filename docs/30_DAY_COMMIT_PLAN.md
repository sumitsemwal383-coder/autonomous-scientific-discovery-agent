# Complete 30-Day Git Commit Strategy & Detailed Work Allocation
**Zaalima Development Pvt. Ltd. — Enterprise Project 1: Autonomous Multimodal Scientific Discovery Agent**  
**Team Roster (3 Members):**
- **Sumeet (Team Lead):** Systems Architecture, Multi-Agent Orchestration, AST Sandbox & RL Self-Debugging
- **Janvi (Data Specialist):** ArXiv/PubMed Pipelines, Dense Vector Database, RAG Grounding & Multimodal Vision
- **Sanskar (ML & UI Specialist):** Statistical Critic Agent, Context Memory, LaTeX Synthesis & Streamlit Dashboard

---

## 1. Deep-Dive Work Breakdown by Member

### 👤 1.1 Sumeet — Team Lead & Systems / RL Architect
**Branch:** `sumeet/orchestrator-sandbox-rl`
**Primary Ownership & Responsibilities:**
1. **Multi-Agent Orchestrator (`src/agents/orchestrator.py` & `base_agent.py`):**
   - Implements the state machine workflow (`IDLE` -> `LITERATURE_REVIEW` -> `MULTIMODAL` -> `HYPOTHESIS` -> `SANDBOX` -> `RL_REFLEXION` -> `CRITIC` -> `SYNTHESIS`).
   - Manages role handoffs, event logging, duration tracking, and token cost estimations.
2. **AST Static Security Sandbox (`src/sandbox/secure_sandbox.py` & `execution_result.py`):**
   - Parses generated Python scripts with `ast.parse()`.
   - Actively intercepts unauthorized imports (`os`, `subprocess`, `sys`, `socket`, `ctypes`, `shutil`).
   - Intercepts dangerous calls (`eval()`, `exec()`, `compile()`) and reflective breakouts (`__subclasses__`, `__bases__`, `__globals__`).
   - Enforces execution timeouts (30s) and captures telemetry metrics (`__AGENT_METRICS__`).
3. **Containerized Docker Sandbox (`docker/Dockerfile.sandbox`, `docker-compose.yml`, `docker_sandbox.py`):**
   - Defines minimal Python 3.11 image dropping all Linux capabilities (`--cap-drop ALL`), setting read-only root and 512 MB memory quota.
4. **Reinforcement Learning Self-Debugging Feedback Loop (`src/rl/`):**
   - Implements `DiscoveryRewardModel`: Computes scalar rewards in $[-1.0, 1.0]$ based on syntax, execution pass, statistical significance, and literature grounding. Clamps reward to $-1.0$ for breakout attempts.
   - Implements `SelfDebuggingFeedbackLoop`: Analyzes stack traces (`NameError`, `ZeroDivisionError`, `SyntaxError`) and writes corrective linguistic reflexions to prompt the Code Executor to rewrite code.
5. **Team Lead Responsibilities:**
   - Git repository setup, merge management (`--no-ff`), CI pipelines (`.github/workflows/`), and architecture reports.

---

### 👤 1.2 Janvi — Data Ingestion, RAG & Multimodal Specialist
**Branch:** `janvi/ingestion-rag-multimodal`
**Primary Ownership & Responsibilities:**
1. **ArXiv Preprints Ingestion Pipeline (`src/ingestion/arxiv_pipeline.py`):**
   - Interrogates `http://export.arxiv.org/api/query` via HTTP requests.
   - Parses XML Atom feed entries, extracting titles, abstracts, author lists, primary categories (`cs.AI`, `stat.ML`), and PDF links.
   - Implements local JSON cache (`data/cache/arxiv_papers_cache.json`) with fallback preprints for offline robustness.
2. **PubMed Biomedical Ingestion Pipeline (`src/ingestion/pubmed_pipeline.py`):**
   - Connects to NCBI Entrez E-utilities (`esearch.fcgi` and `esummary.fcgi`).
   - Retrieves peer-reviewed biomedical literature, parsing XML metadata and caching articles (`data/cache/pubmed_papers_cache.json`).
3. **Dense Semantic Vector Database (`src/rag/embeddings.py` & `vector_db.py`):**
   - `DenseEmbeddingGenerator`: Generates 128-dimensional dense vectors using n-gram hashing and subword frequency projection with cosine similarity.
   - `VectorDatabase`: Disk-persisted vector store (`data/vector_store/`), offering top-$k$ nearest neighbor search and category filtering.
   - `MilvusAdapter` & `PineconeAdapter`: Enterprise cloud/cluster connector interfaces.
4. **Retrieval-Augmented Generation Grounding (`src/rag/retriever.py`):**
   - Retrieves top-$k$ preprints for a topic and formats citation-grounded context (`[Ref_1]`, `[Ref_2]`).
   - Verifies that generated hypotheses cite at least one verified retrieved document.
5. **Multimodal Document & Figure Parser (`src/ingestion/multimodal_parser.py`):**
   - Ingests figures from scientific PDFs (loss curves, comparative bar charts, empirical distribution plots).
   - Extracts visual trendlines, axis labels, and quantitative numbers to enrich the agent's knowledge base.

---

### 👤 1.3 Sanskar — Statistical Critic, Academic Synthesis & Streamlit UI
**Branch:** `sanskar/critic-synthesis-dashboard`
**Primary Ownership & Responsibilities:**
1. **Statistical Critic Agent (`src/agents/critic_agent.py`):**
   - Audits experimental outputs from the Code Executor to prevent false scientific discoveries.
   - Calculates two-tailed Student's $t$-statistic and exact $p$-value ($p < 0.05$).
   - Computes standardized Cohen's $d$ effect sizes ($d \ge 0.8$ large, $d \ge 0.5$ moderate).
   - Computes 95% Confidence Intervals for mean differences, verifying that zero is excluded.
   - Evaluates statistical power ($\beta \ge 0.80$) to prevent underpowered trials.
   - Renders formal verdicts: `CONFIRMED_STATISTICALLY_SIGNIFICANT`, `REJECTED_INSIGNIFICANT`, or `INCONCLUSIVE_UNDERPOWERED`.
2. **Context Window Memory Manager (`src/memory/context_manager.py`):**
   - Manages token budget within 8,192 token limit.
   - Implements sliding window for recent episodic actions and automated summarization for aging multi-day experiments.
3. **Academic LaTeX Synthesis Engine (`src/synthesis/latex_generator.py` & Jinja template):**
   - Converts discoveries into publication-ready LaTeX manuscripts (`.tex`) with structured sections (Abstract, Intro, Related Work, Hypotheses, Results Table, Discussion).
   - Generates formatted `.bib` BibTeX bibliography.
4. **Live Supervisor Monitoring Dashboard (`dashboard/app.py`):**
   - Streamlit application displaying real-time logic tree state machines, literature citation explorer, sandbox execution logs, statistical distributions, LaTeX preview/download, and API cost tracking.
5. **Holdout Benchmark Evaluator (`src/evaluation/benchmark_evaluator.py`):**
   - Grades the agent across literature grounding, statistical rigor, sandbox security, and LaTeX synthesis against human-authored reference papers.

---

## 2. 30-Day Master Commit Schedule (All 3 Members Commit Daily)

Every single day from Day 1 to Day 30, **Sumeet**, **Janvi**, and **Sanskar** each push a commit to their dedicated branch.

### 📅 WEEK 1: Project Foundations, Core APIs & Baseline Sandbox

#### Day 1
- **Sumeet:** `config/settings.py` -> `feat(core): initialize system paths, security limits, and thresholds`
- **Janvi:** `config/agent_config.yaml` -> `chore(config): define declarative agent role schemas`
- **Sanskar:** `tests/__init__.py`, `tests/test_critic_agent.py` -> `test(critic): create test harness skeleton for statistical critic`

#### Day 2
- **Sumeet:** `src/agents/base_agent.py` -> `feat(agents): implement abstract base agent class and telemetry hooks`
- **Janvi:** `src/ingestion/arxiv_pipeline.py` -> `feat(ingestion): implement arxiv atom api search query builder`
- **Sanskar:** `src/agents/critic_agent.py` -> `feat(critic): initialize critic agent with alpha=0.05 baseline threshold`

#### Day 3
- **Sumeet:** `src/sandbox/execution_result.py` -> `feat(sandbox): create ExecutionResult dataclass with security metrics`
- **Janvi:** `src/ingestion/arxiv_pipeline.py` -> `feat(ingestion): parse atom xml entries and extract preprint metadata`
- **Sanskar:** `src/agents/critic_agent.py` -> `feat(critic): implement two-tailed students t-test and p-value calculation`

#### Day 4
- **Sumeet:** `src/sandbox/secure_sandbox.py` -> `feat(sandbox): build ast security visitor blocking unauthorized modules`
- **Janvi:** `src/ingestion/arxiv_pipeline.py` -> `feat(ingestion): implement local disk caching and fallback preprints`
- **Sanskar:** `src/agents/critic_agent.py` -> `feat(critic): add standardized cohens d effect size calculation`

#### Day 5
- **Sumeet:** `src/sandbox/secure_sandbox.py` -> `feat(sandbox): implement AST interception of eval, exec, and compile`
- **Janvi:** `tests/test_ingestion.py` -> `test(ingestion): create unit tests for arxiv preprint ingestion`
- **Sanskar:** `src/agents/critic_agent.py` -> `feat(critic): compute 95 percent confidence intervals for treatment gains`

#### Day 6
- **Sumeet:** `src/sandbox/secure_sandbox.py` -> `feat(sandbox): detect reflective sandbox breakouts on __subclasses__`
- **Janvi:** `src/ingestion/pubmed_pipeline.py` -> `feat(ingestion): implement ncbi entrez esearch for biomedical papers`
- **Sanskar:** `src/agents/critic_agent.py` -> `feat(critic): implement statistical power estimation guarding against beta error`

#### Day 7
- **Sumeet:** `tests/test_sandbox_security.py` -> `test(sandbox): write tests verifying os and subprocess breakout blocks`
- **Janvi:** `src/ingestion/pubmed_pipeline.py` -> `feat(ingestion): parse pubmed esummary records and extract abstracts`
- **Sanskar:** `tests/test_critic_agent.py` -> `test(critic): add test cases validating p-value and effect size assertions`

---

### 📅 WEEK 2: RAG Vector Store, Docker Containers & RL Self-Debugging

#### Day 8
- **Sumeet:** `src/sandbox/secure_sandbox.py` -> `feat(sandbox): add isolated subprocess runner with 30s timeout enforcement`
- **Janvi:** `src/rag/embeddings.py` -> `feat(rag): implement dense semantic embedding generator using n-gram hashing`
- **Sanskar:** `src/memory/context_manager.py` -> `feat(memory): implement episodic context manager with token estimator`

#### Day 9
- **Sumeet:** `docker/Dockerfile.sandbox` -> `feat(docker): write hardened minimal dockerfile with non-root sandboxuser`
- **Janvi:** `src/rag/vector_db.py` -> `feat(rag): construct disk-persisted vector store with cosine similarity`
- **Sanskar:** `src/memory/context_manager.py` -> `feat(memory): implement sliding window history retention logic`

#### Day 10
- **Sumeet:** `docker/docker-compose.yml` -> `feat(docker): configure compose services with cap-drop ALL and 512mb RAM`
- **Janvi:** `src/rag/vector_db.py` -> `feat(rag): implement milvus and pinecone enterprise protocol adapters`
- **Sanskar:** `src/memory/context_manager.py` -> `feat(memory): add milestone summarizer to compress aging episodes`

#### Day 11
- **Sumeet:** `src/sandbox/docker_sandbox.py` -> `feat(sandbox): build docker sandbox runner with hardened subprocess fallback`
- **Janvi:** `src/rag/retriever.py` -> `feat(rag): implement literature retriever formatting grounded context blocks`
- **Sanskar:** `src/synthesis/templates/research_paper.tex.jinja` -> `feat(synthesis): construct academic latex manuscript jinja template`

#### Day 12
- **Sumeet:** `src/rl/reward_model.py` -> `feat(rl): implement discovery reward model with security breakout penalty`
- **Janvi:** `src/rag/retriever.py` -> `feat(rag): implement citation provenance verification against retrieved papers`
- **Sanskar:** `src/synthesis/templates/research_paper.tex.jinja` -> `feat(synthesis): add latex table generator for statistical critic results`

#### Day 13
- **Sumeet:** `src/rl/feedback_loop.py` -> `feat(rl): implement diagnostic stack trace parser for syntax & runtime errors`
- **Janvi:** `src/agents/hypothesis_generator.py` -> `feat(hypothesis): ground hypothesis generation in peer citations via RAG`
- **Sanskar:** `src/synthesis/latex_generator.py` -> `feat(synthesis): build automated bibtex bibliography compiler`

#### Day 14 (Mid-Project Review Checkpoint)
- **Sumeet:** `src/rl/feedback_loop.py` -> `feat(rl): generate actionable verbal reflexions to guide code rewrites`
- **Janvi:** `src/agents/literature_reviewer.py` -> `feat(agents): connect literature reviewer to vector db indexing pipeline`
- **Sanskar:** `docs/WORK_DISTRIBUTION.md` -> `docs(compliance): formalize team work distribution for mid-review audit`
- **Team Lead Merge (Sumeet):** `main` -> `merge: integrate week 1 and 2 features for mid-project review`

---

### 📅 WEEK 3: Multimodal Vision, Code Synthesis & Orchestration

#### Day 15
- **Sumeet:** `src/agents/code_executor_agent.py` -> `feat(code_exec): build code executor synthesizing statistical experiment scripts`
- **Janvi:** `src/ingestion/multimodal_parser.py` -> `feat(multimodal): build visual figure classifier for research pdfs`
- **Sanskar:** `src/synthesis/latex_generator.py` -> `feat(synthesis): build full latex manuscript compiler with error checks`

#### Day 16
- **Sumeet:** `src/agents/code_executor_agent.py` -> `feat(code_exec): add structured metric extraction hook __AGENT_METRICS__`
- **Janvi:** `src/ingestion/multimodal_parser.py` -> `feat(multimodal): extract quantitative trendlines from pdf loss curves`
- **Sanskar:** `tests/test_synthesis.py` -> `test(synthesis): create test suite validating latex syntax and bibtex`

#### Day 17
- **Sumeet:** `src/agents/code_executor_agent.py` -> `feat(code_exec): wire closed-loop reflexion feedback into code executor`
- **Janvi:** `src/ingestion/multimodal_parser.py` -> `feat(multimodal): parse comparative bar charts and extract confidence bounds`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): initialize streamlit supervisor console layout and sidebar`

#### Day 18
- **Sumeet:** `src/agents/orchestrator.py` -> `feat(orchestrator): assemble multi-agent state graph transitions`
- **Janvi:** `src/ingestion/multimodal_parser.py` -> `feat(multimodal): synthesize visual evidence into structured text chunks`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): add interactive logic tree state machine visualizer`

#### Day 19
- **Sumeet:** `src/agents/orchestrator.py` -> `feat(orchestrator): connect sandbox execution and critic evaluation states`
- **Janvi:** `data/cache/` -> `chore(data): populate offline preprint cache for resilient discovery`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): build literature knowledge base explorer and citation viewer`

#### Day 20
- **Sumeet:** `tests/test_orchestrator.py` -> `test(orchestrator): create end-to-end multi-agent discovery cycle test`
- **Janvi:** `data/vector_store/` -> `test(rag): verify vector database persistence and top-k ranking`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): build sandbox execution telemetry and code inspector tab`

#### Day 21
- **Sumeet:** `tests/test_orchestrator.py` -> `test(rl): validate autonomous code repair across 2 debug iterations`
- **Janvi:** `src/ingestion/multimodal_parser.py` -> `feat(ingestion): wire multimodal visual evidence into vector store`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): add empirical distribution charts and critic metric cards`

---

### 📅 WEEK 4: Streamlit Dashboard, Holdout Grading & Penetration Audits

#### Day 22
- **Sumeet:** `scripts/run_pipeline.py` -> `feat(cli): build command-line discovery runner with simulation flags`
- **Janvi:** `data/holdout_papers/benchmark_ground_truth.json` -> `data(benchmarks): compile gold standard human research reference set`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): add latex manuscript preview and one-click download`

#### Day 23
- **Sumeet:** `scripts/run_security_audit.py` -> `test(security): add automated penetration testing script with 8 attack payloads`
- **Janvi:** `src/evaluation/benchmark_evaluator.py` -> `feat(eval): compute grounding and literature attribution scores`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): integrate real-time token tracking and cost analytics`

#### Day 24
- **Sumeet:** `.github/workflows/agent-ci.yml` -> `ci: configure automated github actions test pipeline for pull requests`
- **Janvi:** `src/evaluation/benchmark_evaluator.py` -> `feat(eval): implement statistical rigor scoring against human holdout`
- **Sanskar:** `src/evaluation/benchmark_evaluator.py` -> `feat(eval): implement overall quality scoring and grade calculation`

#### Day 25
- **Sumeet:** `.github/workflows/sandbox-security-test.yml` -> `ci: add nightly sandbox penetration testing security workflow`
- **Janvi:** `src/evaluation/benchmark_evaluator.py` -> `test(eval): add test cases validating holdout benchmark evaluation`
- **Sanskar:** `dashboard/app.py` -> `feat(dashboard): add holdout benchmark grading tab with radar dimensions`

#### Day 26
- **Sumeet:** `docs/ARCHITECTURE.md` -> `docs(arch): detail multi-agent topology, sandbox model, and dataflows`
- **Janvi:** `docs/SOP_COMPLIANCE.md` -> `docs(compliance): document week-by-week zaalima sop compliance proof`
- **Sanskar:** `docs/WORK_DISTRIBUTION.md` -> `docs(compliance): finalize team work distribution and role sign-offs`

#### Day 27
- **Sumeet:** `scripts/setup_git_branches.py` -> `chore(git): create automated git branch initialization script`
- **Janvi:** `data/synthesis/references.bib` -> `docs(bib): verify BibTeX reference citations formatting`
- **Sanskar:** `dashboard/app.py` -> `style(dashboard): refine custom css styling, badges, and responsive layout`

#### Day 28
- **Sumeet:** `tests/test_sandbox_security.py` -> `test(sandbox): add path traversal and DoS termination test assertions`
- **Janvi:** `data/cache/` -> `chore(cache): prune temporary cache artifacts and verify json integrity`
- **Sanskar:** `data/synthesis/scientific_discovery_paper.tex` -> `docs(paper): verify mathematical formulas and LaTeX table rendering`

---

### 📅 FINAL STRETCH (Days 29–30): End-to-End Audits, Final Report & Release

#### Day 29
- **Sumeet:** `RESEARCH_AND_ARCHITECTURE_REPORT.md` (Sections 1-3) -> `docs(report): compile problem statement, architecture, and math proofs`
- **Janvi:** `RESEARCH_AND_ARCHITECTURE_REPORT.md` (Section 4) -> `docs(report): document empirical results and vector store telemetry`
- **Sanskar:** `RESEARCH_AND_ARCHITECTURE_REPORT.md` (Section 5) -> `docs(report): compile statistical critic findings and benchmark grades`

#### Day 30 (Final Review Delivery & Merge Day)
- **Sumeet:** `RESEARCH_AND_ARCHITECTURE_REPORT.md` -> `docs(deliverable): finalize research & architecture report for evaluation`
- **Janvi:** `README.md` -> `docs(readme): update comprehensive quickstart and deployment guide`
- **Sanskar:** `data/synthesis/scientific_discovery_paper.tex` -> `docs(paper): export final verified research manuscript and citations`
- **Team Lead Merge (Sumeet):** `main` -> `merge: integrate all 30 days of feature branches into main for final review`

---

## 3. Daily Git Commands for Each Member (Windows / PowerShell)

### Morning Routine:
```powershell
# 1. Switch to your personal branch
git checkout <your-branch>

# 2. Get latest updates merged into main
git pull origin main
```

### Evening Routine (Commit & Push):
```powershell
# 1. Check your modified files
git status

# 2. Stage your files
git add .

# 3. Commit with the day's message
git commit -m "feat(...): your daily task message"

# 4. Push to your branch on GitHub
git push origin <your-branch>
```

### Review Day Merge Routine (By Sumeet):
```powershell
git checkout main
git pull origin main

git merge sumeet/orchestrator-sandbox-rl --no-ff -m "merge: integrate Sumeet's orchestration and sandbox modules"
git merge janvi/ingestion-rag-multimodal --no-ff -m "merge: integrate Janvi's ingestion and RAG modules"
git merge sanskar/critic-synthesis-dashboard --no-ff -m "merge: integrate Sanskar's critic and dashboard modules"

git push origin main
```
