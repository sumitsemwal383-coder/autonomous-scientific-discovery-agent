# System Architecture Specification

## Autonomous Multimodal Scientific Discovery Agent
**Zaalima Development Pvt. Ltd. — Enterprise Project 1**

---

### 1. Executive Architectural Overview

The Autonomous Multimodal Scientific Discovery Agent is an enterprise-grade AI system designed to conduct self-directed empirical research. The architecture synthesizes:
1. **Multi-Agent Orchestration**: Specialized autonomous roles collaborating across a blackboard state graph.
2. **Retrieval-Augmented Generation (RAG)**: Dense vector indexing over ArXiv preprints and PubMed articles.
3. **AST-Hardened Execution Sandbox**: Strict static code analysis and isolated execution to actively prevent system breakouts.
4. **Verbal Reinforcement Learning (Reflexion)**: Multi-objective self-debugging feedback loop to repair code execution failures without human intervention.
5. **Statistical Critic Regularization**: Formal hypothesis testing verifying $p$-values ($p < 0.05$), 95% Confidence Intervals, Cohen's $d$ effect sizes, and sample size power.
6. **Academic LaTeX Synthesis**: Automated generation of publication-ready scientific manuscripts and BibTeX bibliographies.

---

### 2. Multi-Agent Topology & State Graph

```
       +---------------------------------------------+
       |             ArXiv & PubMed APIs             |
       +---------------------------------------------+
                              |
                              v
       +---------------------------------------------+
       |          Literature Reviewer Agent          |
       |  (Extracts abstracts, state of art & gaps)  |
       +---------------------------------------------+
                              |
                              v
       +---------------------------------------------+
       |         Multimodal Vision Ingestor          |
       |    (Parses PDF figures, charts & trends)    |
       +---------------------------------------------+
                              |
                              v
       +---------------------------------------------+
       |         Hypothesis Generator Agent          |
       |  (Formulates testable H0/H1 grounded in RAG)|
       +---------------------------------------------+
                              |
                              v
       +---------------------------------------------+
       |            Sandbox Code Executor            |<-----------+
       |     (Generates Python experimental code)    |            |
       +---------------------------------------------+            |
                              |                                   |
                              v                                   |
                  +-----------------------+                       |
                  | AST Security Auditor  |                       |
                  | (Blocks jailbreaks)   |                       |
                  +-----------------------+                       |
                              |                                   |
                    Pass      v       Fail                        |
             +----------------+----------------+                  |
             |                                 |                  |
             v                                 v                  |
   +--------------------+          +-----------------------+      |
   | Isolated Execution |          | RL Self-Debugging     |------+
   | (Runtime Subproc)  |          | Feedback Loop         | (Reflexion)
   +--------------------+          +-----------------------+
             |
             v
   +-------------------------------------------------+
   |             Statistical Critic Agent            |
   | (Evaluates p-values, 95% CI, Cohen's d & Power) |
   +-------------------------------------------------+
             |
             v
   +-------------------------------------------------+
   |            Synthesis Engine (LaTeX)             |
   |  (Compiles final paper draft & BibTeX citations)|
   +-------------------------------------------------+
```

---

### 3. Core Agent Role Specifications

| Agent Role | Primary Responsibilities | Input Artifacts | Output Artifacts |
|---|---|---|---|
| **Literature Reviewer** | Scrapes ArXiv & PubMed APIs, updates dense vector store | Research topic query, domain filter | Normalized paper metadata, indexed vector embeddings, research gap statement |
| **Multimodal Parser** | Parses PDF charts, loss curves, and empirical distribution figures | PDF images, figure captions | Quantitative trend lines, axes calibrations, visual evidence points |
| **Hypothesis Generator** | Formulates novel, falsifiable scientific hypotheses strictly grounded via RAG | Retrieved paper citations, domain gap | Structured hypothesis ($H_0, H_1$), independent/dependent variables, design protocol |
| **Code Executor** | Generates validation scripts, oversees sandboxed execution | Structured hypothesis, experimental parameters | Python verification script, telemetry metrics, stdout/stderr |
| **Statistical Critic** | Evaluates empirical rigor and statistical significance | Raw experimental metrics ($t, p, d, CI$) | Formal verdict (`CONFIRMED` / `REJECTED`), power audit, academic critique |
| **Synthesis Engine** | Produces publication-ready manuscripts | Validated hypothesis, metrics, critique, BibTeX | LaTeX `.tex` manuscript, `.bib` bibliography, rendered markdown |

---

### 4. Sandbox Security & Breakout Defense

The Code Execution Sandbox adopts a defense-in-depth model:
- **AST Static Analysis**: Code is inspected prior to execution using Python's `ast` module. Any access to `os`, `subprocess`, `sys`, `socket`, `ctypes`, dynamic code evaluation (`eval`, `exec`), or reflective attributes (`__subclasses__`, `__bases__`, `__globals__`) triggers immediate termination and a security penalty.
- **Resource Limits**: Strict 30-second execution timeouts and memory quotas (512 MB).
- **Execution Isolation**: Runs within ephemeral temporary directories or hardened Docker containers (`--network none`, `--cap-drop ALL`, read-only root).

---

### 5. Reinforcement Learning Feedback Loop

When experimental code encounters syntax errors, runtime exceptions, or sandbox violations, the system initiates an automated Reflexion cycle:
$$R_{total} = w_1 R_{syn} + w_2 R_{exec} + w_3 R_{stat} + w_4 R_{novelty}$$
1. The error trace is diagnosed by `SelfDebuggingFeedbackLoop`.
2. Actionable linguistic feedback is constructed explaining the root cause and prescriptive fix.
3. The Code Executor regenerates the script using verbal reflection memory.
4. Up to 4 iterative refinement cycles are executed until convergence.
