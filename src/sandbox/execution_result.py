"""
Structured Execution Result
Encapsulates stdout, stderr, execution duration, metrics, and security breakout diagnostics.
"""
from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class ExecutionResult:
    success: bool
    stdout: str = ""
    stderr: str = ""
    exit_code: int = 0
    duration: float = 0.0
    metrics: Dict[str, Any] = field(default_factory=dict)
    security_violation: Optional[str] = None
    is_breakout_attempt: bool = False
    sandbox_mode: str = "hardened_subproc"

    def to_dict(self) -> Dict[str, Any]:
        return {
            "success": self.success,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "exit_code": self.exit_code,
            "duration": round(self.duration, 3),
            "metrics": self.metrics,
            "security_violation": self.security_violation,
            "is_breakout_attempt": self.is_breakout_attempt,
            "sandbox_mode": self.sandbox_mode
        }
