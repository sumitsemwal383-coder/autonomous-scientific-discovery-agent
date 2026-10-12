# Complete Step-by-Step Git Commit Guide (20-Day All-Member Protocol)
**Zaalima Development Pvt. Ltd. — Enterprise Project 1**  
**Team Roster:** Sumeet (Team Lead), Janvi, Sanskar  

---

## PART 1: One-Time Local Setup (Each Member Runs Once)

Before making daily commits, each member must configure their Git identity on their own laptop/workstation so GitHub attributes their commits accurately.

### 1.1 Sumeet (Team Lead) Setup
```bash
git config --global user.name "Sumeet"
git config --global user.email "sumeet@example.com"
git checkout -b sumeet/orchestrator-sandbox-rl
git push -u origin sumeet/orchestrator-sandbox-rl
```

### 1.2 Janvi Setup
```bash
git config --global user.name "Janvi"
git config --global user.email "janvi@example.com"
git checkout -b janvi/ingestion-rag-multimodal
git push -u origin janvi/ingestion-rag-multimodal
```

### 1.3 Sanskar Setup
```bash
git config --global user.name "Sanskar"
git config --global user.email "sanskar@example.com"
git checkout -b sanskar/critic-synthesis-dashboard
git push -u origin sanskar/critic-synthesis-dashboard
```

---

## PART 2: The 5-Step Daily Commit Routine (HOW to Commit Every Day)

Every single day from Day 1 to Day 20, **every member** must follow these 5 steps in their terminal (Command Prompt / PowerShell / VS Code Terminal):

```
+-------------------------------------------------------------------------------+
|                       DAILY 5-STEP GIT WORKFLOW                               |
+-------------------------------------------------------------------------------+
  Step 1: git checkout <your-branch> && git pull origin main
  Step 2: Edit your assigned files / write your code
  Step 3: git status (Verify only your changed files are listed)
  Step 4: git add <files> (Stage changes)
  Step 5: git commit -m "feat/fix/test(...): message" && git push origin <branch>
```

### Step 1: Switch to Your Dedicated Branch & Sync
Never commit directly to `main`. Always switch to your branch and sync latest changes:
```bash
git checkout <your-branch-name>
git pull origin main
```

### Step 2: Write or Update Your Assigned Daily Code
Edit or add the files assigned for that day (e.g., adding unit tests, refining an agent function, writing docstrings).

### Step 3: Check What Was Modified
```bash
git status
```
*Tip:* You should see modified or newly created files in red or green.

### Step 4: Stage the Specific Files
You can stage specific files or all modified files:
```bash
# Stage specific files (recommended):
git add src/agents/orchestrator.py tests/test_orchestrator.py

# Or stage all current directory changes:
git add .
```

### Step 5: Commit and Push
```bash
git commit -m "feat(orchestrator): implement state machine transition logic"
git push origin <your-branch-name>
```

---

## PART 3: 20-Day "WHAT to Commit" Master Schedule (All 3 Members Commit Every Day)

Every day from Day 1 to Day 20, all 3 members have distinct tasks and files to commit.

### WEEK 1: Ingestion, Architecture & Baseline Sandbox

#### Day 1
- **Sumeet:**
  - Files: `config/settings.py`, `src/agents/base_agent.py`
  - Commit: `feat(core): initialize base agent interface and execution telemetry`
- **Janvi:**
  - Files: `config/agent_config.yaml`, `src/ingestion/__init__.py`
  - Commit: `chore(config): configure yaml schema for literature ingestion roles`
- **Sanskar:**
  - Files: `tests/__init__.py`, `tests/test_critic_agent.py` (skeleton)
  - Commit: `test(critic): create test harness skeleton for statistical critic`

#### Day 2
- **Sumeet:**
  - Files: `src/sandbox/execution_result.py`
  - Commit: `feat(sandbox): create structured ExecutionResult dataclass`
- **Janvi:**
  - Files: `src/ingestion/arxiv_pipeline.py`
  - Commit: `feat(ingestion): implement arxiv atom api query parser and caching`
