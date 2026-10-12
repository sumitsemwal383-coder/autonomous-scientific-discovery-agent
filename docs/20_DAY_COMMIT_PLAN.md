# Zaalima Development Pvt. Ltd. — 20-Day Git Commit Strategy & Roadmap
**Project 1: Autonomous Multimodal Scientific Discovery Agent**  
**Team Roster (3 Members):**
- **Sumeet** (Team Lead | Multi-Agent Orchestrator, Sandbox Security & RL Self-Debugging)
- **Janvi** (Data Engineer | ArXiv/PubMed Ingestion, Dense RAG Vector Store & Multimodal Vision)
- **Sanskar** (ML & UI Specialist | Statistical Critic Agent, LaTeX Synthesis & Streamlit Dashboard)

---

## 1. Zaalima SOP 20-Day Commit Rule Explained

Under **Zaalima Development SOP Version 1.1 (Section 3.2 & Section 9)**:
1. **The 20-Day Requirement**: In the 20 days leading to the Final Review, the shared team repository must show commit activity on **at least 20 distinct days**. No gaps are permitted.
2. **Branch Isolation**: Each member must maintain their **own individual feature branch** (`sumeet/...`, `janvi/...`, `sanskar/...`) and commit directly to it.
3. **Collective Team Metric**: Commit activity on any member's branch counts toward the shared repository's daily streak, but all 3 members must show steady individual contributions to receive evaluation clearance.
4. **Merge Protocol**: Individual branches are reviewed and merged periodically into `main` by Team Lead (Sumeet) using non-fast-forward merges (`git merge --no-ff`).

---

## 2. Team Role & Module Allocation

```
+----------------------------------------------------------------------------------------------------+
|                                    PROJECT 1 MODULE ALLOCATION                                     |
+----------------------------------------------------------------------------------------------------+
  SUMEET (Branch: sumeet/orchestrator-sandbox-rl)
  ├── Multi-Agent State Machine Orchestrator (src/agents/orchestrator.py, base_agent.py)
  ├── AST Static Security Sandbox & Breakout Interceptor (src/sandbox/secure_sandbox.py)
  ├── Docker Container Runner & Compose Environment (docker/Dockerfile.sandbox, docker-compose.yml)
  └── Verbal RL Self-Debugging Feedback Loop (src/rl/feedback_loop.py, reward_model.py)

  JANVI (Branch: janvi/ingestion-rag-multimodal)
  ├── ArXiv Atom API Scraper & Parser (src/ingestion/arxiv_pipeline.py)
  ├── NCBI PubMed E-Utilities Ingestion Engine (src/ingestion/pubmed_pipeline.py)
  ├── Dense Semantic Vector Store & Milvus/Pinecone Adapters (src/rag/vector_db.py, embeddings.py)
  ├── Literature Grounding Retriever for RAG (src/rag/retriever.py)
  └── Multimodal PDF Chart, Graph & Figure Parser (src/ingestion/multimodal_parser.py)

  SANSKAR (Branch: sanskar/critic-synthesis-dashboard)
  ├── Empirical Statistical Critic Agent (src/agents/critic_agent.py: p-values, 95% CIs, Cohen's d)
  ├── Context Window Memory Manager (src/memory/context_manager.py)
  ├── Academic LaTeX Paper & BibTeX Generator (src/synthesis/latex_generator.py, templates/)
  ├── Holdout Benchmark Evaluation Roadmap (src/evaluation/benchmark_evaluator.py)
  └── Live Supervisor Monitoring Dashboard (dashboard/app.py)
```

---

## 3. Day-by-Day (Day 1 to Day 20) Commit Calendar

