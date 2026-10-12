"""Agent Roles and Orchestration Package."""
from .base_agent import BaseAgent
from .literature_reviewer import LiteratureReviewerAgent
from .hypothesis_generator import HypothesisGeneratorAgent
from .code_executor_agent import CodeExecutorAgent
from .critic_agent import CriticAgent
from .orchestrator import ScientificDiscoveryOrchestrator

__all__ = [
    "BaseAgent",
    "LiteratureReviewerAgent",
    "HypothesisGeneratorAgent",
    "CodeExecutorAgent",
    "CriticAgent",
    "ScientificDiscoveryOrchestrator"
]
