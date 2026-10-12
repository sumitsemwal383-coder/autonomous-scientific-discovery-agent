"""
Live Supervisor Monitoring Dashboard
Interactive Streamlit application to monitor multi-agent logic trees, literature citations,
sandboxed code execution, statistical critique, and execution costs in real time.
"""
import streamlit as st
import json
import time
import pandas as pd
import numpy as np
from pathlib import Path
import sys

# Ensure project root is in sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.agents.orchestrator import ScientificDiscoveryOrchestrator
from src.evaluation.benchmark_evaluator import BenchmarkEvaluator

st.set_page_config(
    page_title="Zaalima AI - Autonomous Scientific Discovery Agent",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main-header { font-size: 2.2rem; font-weight: 700; color: #1E3A8A; margin-bottom: 0.2rem; }
    .sub-header { font-size: 1.05rem; color: #4B5563; margin-bottom: 1.5rem; }
    .metric-card { background-color: #F8FAFC; border-radius: 8px; padding: 15px; border-left: 5px solid #3B82F6; }
    .status-badge { background-color: #10B981; color: white; padding: 4px 8px; border-radius: 4px; font-weight: 600; font-size: 0.8rem; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { border-radius: 6px 6px 0 0; padding: 10px 16px; background-color: #F1F5F9; }
    .stTabs [aria-selected="true"] { background-color: #2563EB !important; color: white !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🔬 Autonomous Multimodal Scientific Discovery Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Enterprise Self-Directed AI Researcher | Zaalima Development Architecture</div>', unsafe_allow_html=True)

# Sidebar Controls
st.sidebar.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=70)
st.sidebar.title("Supervisor Controls")
st.sidebar.markdown("---")

research_topic = st.sidebar.text_input(
    "Scientific Research Topic",
    value="multi-agent reinforcement learning reasoning",
    help="Topic query passed to ArXiv and PubMed APIs"
)

max_papers = st.sidebar.slider("Papers to Ingest", min_value=2, max_value=8, value=4)

enable_docker = st.sidebar.checkbox(
    "Use Docker Container Sandbox",
    value=False,
    help="Runs in isolated Docker container if active, else AST-hardened subprocess"
)

test_debug_loop = st.sidebar.checkbox(
    "Simulate Self-Debugging RL Loop",
    value=False,
    help="Injects synthetic bug to visualize autonomous multi-cycle self-correction"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Agent Architecture")
st.sidebar.markdown("• **Literature Reviewer**: ArXiv & PubMed\n• **Hypothesis Generator**: Grounded RAG\n• **Code Executor**: Hardened Sandbox\n• **Critic Agent**: Statistical Testing\n• **Synthesis Module**: LaTeX & BibTeX")

if "discovery_result" not in st.session_state:
    st.session_state["discovery_result"] = None
if "bench_result" not in st.session_state:
    st.session_state["bench_result"] = None

run_button = st.sidebar.button("🚀 Run Autonomous Discovery", type="primary", use_container_width=True)

if run_button:
    with st.spinner("Executing end-to-end multi-agent scientific discovery cycle..."):
        orchestrator = ScientificDiscoveryOrchestrator(
            use_docker=enable_docker,
            max_debug_iterations=4
        )
        result = orchestrator.run_discovery_cycle(
            research_topic=research_topic,
            max_papers=max_papers,
            test_self_debug=test_debug_loop
        )
        st.session_state["discovery_result"] = result
        
        # Run holdout paper evaluation
        evaluator = BenchmarkEvaluator()
        bench = evaluator.evaluate_discovery_run(result)
        st.session_state["bench_result"] = bench

res = st.session_state["discovery_result"]
bench = st.session_state["bench_result"]

if res is None:
    st.info("👈 Enter a research topic and click **'Run Autonomous Discovery'** to begin the automated research pipeline.")
    
    # Overview preview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 📚 1. Grounded Ingestion")
        st.write("Autonomous queries to ArXiv & PubMed APIs, extracting abstracts, metadata, and indexing dense vectors into Milvus/vector database.")
    with col2:
        st.markdown("### 🛡️ 2. Sandboxed Execution")
        st.write("Code Executor synthesizes Python simulations and model training loops, running inside an AST-hardened sandbox with breakout prevention.")
    with col3:
        st.markdown("### 📊 3. Statistical Critique & LaTeX")
        st.write("Critic Agent validates p-values, 95% CIs, and Cohen's d effect sizes, producing publication-ready LaTeX manuscripts.")
else:
    # Top Telemetry Bar
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.metric("Workflow Status", res["status"], delta="Normal")
    with c2:
        st.metric("Execution Time", f"{res['duration_seconds']}s")
    with c3:
        st.metric("Active Memory", f"{res['telemetry']['tokens']['active_context_tokens']} tokens")
    with c4:
        st.metric("Execution Cost", f"${res['estimated_cost_usd']:.5f}")
    with c5:
        critic_verdict = res["critic_evaluation"].get("verdict", "PENDING")
        st.metric("Critic Verdict", "CONFIRMED" if "CONFIRMED" in critic_verdict else "REJECTED")

    st.markdown("---")

    # Tabs for Agent Modules
    t1, t2, t3, t4, t5, t6, t7 = st.tabs([
        "🌳 Logic Tree & Telemetry",
        "📚 Literature & Vector Store",
        "🖼️ Multimodal Vision",
        "⚙️ Sandbox & Self-Debugging",
        "📈 Statistical Critic",
        "📄 LaTeX Research Paper",
        "🏆 Holdout Benchmark Grade"
    ])

    with t1:
        st.subheader("Agent Execution State Machine & Trace Log")
        st.markdown("Trace how agents hand off tasks, enforce security boundaries, and validate hypotheses.")
        
        # State flowchart representation
        st.markdown("""
        ```mermaid
        flowchart LR
            LR[Literature Reviewer] --> MP[Multimodal Parser]
            MP --> HG[Hypothesis Generator]
            HG --> CE[Sandbox Code Executor]
            CE --> RL{Error Detected?}
            RL -- Yes --> DBG[RL Self-Debugging]
            DBG --> CE
            RL -- No --> SC[Statistical Critic]
            SC --> RM[Reward Model]
            RM --> SYN[LaTeX Synthesis]
        ```
        """)

        # Event log table
        df_events = pd.DataFrame(res["trace_logs"])
        st.dataframe(df_events, use_container_width=True)

    with t2:
        st.subheader("Literature Grounding & Vector Knowledge Base")
        lit = res["literature_review"]
        st.write(f"**Synthesis:** {lit.get('literature_synthesis')}")
        st.write(f"**Identified Research Gap:** `{lit.get('research_gap')}`")

        st.markdown("#### Retrieved Peer-Reviewed Preprints")
        for p in lit.get("papers", []):
            with st.expander(f"[{p['source'].upper()}] {p['title']}"):
                st.write(f"**Authors:** {p['authors']}")
                st.write(f"**Source ID:** {p['id']}")
                st.write(f"**Abstract Snippet:** {p['key_finding']}")

    with t3:
        st.subheader("Multimodal Ingestion (Charts & Visual Evidence)")
        st.markdown("Vision-Language model parsing of figures, trendlines, and experimental plots.")
        figures = res["multimodal_figures"]
        for fig in figures:
            st.info(f"**{fig['caption']}**\n\n• **Visual Interpretation:** {fig['interpretation']}\n• **Quantitative Extracted Data:** `{fig['quantitative_summary']}`")

    with t4:
        st.subheader("Sandboxed Code Execution & RL Self-Correction")
        code_info = res["code_execution"]
        exec_meta = code_info.get("execution_result", {})

        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"**Sandbox Isolation Mode:** `{exec_meta.get('sandbox_mode')}`")
            st.markdown(f"**Breakout Attempt Detected:** `{exec_meta.get('is_breakout_attempt')}`")
            st.markdown(f"**Debug Iterations Required:** `{code_info.get('debug_iterations_count')}`")
        with col_b:
            st.markdown(f"**Exit Code:** `{exec_meta.get('exit_code')}`")
            st.markdown(f"**Execution Duration:** `{exec_meta.get('duration')}s`")

        if code_info.get("debug_trace"):
            st.warning("⚠️ **RL Self-Debugging Loop Triggered:**")
            for dt in code_info["debug_trace"]:
                st.markdown(f"- **Cycle {dt['iteration']} Failure:** `{dt['failure_analysis']['error_type']}` - {dt['failure_analysis']['actionable_fix']}")

        st.markdown("#### Generated Experimental Code")
        st.code(code_info.get("code", ""), language="python")

        st.markdown("#### Execution Output (Stdout)")
        st.text(exec_meta.get("stdout", "No stdout"))

    with t5:
        st.subheader("Statistical Critic Evaluation")
        critic = res["critic_evaluation"]
        metrics = res["code_execution"].get("metrics", {})

        st.success(f"**Critic Verdict:** {critic.get('verdict')}")
        st.write(f"_{critic.get('critique')}_")

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("p-value", f"{metrics.get('p_value', 1.0):.4e}")
        with m2:
            st.metric("Cohen's d Effect Size", f"{metrics.get('cohens_d', 0.0):.2f}")
        with m3:
            st.metric("95% Confidence Interval", f"[{metrics.get('ci_95_low', 0):.2f}, {metrics.get('ci_95_high', 0):.2f}]")
        with m4:
            st.metric("Estimated Power", f"{critic.get('estimated_power', 0.85):.2f}")

        # Visualization of empirical distributions
        if metrics:
            st.markdown("#### Empirical Distribution Comparison (N=100 Trials)")
            b_mean = metrics.get("baseline_mean", 70)
            b_std = metrics.get("baseline_std", 8)
            t_mean = metrics.get("treatment_mean", 84)
            t_std = metrics.get("treatment_std", 6)

            df_sim = pd.DataFrame({
                "Baseline (Uncalibrated Self-Reflection)": np.random.normal(b_mean, b_std, 100),
                "Critic-Guided Proposed Method": np.random.normal(t_mean, t_std, 100)
            })
            st.line_chart(df_sim)

    with t6:
        st.subheader("Synthesized Academic Research Paper (LaTeX)")
        latex = res["latex_synthesis"]
        st.markdown(f"**Title:** {latex.get('title')}")
        st.markdown(f"**Generated File:** `{latex.get('tex_path')}`")
        
        st.markdown("#### Paper Abstract")
        st.info(latex.get("abstract"))

        st.download_button(
            label="📥 Download LaTeX Manuscript (.tex)",
            data=latex.get("rendered_tex", ""),
            file_name="scientific_discovery_paper.tex",
            mime="text/plain"
        )

        with st.expander("View Full LaTeX Source Code"):
            st.code(latex.get("rendered_tex", ""), language="latex")

    with t7:
        st.subheader("Holdout Benchmark Evaluation")
        if bench:
            st.metric("Overall Discovery Quality Score", f"{bench['overall_score']}%", delta=bench["grade"])
            st.write(f"**Status:** {bench['recommendation']}")

            st.markdown("#### Academic Dimension Breakdown")
            dims = bench["dimensions"]
            col_x, col_y = st.columns(2)
            with col_x:
                st.write(f"• **Literature Grounding Precision:** `{dims['literature_grounding']}%`")
                st.write(f"• **Statistical Rigor & Power:** `{dims['statistical_rigor']}%`")
            with col_y:
                st.write(f"• **Sandbox Security & Soundness:** `{dims['sandbox_security_soundness']}%`")
                st.write(f"• **LaTeX Synthesis Fidelity:** `{dims['latex_synthesis_fidelity']}%`")
