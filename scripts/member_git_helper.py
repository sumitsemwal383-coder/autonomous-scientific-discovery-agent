"""
Interactive VS Code Member Git Helper
Provides instant guidance, daily commit messages, and automated branch staging
for Sumeet, Janvi, and Sanskar across the 30-day Zaalima Development schedule.
"""
import argparse
import subprocess
import sys
from pathlib import Path

SCHEDULE = {
    1: {
        "sumeet": ("config/settings.py", "feat(core): initialize system paths and security thresholds"),
        "janvi": ("config/agent_config.yaml", "chore(config): define declarative agent role schemas"),
        "sanskar": ("tests/test_critic_agent.py", "test(critic): create test harness skeleton for statistical critic")
    },
    2: {
        "sumeet": ("src/agents/base_agent.py", "feat(agents): implement abstract base agent lifecycle"),
        "janvi": ("src/ingestion/arxiv_pipeline.py", "feat(ingestion): implement arxiv atom api search query builder"),
        "sanskar": ("src/agents/critic_agent.py", "feat(critic): initialize critic agent with alpha=0.05 threshold")
    },
    3: {
        "sumeet": ("src/sandbox/execution_result.py", "feat(sandbox): create ExecutionResult dataclass with security metrics"),
        "janvi": ("src/ingestion/arxiv_pipeline.py", "feat(ingestion): parse atom xml entries and extract preprint metadata"),
        "sanskar": ("src/agents/critic_agent.py", "feat(critic): implement two-tailed students t-test calculation")
    },
    4: {
        "sumeet": ("src/sandbox/secure_sandbox.py", "feat(sandbox): build ast security visitor blocking unauthorized modules"),
        "janvi": ("src/ingestion/arxiv_pipeline.py", "feat(ingestion): implement local disk caching and fallback preprints"),
        "sanskar": ("src/agents/critic_agent.py", "feat(critic): add standardized cohens d effect size calculation")
    },
    5: {
        "sumeet": ("src/sandbox/secure_sandbox.py", "feat(sandbox): implement AST interception of eval, exec, and compile"),
        "janvi": ("tests/test_ingestion.py", "test(ingestion): create unit tests for arxiv preprint ingestion"),
        "sanskar": ("src/agents/critic_agent.py", "feat(critic): compute 95 percent confidence intervals for gains")
    },
    6: {
        "sumeet": ("src/sandbox/secure_sandbox.py", "feat(sandbox): detect reflective sandbox breakouts on __subclasses__"),
        "janvi": ("src/ingestion/pubmed_pipeline.py", "feat(ingestion): implement ncbi entrez esearch for biomedical papers"),
        "sanskar": ("src/agents/critic_agent.py", "feat(critic): implement statistical power estimation guarding beta error")
    },
    7: {
        "sumeet": ("tests/test_sandbox_security.py", "test(sandbox): write tests verifying os and subprocess breakout blocks"),
        "janvi": ("src/ingestion/pubmed_pipeline.py", "feat(ingestion): parse pubmed esummary records and extract abstracts"),
        "sanskar": ("tests/test_critic_agent.py", "test(critic): add test cases validating p-value and effect size assertions")
    },
    8: {
        "sumeet": ("src/sandbox/secure_sandbox.py", "feat(sandbox): add isolated subprocess runner with 30s timeout"),
        "janvi": ("src/rag/embeddings.py", "feat(rag): implement dense semantic embedding generator"),
        "sanskar": ("src/memory/context_manager.py", "feat(memory): implement episodic context manager with token estimator")
    },
    9: {
        "sumeet": ("docker/Dockerfile.sandbox", "feat(docker): write hardened minimal dockerfile with non-root user"),
        "janvi": ("src/rag/vector_db.py", "feat(rag): construct disk-persisted vector store with cosine similarity"),
        "sanskar": ("src/memory/context_manager.py", "feat(memory): implement sliding window history retention logic")
    },
    10: {
        "sumeet": ("docker/docker-compose.yml", "feat(docker): configure compose services with cap-drop ALL"),
        "janvi": ("src/rag/vector_db.py", "feat(rag): implement milvus and pinecone enterprise protocol adapters"),
        "sanskar": ("src/memory/context_manager.py", "feat(memory): add milestone summarizer to compress aging episodes")
    },
    11: {
        "sumeet": ("src/sandbox/docker_sandbox.py", "feat(sandbox): build docker sandbox runner with hardened fallback"),
        "janvi": ("src/rag/retriever.py", "feat(rag): implement literature retriever formatting grounded context"),
        "sanskar": ("src/synthesis/templates/research_paper.tex.jinja", "feat(synthesis): construct academic latex manuscript jinja template")
    },
    12: {
        "sumeet": ("src/rl/reward_model.py", "feat(rl): implement discovery reward model with security penalty"),
        "janvi": ("src/rag/retriever.py", "feat(rag): implement citation provenance verification against papers"),
        "sanskar": ("src/synthesis/templates/research_paper.tex.jinja", "feat(synthesis): add latex table generator for statistical results")
    },
    13: {
        "sumeet": ("src/rl/feedback_loop.py", "feat(rl): implement diagnostic stack trace parser for runtime errors"),
        "janvi": ("src/agents/hypothesis_generator.py", "feat(hypothesis): ground hypothesis generation in peer citations via RAG"),
        "sanskar": ("src/synthesis/latex_generator.py", "feat(synthesis): build automated bibtex bibliography compiler")
    },
    14: {
        "sumeet": ("src/rl/feedback_loop.py", "feat(rl): generate actionable verbal reflexions to guide code rewrites"),
        "janvi": ("src/agents/literature_reviewer.py", "feat(agents): connect literature reviewer to vector db indexing"),
        "sanskar": ("docs/WORK_DISTRIBUTION.md", "docs(compliance): formalize team work distribution for mid-review audit")
    },
    15: {
        "sumeet": ("src/agents/code_executor_agent.py", "feat(code_exec): build code executor synthesizing experiment scripts"),
        "janvi": ("src/ingestion/multimodal_parser.py", "feat(multimodal): build visual figure classifier for research pdfs"),
        "sanskar": ("src/synthesis/latex_generator.py", "feat(synthesis): build full latex manuscript compiler with error checks")
    },
    16: {
        "sumeet": ("src/agents/code_executor_agent.py", "feat(code_exec): add structured metric extraction hook"),
        "janvi": ("src/ingestion/multimodal_parser.py", "feat(multimodal): extract quantitative trendlines from pdf loss curves"),
        "sanskar": ("tests/test_synthesis.py", "test(synthesis): create test suite validating latex syntax and bibtex")
    },
    17: {
        "sumeet": ("src/agents/code_executor_agent.py", "feat(code_exec): wire closed-loop reflexion feedback into executor"),
        "janvi": ("src/ingestion/multimodal_parser.py", "feat(multimodal): parse comparative bar charts and extract confidence bounds"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): initialize streamlit supervisor console layout")
    },
    18: {
        "sumeet": ("src/agents/orchestrator.py", "feat(orchestrator): assemble multi-agent state graph transitions"),
        "janvi": ("src/ingestion/multimodal_parser.py", "feat(multimodal): synthesize visual evidence into structured text chunks"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): add interactive logic tree state machine visualizer")
    },
    19: {
        "sumeet": ("src/agents/orchestrator.py", "feat(orchestrator): connect sandbox execution and critic states"),
        "janvi": ("data/cache/", "chore(data): populate offline preprint cache for resilient discovery"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): build literature knowledge base explorer and citation viewer")
    },
    20: {
        "sumeet": ("tests/test_orchestrator.py", "test(orchestrator): create end-to-end multi-agent discovery cycle test"),
        "janvi": ("data/vector_store/", "test(rag): verify vector database persistence and top-k ranking"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): build sandbox execution telemetry and code inspector tab")
    },
    21: {
        "sumeet": ("tests/test_orchestrator.py", "test(rl): validate autonomous code repair across 2 debug iterations"),
        "janvi": ("src/ingestion/multimodal_parser.py", "feat(ingestion): wire multimodal visual evidence into vector store"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): add empirical distribution charts and critic metric cards")
    },
    22: {
        "sumeet": ("scripts/run_pipeline.py", "feat(cli): build command-line discovery runner with simulation flags"),
        "janvi": ("data/holdout_papers/benchmark_ground_truth.json", "data(benchmarks): compile gold standard human research reference set"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): add latex manuscript preview and one-click download")
    },
    23: {
        "sumeet": ("scripts/run_security_audit.py", "test(security): add automated penetration testing script with 8 attack payloads"),
        "janvi": ("src/evaluation/benchmark_evaluator.py", "feat(eval): compute grounding and literature attribution scores"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): integrate real-time token tracking and cost analytics")
    },
    24: {
        "sumeet": (".github/workflows/agent-ci.yml", "ci: configure automated github actions test pipeline for pull requests"),
        "janvi": ("src/evaluation/benchmark_evaluator.py", "feat(eval): implement statistical rigor scoring against human holdout"),
        "sanskar": ("src/evaluation/benchmark_evaluator.py", "feat(eval): implement overall quality scoring and grade calculation")
    },
    25: {
        "sumeet": (".github/workflows/sandbox-security-test.yml", "ci: add nightly sandbox penetration testing security workflow"),
        "janvi": ("src/evaluation/benchmark_evaluator.py", "test(eval): add test cases validating holdout benchmark evaluation"),
        "sanskar": ("dashboard/app.py", "feat(dashboard): add holdout benchmark grading tab with radar dimensions")
    },
    26: {
        "sumeet": ("docs/ARCHITECTURE.md", "docs(arch): detail multi-agent topology, sandbox model, and dataflows"),
        "janvi": ("docs/SOP_COMPLIANCE.md", "docs(compliance): document week-by-week zaalima sop compliance proof"),
        "sanskar": ("docs/WORK_DISTRIBUTION.md", "docs(compliance): finalize team work distribution and role sign-offs")
    },
    27: {
        "sumeet": ("scripts/setup_git_branches.py", "chore(git): create automated git branch initialization script"),
        "janvi": ("data/synthesis/references.bib", "docs(bib): verify BibTeX reference citations formatting"),
        "sanskar": ("dashboard/app.py", "style(dashboard): refine custom css styling, badges, and layout")
    },
    28: {
        "sumeet": ("tests/test_sandbox_security.py", "test(sandbox): add path traversal and DoS termination test assertions"),
        "janvi": ("data/cache/", "chore(cache): prune temporary cache artifacts and verify json integrity"),
        "sanskar": ("data/synthesis/scientific_discovery_paper.tex", "docs(paper): verify mathematical formulas and LaTeX table rendering")
    },
    29: {
        "sumeet": ("RESEARCH_AND_ARCHITECTURE_REPORT.md", "docs(report): compile problem statement, architecture, and math proofs"),
        "janvi": ("RESEARCH_AND_ARCHITECTURE_REPORT.md", "docs(report): document empirical results and vector store telemetry"),
        "sanskar": ("RESEARCH_AND_ARCHITECTURE_REPORT.md", "docs(report): compile statistical critic findings and benchmark grades")
    },
    30: {
        "sumeet": ("RESEARCH_AND_ARCHITECTURE_REPORT.md", "docs(deliverable): finalize research & architecture report for evaluation"),
        "janvi": ("README.md", "docs(readme): update comprehensive quickstart and deployment guide"),
        "sanskar": ("data/synthesis/scientific_discovery_paper.tex", "docs(paper): export final verified research manuscript and citations")
    }
}

