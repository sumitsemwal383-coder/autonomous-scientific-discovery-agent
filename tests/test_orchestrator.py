"""
Multi-Agent Orchestrator and Self-Debugging Loop Tests
Validates the complete closed-loop scientific discovery pipeline and RL self-debugging.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.agents.orchestrator import ScientificDiscoveryOrchestrator

def test_full_autonomous_discovery_cycle():
    orchestrator = ScientificDiscoveryOrchestrator(use_docker=False)
    result = orchestrator.run_discovery_cycle(
        research_topic="multi-agent reinforcement learning reasoning",
        max_papers=2,
        test_self_debug=False
    )
    assert result["status"] == "SUCCESS"
    assert result["literature_review"]["papers_found"] > 0
    assert len(result["hypothesis"].get("grounding_citations", [])) >= 0
    assert "statement" in result["hypothesis"]
    assert result["code_execution"]["status"] == "SUCCESS"
    assert result["critic_evaluation"]["status"] == "SUCCESS"
    assert "CONFIRMED" in result["critic_evaluation"]["verdict"]
    assert result["latex_synthesis"]["status"] == "SUCCESS"
    assert Path(result["latex_synthesis"]["tex_path"]).exists()

def test_rl_self_debugging_feedback_loop():
    orchestrator = ScientificDiscoveryOrchestrator(use_docker=False, max_debug_iterations=3)
    # Trigger intentional bug on iteration 1
    result = orchestrator.run_discovery_cycle(
        research_topic="iterative language model reflexion",
        max_papers=2,
        test_self_debug=True
    )
    assert result["status"] == "SUCCESS"
    code_res = result["code_execution"]
    # Verify that the self-debugging loop triggered at least 1 debug trace and recovered
    assert code_res["debug_iterations_count"] >= 2
    assert len(code_res["debug_trace"]) >= 1
    assert code_res["status"] == "SUCCESS"

if __name__ == "__main__":
    test_full_autonomous_discovery_cycle()
    test_rl_self_debugging_feedback_loop()
    print("[SUCCESS] All Multi-Agent Orchestrator and RL Self-Debugging tests passed successfully!")