| Day | Primary Contributor | Active Branch | Scope / Task Description | Commit Message (Conventional Commits) |
|:---:|:---:|:---:|---|---|
| **Day 1** | **Sumeet** | `main` & `sumeet/orchestrator-sandbox-rl` | Repository bootstrap, directory structure, config settings, and agent base class | `chore: scaffold project structure and base agent lifecycle` |
| **Day 2** | **Janvi** | `janvi/ingestion-rag-multimodal` | ArXiv API connector, Atom XML parsing, metadata extraction, and local cache | `feat(ingestion): implement arxiv pipeline with atom xml parsing` |
| **Day 3** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Statistical Critic Agent skeleton, p-value thresholds, and confidence interval formulas | `feat(critic): initialize statistical critic agent and alpha thresholds` |
| **Day 4** | **Janvi** | `janvi/ingestion-rag-multimodal` | NCBI PubMed E-utilities connector (esearch & esummary) and biomedical preprint cache | `feat(ingestion): build pubmed entez pipeline with fallback cache` |
| **Day 5** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | AST Security Validator detecting os, subprocess, eval, and reflective breakouts | `feat(sandbox): implement ast static security auditor for breakout prevention` |
| **Day 6** | **Janvi** | `janvi/ingestion-rag-multimodal` | Dense vector embedding generator with cosine similarity and Milvus/Pinecone adapter | `feat(rag): create dense embedding generator and vector db store` |
| **Day 7** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | Isolated execution runner with 30s timeout and telemetry metric extractor | `feat(sandbox): build hardened execution runner with timeout boundaries` |
| **Day 8** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Effect size calculation (Cohen's d) and statistical power estimation ($\beta \ge 0.80$) | `feat(critic): add cohens d effect size and statistical power estimator` |
| **Day 9** | **Janvi** | `janvi/ingestion-rag-multimodal` | Literature retriever verifying grounding against peer-reviewed citations ([Ref_X]) | `feat(rag): build literature retriever with citation grounding verification` |
| **Day 10** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | Multi-agent state graph orchestrator connecting Reviewer, Hypothesis, and Code Executor | `feat(orchestrator): implement multi-agent workflow state machine` |
| **Mid-Rev** | **Sumeet (Lead)** | `main` (Merge Day) | **Mid-Project Review checkpoint:** Merge all 3 branches into `main` (10 commit days reached) | `merge: integrate week 1 and week 2 features for mid-project review` |
| **Day 11** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | Multi-objective RL reward model penalizing jailbreaks and rewarding statistical significance | `feat(rl): build discovery reward model with security clamping` |
| **Day 12** | **Janvi** | `janvi/ingestion-rag-multimodal` | Multimodal scientific parser extracting quantitative trendlines from PDF charts and loss curves | `feat(multimodal): implement vision-language figure and chart parser` |
| **Day 13** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | Reflexion self-debugging loop translating execution stack traces into code rewrites | `feat(rl): implement verbal reflexion self-debugging feedback loop` |
| **Day 14** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Context window memory manager with sliding window and milestone summarization | `feat(memory): implement hierarchical context window token budget manager` |
| **Day 15** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Jinja2 LaTeX research paper template with tables, hypotheses, and BibTeX generator | `feat(synthesis): construct academic latex paper and bibtex generator` |
| **Day 16** | **Janvi** | `janvi/ingestion-rag-multimodal` | Integration of multimodal figure summaries into the Literature Reviewer pipeline | `feat(ingestion): wire multimodal visual evidence into vector knowledge base` |
| **Day 17** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Interactive Streamlit live supervisor dashboard (Logic tree, Citations, Metrics, LaTeX preview) | `feat(dashboard): build streamlit live monitoring supervisor console` |
| **Day 18** | **Sumeet** | `sumeet/orchestrator-sandbox-rl` | Penetration test suite verifying 100% block rate across 8 adversarial breakout payloads | `test(sandbox): implement automated penetration test and security audit` |
| **Day 19** | **Sanskar** | `sanskar/critic-synthesis-dashboard` | Holdout paper benchmark evaluator grading agent output against human-authored research | `feat(eval): implement benchmark evaluator against human holdout papers` |
| **Day 20** | **All 3 Members** | `main` | Final end-to-end integration test, report generation, and final merge into `main` | `docs: finalize research & architecture report and enterprise release` |

---

## 4. Git Commands Reference for Sumeet, Janvi, and Sanskar

### Step 1: Initial Clone and Branch Setup
Each member runs this on their local machine:
```bash
# Sumeet sets up his branch
git checkout -b sumeet/orchestrator-sandbox-rl

# Janvi sets up her branch
git checkout -b janvi/ingestion-rag-multimodal

# Sanskar sets up his branch
git checkout -b sanskar/critic-synthesis-dashboard
```

### Step 2: Daily Workflow (Run Every Single Day)
```bash
# 1. Pull latest changes from main before starting work
git checkout <your-branch>
git pull origin main

# 2. Complete the assigned task for the day
# (Edit code, add tests, write docs)

# 3. Stage and commit with descriptive conventional commit message
git add .
git commit -m "feat(module): description of today's work"

# 4. Push directly to your dedicated remote branch
git push origin <your-branch>
```

### Step 3: Mid-Review and Final-Review Merge into `main` (By Sumeet, Team Lead)
```bash
# Switch to main
git checkout main
git pull origin main

# Merge individual branches with merge commit preserved
git merge sumeet/orchestrator-sandbox-rl --no-ff -m "merge: integrate Sumeet's orchestration and sandbox modules"
git merge janvi/ingestion-rag-multimodal --no-ff -m "merge: integrate Janvi's ingestion, RAG, and multimodal modules"
git merge sanskar/critic-synthesis-dashboard --no-ff -m "merge: integrate Sanskar's critic, synthesis, and dashboard modules"

# Push updated main to GitHub
git push origin main
```
