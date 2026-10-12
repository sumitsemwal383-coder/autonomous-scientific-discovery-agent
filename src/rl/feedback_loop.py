"""
Reinforcement Learning Self-Debugging Feedback Loop
Analyzes execution errors, traces exceptions, generates actionable reflexions,
and prompts the agent to rewrite and optimize experimental code.
"""
import re
import logging
from typing import Dict, Any, List, Optional
from .reward_model import DiscoveryRewardModel

logger = logging.getLogger(__name__)

class SelfDebuggingFeedbackLoop:
    def __init__(self, max_iterations: int = 4):
        self.max_iterations = max_iterations
        self.reward_model = DiscoveryRewardModel()
        self.history: List[Dict[str, Any]] = []

    def analyze_execution_failure(self, code: str, stderr: str, exit_code: int, security_violation: Optional[str] = None) -> Dict[str, Any]:
        """
        Parses runtime errors and produces structured debugging critique.
        """
        if security_violation:
            return {
                "error_type": "SecurityBreakoutViolation",
                "message": security_violation,
                "culprit_hint": "Code attempted an unauthorized system call or forbidden module import.",
                "actionable_fix": "Rewrite code strictly using allowed scientific packages (numpy, scipy, pandas, sklearn). Remove all OS, socket, subprocess, and dangerous eval/exec calls."
            }

        # Analyze standard Python errors from stderr
        if "SyntaxError" in stderr:
            match = re.search(r"line (\d+)", stderr)
            line_no = match.group(1) if match else "unknown"
            return {
                "error_type": "SyntaxError",
                "message": stderr.strip().splitlines()[-1],
                "culprit_hint": f"Syntax error near line {line_no}.",
                "actionable_fix": "Verify parentheses, indentation, and variable assignments in Python 3 syntax."
            }
        elif "ZeroDivisionError" in stderr:
            return {
                "error_type": "ZeroDivisionError",
                "message": "Division by zero encountered in calculation.",
                "culprit_hint": "Denominator evaluated to 0 (e.g., standard deviation was 0 or sample size was 0).",
                "actionable_fix": "Add an epsilon (e.g. + 1e-8) or clamp denominator values before division."
            }
        elif "NameError" in stderr:
            match = re.search(r"name '(\w+)' is not defined", stderr)
            var_name = match.group(1) if match else "variable"
            return {
                "error_type": "NameError",
                "message": f"Undefined variable or module: '{var_name}'",
                "culprit_hint": f"The identifier '{var_name}' was accessed before declaration or requires import.",
                "actionable_fix": f"Ensure '{var_name}' is declared or imported from numpy/scipy before use."
            }
        elif "IndexError" in stderr or "ValueError" in stderr:
            return {
                "error_type": "ShapeOrValueError",
                "message": stderr.strip().splitlines()[-1],
                "culprit_hint": "Array dimensions mismatched or empty collection accessed.",
                "actionable_fix": "Verify array shapes (e.g., .shape, len()) and ensure data generators produce at least N >= 30 samples."
            }
        elif "timed out" in stderr.lower():
            return {
                "error_type": "ExecutionTimeout",
                "message": "Execution time exceeded sandbox threshold.",
                "culprit_hint": "Infinite loop or computationally excessive simulation size.",
                "actionable_fix": "Vectorize matrix loops using NumPy array operations and reduce iteration steps."
            }
        else:
            return {
                "error_type": "RuntimeError",
                "message": stderr.strip() if stderr else f"Non-zero exit code: {exit_code}",
                "culprit_hint": "Unhandled exception during script execution.",
                "actionable_fix": "Refactor logic with defensive try/except handling and ensure __AGENT_METRICS__ dictionary is populated."
            }

    def generate_debugging_prompt(self, iteration: int, original_code: str, analysis: Dict[str, Any]) -> str:
        """
        Creates the iterative reflexion prompt for the Code Executor.
        """
        prompt = (
            f"=== RL SELF-DEBUGGING FEEDBACK (Cycle {iteration} / {self.max_iterations}) ===\n"
            f"Detected Failure: {analysis['error_type']}\n"
            f"Diagnostic Message: {analysis['message']}\n"
            f"Root Cause: {analysis['culprit_hint']}\n"
            f"Corrective Directive: {analysis['actionable_fix']}\n\n"
            f"Original Defective Code Snippet:\n"
            f"```python\n{original_code}\n```\n\n"
            f"Task: Rewrite the experimental code to fix the failure above while strictly fulfilling the scientific hypothesis testing requirements."
        )
        return prompt

    def record_cycle(self, iteration: int, reward_info: Dict[str, Any], fix_applied: str) -> None:
        self.history.append({
            "iteration": iteration,
            "reward": reward_info.get("total_reward", 0.0),
            "verdict": reward_info.get("verdict", ""),
            "fix_applied": fix_applied
        })