- **Sanskar:**
  - Files: `src/agents/critic_agent.py` (Alpha threshold & imports)
  - Commit: `feat(critic): initialize critic agent with alpha=0.05 baseline`

#### Day 3
- **Sumeet:**
  - Files: `src/sandbox/secure_sandbox.py` (AST visitor skeleton)
  - Commit: `feat(sandbox): build ast node visitor for forbidden module detection`
- **Janvi:**
  - Files: `tests/test_ingestion.py`
  - Commit: `test(ingestion): add unit test suite for arxiv preprint parsing`
- **Sanskar:**
  - Files: `src/agents/critic_agent.py` (Two-tailed Student's t-test logic)
  - Commit: `feat(critic): implement paired t-test and p-value calculation`

#### Day 4
- **Sumeet:**
  - Files: `src/sandbox/secure_sandbox.py` (Execution timeout and subprocess isolation)
  - Commit: `feat(sandbox): add subprocess runtime isolation and timeout boundary`
- **Janvi:**
  - Files: `src/ingestion/pubmed_pipeline.py`
  - Commit: `feat(ingestion): build ncbi entrez pubmed esearch and esummary pipeline`
- **Sanskar:**
  - Files: `src/agents/critic_agent.py` (Cohen's d formula)
  - Commit: `feat(critic): implement cohens d effect size magnitude evaluator`

#### Day 5
- **Sumeet:**
  - Files: `tests/test_sandbox_security.py` (Breakout attack tests)
  - Commit: `test(sandbox): add unit tests for os and subprocess breakout blocking`
- **Janvi:**
  - Files: `src/rag/embeddings.py`
  - Commit: `feat(rag): implement dense semantic embedding generator`
- **Sanskar:**
  - Files: `src/agents/critic_agent.py` (95% Confidence Interval calculation)
  - Commit: `feat(critic): compute 95 percent confidence intervals for effect gains`

---

### WEEK 2: RAG Grounding, Breakout Defense & RL Self-Debugging

#### Day 6
- **Sumeet:**
  - Files: `docker/Dockerfile.sandbox`
  - Commit: `feat(docker): build minimal hardened python sandbox container image`
- **Janvi:**
  - Files: `src/rag/vector_db.py` (Cosine similarity & persistence)
  - Commit: `feat(rag): construct persistent vector database with metadata index`
- **Sanskar:**
  - Files: `src/agents/critic_agent.py` (Statistical power calculation)
  - Commit: `feat(critic): add sample size power analysis guarding against beta errors`

#### Day 7
- **Sumeet:**
  - Files: `docker/docker-compose.yml`
  - Commit: `feat(docker): configure compose services with dropped capabilities`
- **Janvi:**
  - Files: `src/rag/vector_db.py` (Milvus & Pinecone adapter classes)
  - Commit: `feat(rag): add enterprise milvus and pinecone client protocol adapters`
- **Sanskar:**
  - Files: `tests/test_critic_agent.py` (Significance verification tests)
  - Commit: `test(critic): add full test assertions for confirmed and rejected verdicts`

#### Day 8
- **Sumeet:**
  - Files: `src/sandbox/docker_sandbox.py`
  - Commit: `feat(sandbox): create containerized docker runner with secure fallback`
- **Janvi:**
  - Files: `src/rag/retriever.py`
  - Commit: `feat(rag): construct literature retriever with provenance citation keys`
- **Sanskar:**
  - Files: `src/memory/context_manager.py` (Token estimation & episodic memory)
  - Commit: `feat(memory): implement episodic context memory and token estimator`

#### Day 9
- **Sumeet:**
  - Files: `src/rl/reward_model.py`
  - Commit: `feat(rl): implement multi-objective discovery reward model`
- **Janvi:**
  - Files: `src/agents/hypothesis_generator.py`
  - Commit: `feat(hypothesis): ground hypothesis generation in retrieved peer literature`
- **Sanskar:**
  - Files: `src/memory/context_manager.py` (Sliding window & compression)
  - Commit: `feat(memory): add sliding window retention and milestone summarizer`

#### Day 10 (Mid-Project Review Checkpoint)
- **Sumeet:**
  - Files: `src/rl/feedback_loop.py`
  - Commit: `feat(rl): implement reflexion self-debugging failure parser`
- **Janvi:**
  - Files: `src/agents/literature_reviewer.py`
  - Commit: `feat(agents): connect literature reviewer to vector db indexing pipeline`
- **Sanskar:**
  - Files: `docs/WORK_DISTRIBUTION.md`
  - Commit: `docs(compliance): formalize team work distribution for mid-review audit`
- **Team Lead Merge (Sumeet):**
  - Commit: `merge: merge mid-project review features into main branch`

---

### WEEK 3: Multimodal Vision, Code Synthesis & Statistical Criticism

#### Day 11
- **Sumeet:**
  - Files: `src/agents/code_executor_agent.py`
  - Commit: `feat(code_exec): build code executor with automated simulation templates`
- **Janvi:**
  - Files: `src/ingestion/multimodal_parser.py` (Chart and figure classifier)
  - Commit: `feat(multimodal): build visual figure classifier for research pdfs`
- **Sanskar:**
  - Files: `src/synthesis/templates/research_paper.tex.jinja` (Structure setup)
  - Commit: `feat(synthesis): construct academic latex paper jinja template`

#### Day 12
- **Sumeet:**
  - Files: `src/agents/code_executor_agent.py` (Wiring RL self-debugging)
  - Commit: `feat(code_exec): integrate closed-loop reflexion feedback into executor`
- **Janvi:**
  - Files: `src/ingestion/multimodal_parser.py` (Trendline extraction)
  - Commit: `feat(multimodal): extract quantitative trendlines and axes data points`
- **Sanskar:**
  - Files: `src/synthesis/templates/research_paper.tex.jinja` (Tables & Math equations)
  - Commit: `feat(synthesis): add latex table generator for statistical critic results`

#### Day 13
- **Sumeet:**
  - Files: `tests/test_orchestrator.py` (Self-debug cycle tests)
  - Commit: `test(rl): validate autonomous code repair across 2 debug iterations`
- **Janvi:**
  - Files: `src/ingestion/multimodal_parser.py` (Summary generator)
  - Commit: `feat(multimodal): synthesize visual evidence into structured text chunks`
- **Sanskar:**
  - Files: `src/synthesis/latex_generator.py` (BibTeX reference builder)
  - Commit: `feat(synthesis): implement automated bibtex citation entry compiler`

#### Day 14
- **Sumeet:**
  - Files: `src/agents/orchestrator.py` (State graph initialization)
  - Commit: `feat(orchestrator): assemble end-to-end multi-agent orchestration graph`
- **Janvi:**
  - Files: `data/cache/` (Preprint cache verification)
  - Commit: `chore(data): populate offline preprint cache for resilient discovery`
- **Sanskar:**
  - Files: `src/synthesis/latex_generator.py` (Document renderer)
  - Commit: `feat(synthesis): build full latex manuscript compiler with error checks`

#### Day 15
- **Sumeet:**
  - Files: `scripts/run_pipeline.py` (CLI options & debug flags)
  - Commit: `feat(cli): build command-line discovery runner with simulation flags`
- **Janvi:**
  - Files: `data/vector_store/` (Indexing persistence tests)
  - Commit: `test(rag): verify vector database persistence and top-k ranking`
- **Sanskar:**
  - Files: `tests/test_synthesis.py`
  - Commit: `test(synthesis): create test suite validating latex syntax and bibtex`

---

### WEEK 4: Streamlit Dashboard, Holdout Grading & Final Review

#### Day 16
- **Sumeet:**
  - Files: `scripts/run_security_audit.py` (8 attack payloads)
  - Commit: `test(security): add penetration testing script with 8 attack payloads`
- **Janvi:**
  - Files: `data/holdout_papers/benchmark_ground_truth.json`
  - Commit: `data(benchmarks): compile gold standard human research reference set`
- **Sanskar:**
  - Files: `dashboard/app.py` (Sidebar controls & tabs layout)
  - Commit: `feat(dashboard): initialize streamlit supervisor console layout`

#### Day 17
- **Sumeet:**
  - Files: `.github/workflows/agent-ci.yml`
  - Commit: `ci: configure automated github actions test pipeline for pull requests`
- **Janvi:**
  - Files: `src/evaluation/benchmark_evaluator.py` (Dimension scorers)
  - Commit: `feat(eval): compute grounding and literature attribution scores`
- **Sanskar:**
  - Files: `dashboard/app.py` (Logic tree & event log visualization)
  - Commit: `feat(dashboard): add interactive logic tree state machine visualizer`

#### Day 18
- **Sumeet:**
  - Files: `.github/workflows/sandbox-security-test.yml`
  - Commit: `ci: add nightly sandbox penetration testing security workflow`
- **Janvi:**
  - Files: `src/evaluation/benchmark_evaluator.py` (Statistical grading)
  - Commit: `feat(eval): implement statistical rigor scoring against human holdout`
- **Sanskar:**
  - Files: `dashboard/app.py` (Empirical distribution charts & LaTeX export button)
  - Commit: `feat(dashboard): add empirical distribution charts and latex download`

#### Day 19
- **Sumeet:**
  - Files: `docs/ARCHITECTURE.md`
  - Commit: `docs(arch): detail multi-agent topology, sandbox model, and dataflows`
- **Janvi:**
  - Files: `docs/SOP_COMPLIANCE.md`
  - Commit: `docs(compliance): document week-by-week zaalima sop compliance proof`
- **Sanskar:**
  - Files: `dashboard/app.py` (Cost estimation & token telemetry cards)
  - Commit: `feat(dashboard): integrate real-time token tracking and cost analytics`

#### Day 20 (Final Review Delivery)
- **Sumeet:**
  - Files: `RESEARCH_AND_ARCHITECTURE_REPORT.md` (Executive systems report)
  - Commit: `docs(deliverable): finalize research & architecture report for evaluation`
- **Janvi:**
  - Files: `README.md` (Quickstart, commands, installation instructions)
  - Commit: `docs(readme): update comprehensive quickstart and deployment guide`
- **Sanskar:**
  - Files: `data/synthesis/scientific_discovery_paper.tex` (Final compiled paper)
  - Commit: `docs(paper): export final verified research manuscript and citations`
- **Team Lead Merge (Sumeet):**
  - Commit: `merge: integrate all week 3 and 4 feature branches into main for final review`

---

## PART 4: Mid-Review & Final-Review Merges (By Sumeet, Team Lead)

On **Day 10 (Mid-Review)** and **Day 20 (Final-Review)**, Sumeet performs the merge from the three branches into `main`:

```bash
# 1. Ensure main is clean and up to date
git checkout main
git pull origin main

# 2. Merge each member's branch preserving commit history (--no-ff)
git merge sumeet/orchestrator-sandbox-rl --no-ff -m "merge: integrate Sumeet's orchestration and sandbox modules"
git merge janvi/ingestion-rag-multimodal --no-ff -m "merge: integrate Janvi's ingestion and RAG modules"
git merge sanskar/critic-synthesis-dashboard --no-ff -m "merge: integrate Sanskar's critic and dashboard modules"

# 3. Push to GitHub
git push origin main
```

---

## PART 5: Pro-Tips to Avoid Disqualification by Zaalima

1. **Commit Every Single Calendar Day (Zero Gaps):**
   Zaalima strictly checks that there are 20 different dates in the commit log. Never do 5 commits on Friday and nothing on the weekend. Space your commits daily!
2. **If Someone is Sick or Away:**
   Under Zaalima Individual Fallback rules, the remaining members must still push commits on that day so the shared repository maintains its daily commit streak.
3. **Use Professional Commit Messages:**
   Always use standard prefixes: `feat:`, `fix:`, `test:`, `docs:`, `refactor:`, `chore:`. Zaalima evaluators read commit messages to evaluate professional collaboration.
4. **Keep Local Branches Synced:**
   Every morning before writing code, run `git pull origin main` to ensure your branch has the latest merged code from your teammates.
