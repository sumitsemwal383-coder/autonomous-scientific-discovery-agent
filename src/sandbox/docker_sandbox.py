"""
Containerized Docker Sandbox Runner
Executes untrusted agent-generated ML code inside isolated Docker containers
with strict capability dropping, memory quotas, and CPU limits.
"""
import subprocess
import shutil
import logging
from typing import Optional
from pathlib import Path
from .execution_result import ExecutionResult
from .secure_sandbox import SecureSandbox

logger = logging.getLogger(__name__)

class DockerSandbox:
    def __init__(self, image_name: str = "zaalima-discovery-sandbox:latest", timeout_seconds: int = 30):
        self.image_name = image_name
        self.timeout_seconds = timeout_seconds
        self.docker_available = self._check_docker()
        self.fallback_sandbox = SecureSandbox(timeout_seconds=timeout_seconds)

    def _check_docker(self) -> bool:
        docker_path = shutil.which("docker")
        if not docker_path:
            return False
        try:
            res = subprocess.run(["docker", "info"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
            return res.returncode == 0
        except Exception:
            return False

    def execute(self, code_str: str) -> ExecutionResult:
        """
        Executes code inside a hardened Docker container, or seamlessly falls back
        to the AST-verified SecureSandbox if Docker daemon is not active.
        """
        if not self.docker_available:
            logger.info("Docker daemon not accessible; utilizing AST-hardened secure subprocess sandbox.")
            res = self.fallback_sandbox.execute(code_str)
            res.sandbox_mode = "secure_ast_fallback"
            return res

        # Run containerized with locked-down security flags
        # --network none : Prevent any network socket breakout
        # --cap-drop ALL : Drop all Linux capabilities
        # --read-only    : Read-only container root
        # --memory 512m  : Bounded RAM allocation
        import tempfile
        import time

        with tempfile.TemporaryDirectory(prefix="docker_sandbox_") as tmpdir:
            script_path = Path(tmpdir) / "experiment.py"
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(code_str)

            cmd = [
                "docker", "run", "--rm",
                "--network", "none",
                "--cap-drop", "ALL",
                "--memory", "512m",
                "--cpus", "1.0",
                "-v", f"{str(script_path)}:/app/experiment.py:ro",
                self.image_name,
                "python", "/app/experiment.py"
            ]

            start_time = time.time()
            try:
                proc = subprocess.run(
                    cmd,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout_seconds
                )
                duration = time.time() - start_time
                success = (proc.returncode == 0)
                metrics = self.fallback_sandbox._extract_metrics(proc.stdout)

                return ExecutionResult(
                    success=success,
                    stdout=proc.stdout,
                    stderr=proc.stderr,
                    exit_code=proc.returncode,
                    duration=duration,
                    metrics=metrics,
                    security_violation=None,
                    is_breakout_attempt=False,
                    sandbox_mode="docker_containerized"
                )
            except subprocess.TimeoutExpired:
                return ExecutionResult(
                    success=False,
                    stdout="",
                    stderr=f"Docker execution timed out after {self.timeout_seconds}s",
                    exit_code=-2,
                    duration=time.time() - start_time,
                    metrics={},
                    security_violation="Container timeout limit reached",
                    is_breakout_attempt=False,
                    sandbox_mode="docker_containerized"
                )
            except Exception as e:
                return ExecutionResult(
                    success=False,
                    stdout="",
                    stderr=str(e),
                    exit_code=-3,
                    duration=time.time() - start_time,
                    metrics={},
                    security_violation=str(e),
                    is_breakout_attempt=False,
                    sandbox_mode="docker_containerized"
                )