BRANCHES = {
    "sumeet": "sumeet/orchestrator-sandbox-rl",
    "janvi": "janvi/ingestion-rag-multimodal",
    "sanskar": "sanskar/critic-synthesis-dashboard"
}

def main():
    parser = argparse.ArgumentParser(description="Zaalima VS Code Member Git Helper")
    parser.add_argument("--member", type=str, choices=["sumeet", "janvi", "sanskar"], required=True, help="Team member name")
    parser.add_argument("--day", type=int, choices=range(1, 31), default=1, help="Schedule day (1 to 30)")
    parser.add_argument("--auto-commit", action="store_true", help="Stage files and commit directly")
    args = parser.parse_args()

    member = args.member.lower()
    day = args.day
    branch = BRANCHES[member]
    day_info = SCHEDULE[day][member]
    target_files, commit_msg = day_info

    print("\n" + "="*75)
    print(f"  ZAALIMA DEV GIT HELPER | MEMBER: {member.upper()} | DAY {day} / 30")
    print("="*75)
    print(f"[*] Dedicated Branch:  {branch}")
    print(f"[*] Assigned Target:   {target_files}")
    print(f"[*] Commit Message:    \"{commit_msg}\"")
    print("-" * 75)
    print("\n[>] Step-by-Step Terminal Commands for Today:")
    print(f"    1. git checkout {branch}")
    print(f"    2. git pull origin main")
    print(f"    3. git add {target_files}")
    print(f"    4. git commit -m \"{commit_msg}\"")
    print(f"    5. git push origin {branch}\n")
    print("="*75)

    if args.auto_commit:
        print("\n[*] Executing automated git staging and commit...")
        subprocess.run(["git", "checkout", branch])
        subprocess.run(["git", "add", target_files])
        res = subprocess.run(["git", "commit", "-m", commit_msg])
        if res.returncode == 0:
            print("[+] Successfully committed for Day", day)
        else:
            print("[!] Git commit returned non-zero code.")

if __name__ == "__main__":
    main()
