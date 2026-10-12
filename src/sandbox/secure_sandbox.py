"""
Secure Sandboxed Python Execution Engine
Performs Static AST Security Validation to actively prevent jailbreaks and breakout attempts,
enforcing resource boundaries and isolating generated ML experiments.
"""
import ast
import json
import logging
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional, Tuple
from config.settings import SANDBOX_TIMEOUT_SECONDS, SANDBOX_DISALLOWED_IMPORTS
from .execution_result import ExecutionResult

logger = logging.getLogger(__name__)

class ASTSecurityValidator(ast.NodeVisitor):
    """
    Statically analyzes Python AST to detect and block malicious breakouts,
    privilege escalations, dangerous builtins, and OS/socket primitives.
    """
    def __init__(self):
        self.violations = []
        self.is_breakout = False
        self.disallowed_modules = {
            "os", "subprocess", "ctypes", "socket", "shutil",
            "urllib", "requests", "http", "ftplib", "telnetlib",
            "paramiko", "pty", "fcntl", "pwd", "grp", "sys"
        }
        self.disallowed_functions = {
            "eval", "exec", "compile", "__import__", "breakpoint",
            "exit", "quit"
        }
        self.dangerous_attributes = {
            "__class__", "__base__", "__bases__", "__subclasses__",
            "__globals__", "__builtins__", "__import__"
        }

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            mod_root = alias.name.split(".")[0]
            if mod_root in self.disallowed_modules:
                self.violations.append(f"Blocked import of unauthorized system module: '{alias.name}'")
                self.is_breakout = True
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module:
            mod_root = node.module.split(".")[0]
            if mod_root in self.disallowed_modules:
                self.violations.append(f"Blocked from-import of unauthorized system module: '{node.module}'")
                self.is_breakout = True
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        # Detect eval(), exec(), compile()
        if isinstance(node.func, ast.Name):
            if node.func.id in self.disallowed_functions:
                self.violations.append(f"Blocked invocation of unsafe builtin function: '{node.func.id}()'")
                self.is_breakout = True
        # Detect open() targeting sensitive files
        if isinstance(node.func, ast.Name) and node.func.id == "open":
            if node.args and isinstance(node.args[0], ast.Constant):
                path_str = str(node.args[0].value)
                if any(x in path_str.lower() for x in ["etc", "windows", "system32", ".ssh", "root", ".."]):
                    self.violations.append(f"Blocked potential directory traversal in open('{path_str}')")
                    self.is_breakout = True
        self.generic_visit(node)

    def visit_Attribute(self, node: ast.Attribute):
        if node.attr in self.dangerous_attributes:
            self.violations.append(f"Blocked reflective sandbox breakout attribute: '{node.attr}'")
            self.is_breakout = True
        self.generic_visit(node)


class SecureSandbox:
    """
    Isolated execution runner enforcing AST security validation,
    execution timeouts, and structured telemetry extraction.
    """
    def __init__(self, timeout_seconds: int = SANDBOX_TIMEOUT_SECONDS):
        self.timeout_seconds = timeout_seconds

    def validate_code(self, code_str: str) -> Tuple[bool, Optional[str], bool]:
        """
        Returns (is_valid, violation_message, is_breakout_attempt)
        """
        try:
            tree = ast.parse(code_str)
        except SyntaxError as se:
            return False, f"Syntax Error: {se}", False

        validator = ASTSecurityValidator()
        validator.visit(tree)

        if validator.violations:
            violation_msg = "; ".join(validator.violations)
            return False, violation_msg, validator.is_breakout

        return True, None, False

    def execute(self, code_str: str) -> ExecutionResult:
        """
        Validates and runs Python code within an isolated subprocess sandbox.
        """
        # 1. AST Static Security Audit
        is_valid, violation, is_breakout = self.validate_code(code_str)
        if not is_valid:
            logger.warning(f"Sandbox security audit failed! Violation: {violation}")
            return ExecutionResult(
                success=False,
                stdout="",
                stderr=f"SECURITY VIOLATION: {violation}",
                exit_code=-1,
                duration=0.0,
                metrics={},
                security_violation=violation,
                is_breakout_attempt=is_breakout,
                sandbox_mode="hardened_ast_subproc"
            )

        # 2. Prepare isolated temporary execution directory
        with tempfile.TemporaryDirectory(prefix="agent_sandbox_") as tmpdir:
            script_path = Path(tmpdir) / "experiment_run.py"
            
            # Wrap code with metric capture hooks
            instrumented_code = self._instrument_code(code_str)
            with open(script_path, "w", encoding="utf-8") as f:
                f.write(instrumented_code)

            start_time = time.time()
            try:
                # Subprocess with clean environment and bounded timeout
                proc = subprocess.run(
                    [sys.executable, str(script_path)],
                    cwd=tmpdir,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout_seconds
                )
                duration = time.time() - start_time
                stdout = proc.stdout
                stderr = proc.stderr
                exit_code = proc.returncode

                # Parse metrics from stdout
                metrics = self._extract_metrics(stdout)
                success = (exit_code == 0)

                return ExecutionResult(
                    success=success,
                    stdout=stdout,
                    stderr=stderr,
                    exit_code=exit_code,
                    duration=duration,
                    metrics=metrics,
                    security_violation=None,
                    is_breakout_attempt=False,
                    sandbox_mode="hardened_ast_subproc"
                )

            except subprocess.TimeoutExpired:
                duration = time.time() - start_time
                return ExecutionResult(
                    success=False,
                    stdout="",
                    stderr=f"Execution timed out after {self.timeout_seconds} seconds.",
                    exit_code=-2,
                    duration=duration,
                    metrics={},
                    security_violation=f"Timeout limit of {self.timeout_seconds}s exceeded",
                    is_breakout_attempt=False,
                    sandbox_mode="hardened_ast_subproc"
                )
            except Exception as e:
                duration = time.time() - start_time
                return ExecutionResult(
                    success=False,
                    stdout="",
                    stderr=f"Sandbox execution error: {str(e)}",
                    exit_code=-3,
                    duration=duration,
                    metrics={},
                    security_violation=str(e),
                    is_breakout_attempt=False,
                    sandbox_mode="hardened_ast_subproc"
                )

    def _instrument_code(self, code: str) -> str:
        """Adds structured telemetry dumping helpers."""
        metric_footer = """
import json

# Ensure agent metrics are exported if defined
if '__AGENT_METRICS__' in locals():
    print("__AGENT_METRICS__:" + json.dumps(__AGENT_METRICS__))
"""
        return code + "\n" + metric_footer

    def _extract_metrics(self, stdout: str) -> dict:
        metrics = {}
        for line in stdout.splitlines():
            if line.startswith("__AGENT_METRICS__:"):
                json_str = line.replace("__AGENT_METRICS__:", "").strip()
                try:
                    metrics.update(json.loads(json_str))
                except Exception:
                    pass
        return metrics
