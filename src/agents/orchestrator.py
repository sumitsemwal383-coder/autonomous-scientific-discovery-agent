"""
Multi-Agent Orchestrator for Autonomous Scientific Discovery
Coordinates the end-to-end research workflow across Literature Reviewer, Hypothesis Generator,
Sandbox Code Executor, Statistical Critic, and LaTeX Synthesis Engine.
"""
import time
import logging
from typing import Dict, Any, List, Optional
from pathlib import Path

from src.rag.vector_db import VectorDatabase
from src.rag.retriever import LiteratureRetriever
from src.sandbox.secure_sandbox import SecureSandbox
from src.sandbox.docker_sandbox import DockerSandbox
from src.rl.feedback_loop import SelfDebuggingFeedbackLoop
from src.rl.reward_model import DiscoveryRewardModel
from src.memory.context_manager import ContextMemoryManager
from src.ingestion.multimodal_parser import MultimodalParser
from src.synthesis.latex_generator import LatexPaperGenerator

from .literature_reviewer import LiteratureReviewerAgent
from .hypothesis_generator import HypothesisGeneratorAgent
from .code_executor_agent import CodeExecutorAgent
from .critic_agent import CriticAgent

logger = logging.getLogger(__name__)

class ScientificDiscoveryOrchestrator:
    def __init__(self, use_docker: bool = False, max_debug_iterations: int = 4):
        # 1. Shared Infrastructure
        self.vector_db = VectorDatabase()
        self.retriever = LiteratureRetriever(self.vector_db)
        self.memory = ContextMemoryManager()
        self.multimodal_parser = MultimodalParser()
        self.reward_model = DiscoveryRewardModel()
        self.latex_generator = LatexPaperGenerator()

        # 2. Execution Sandbox
        if use_docker:
            self.sandbox = DockerSandbox()
        else:
            self.sandbox = SecureSandbox()

        # 3. RL Feedback Loop
        self.feedback_loop = SelfDebuggingFeedbackLoop(max_iterations=max_debug_iterations)

        # 4. Specialized Agents
        self.reviewer_agent = LiteratureReviewerAgent(self.vector_db)
        self.hypothesis_agent = HypothesisGeneratorAgent(self.retriever)
        self.code_agent = CodeExecutorAgent(self.sandbox, self.feedback_loop)
        self.critic_agent = CriticAgent()

        # 5. Telemetry and Audit Trail
        self.trace_logs: List[Dict[str, Any]] = []
        self.current_state = "IDLE"

    def run_discovery_cycle(
        self,
        research_topic: str = "multi-agent reinforcement learning reasoning",
        max_papers: int = 4,
        test_self_debug: bool = False
    ) -> Dict[str, Any]:
        """
        Executes an end-to-end autonomous discovery pipeline.
        """
        start_time = time.time()
        self._record_event("ORCHESTRATOR", "WORKFLOW_START", f"Commencing scientific discovery cycle for: '{research_topic}'")

        # Step 1: Literature Review & Ingestion
        self.current_state = "LITERATURE_REVIEW"
        self._record_event("LITERATURE_REVIEWER", "START_INGESTION", "Interrogating ArXiv & PubMed APIs")
        review_res = self.reviewer_agent.execute({
            "research_topic": research_topic,
            "max_papers": max_papers
        })
        self.memory.add_interaction(
            "LiteratureReviewer",
            "INGESTION_COMPLETE",
            review_res.get("literature_synthesis", "")
        )
        self._record_event("LITERATURE_REVIEWER", "INGESTION_COMPLETE", f"Indexed {review_res.get('indexed_count')} papers.")

        # Step 2: Multimodal Asset Ingestion
        self.current_state = "MULTIMODAL_INGESTION"
        self._record_event("MULTIMODAL_PARSER", "PARSE_FIGURES", "Extracting visual trends and empirical plots")
        figures = self.multimodal_parser.extract_paper_multimodal_assets(research_topic)
        self._record_event("MULTIMODAL_PARSER", "FIGURES_EXTRACTED", f"Processed {len(figures)} multimodal evidence figures")

        # Step 3: Grounded Hypothesis Formulation
        self.current_state = "HYPOTHESIS_GENERATION"
        self._record_event("HYPOTHESIS_GENERATOR", "FORMULATE_HYPOTHESIS", "Generating falsifiable hypothesis grounded via RAG")
        hypo_res = self.hypothesis_agent.execute({"research_topic": research_topic})
        hypothesis = hypo_res.get("hypothesis", {})
        self.memory.add_interaction(
            "HypothesisGenerator",
            "HYPOTHESIS_FORMULATED",
            hypothesis.get("statement", "")
        )
        self._record_event("HYPOTHESIS_GENERATOR", "HYPOTHESIS_READY", f"Hypothesis ID: {hypothesis.get('hypothesis_id')}")

        # Step 4: Code Synthesis & Sandboxed Execution with RL Feedback
        self.current_state = "SANDBOX_EXPERIMENTATION"
        self._record_event("CODE_EXECUTOR", "EXECUTE_EXPERIMENT", "Synthesizing Python validation script & executing in sandbox")
        code_res = self.code_agent.execute({
            "hypothesis": hypothesis,
            "test_self_debug": test_self_debug
        })
        self._record_event(
            "CODE_EXECUTOR",
            "EXECUTION_FINISHED",
            f"Exit status: {code_res.get('status')} across {code_res.get('debug_iterations_count')} iteration(s)"
        )

        # Step 5: Statistical Critic Evaluation
        self.current_state = "STATISTICAL_CRITIC"
        self._record_event("STATISTICAL_CRITIC", "EVALUATE_METRICS", "Performing hypothesis testing, p-value & CI analysis")
        critic_res = self.critic_agent.execute({
            "metrics": code_res.get("metrics", {}),
            "hypothesis": hypothesis
        })
        self.memory.add_interaction(
            "CriticAgent",
            "VERDICT_RENDERED",
            critic_res.get("critique", "")
        )
        self._record_event("STATISTICAL_CRITIC", "VERDICT", f"Verdict: {critic_res.get('verdict')}")

        # Step 6: Reinforcement Learning Reward Computation
        self.current_state = "RL_REWARD_COMPUTATION"
        exec_info = code_res.get("execution_result", {})
        reward_info = self.reward_model.compute_reward(
            syntax_valid=code_res.get("status") == "SUCCESS",
            execution_success=code_res.get("status") == "SUCCESS",
            is_breakout=exec_info.get("is_breakout_attempt", False),
            statistical_significance=critic_res.get("is_significant", False),
            p_value=code_res.get("metrics", {}).get("p_value", 1.0),
            effect_size=code_res.get("metrics", {}).get("cohens_d", 0.0),
            grounded_in_lit=hypo_res.get("is_grounded", True)
        )
        self._record_event("REWARD_MODEL", "REWARD_ASSIGNED", f"Reward: {reward_info.get('total_reward')} ({reward_info.get('verdict')})")

        # Step 7: Synthesis of Publication-Ready LaTeX Research Paper
        self.current_state = "LATEX_SYNTHESIS"
        self._record_event("SYNTHESIS_MODULE", "COMPILE_PAPER", "Rendering LaTeX academic manuscript and BibTeX references")
        latex_res = self.latex_generator.compile_research_paper(
            hypothesis_data=hypo_res,
            experiment_data=code_res,
            critic_data=critic_res,
            literature_data=review_res
        )
        self._record_event("SYNTHESIS_MODULE", "PAPER_SAVED", f"Saved: {latex_res.get('tex_path')}")

        # Completion Telemetry
        self.current_state = "COMPLETED"
        total_duration = time.time() - start_time
        token_stats = self.memory.get_token_metrics()
        
        # Cost estimate: ~$0.0015 per 1K tokens
        estimated_cost_usd = round((token_stats["total_tokens_consumed"] / 1000.0) * 0.0015, 5)

        summary = {
            "status": "SUCCESS",
            "duration_seconds": round(total_duration, 2),
            "estimated_cost_usd": estimated_cost_usd,
            "research_topic": research_topic,
            "literature_review": review_res,
            "multimodal_figures": figures,
            "hypothesis": hypothesis,
            "code_execution": code_res,
            "critic_evaluation": critic_res,
            "rl_reward": reward_info,
            "latex_synthesis": latex_res,
            "telemetry": {
                "events_count": len(self.trace_logs),
                "tokens": token_stats,
                "cost_usd": estimated_cost_usd
            },
            "trace_logs": self.trace_logs
        }
        return summary

    def _record_event(self, role: str, action: str, details: str) -> None:
        event = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "role": role,
            "action": action,
            "details": details
        }
        self.trace_logs.append(event)
        logger.info(f"[{role}] {action} -> {details}")
