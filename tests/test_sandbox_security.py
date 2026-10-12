"""
Sandbox Breakout Prevention Test Suite
Validates that the automated code execution sandbox actively detects and prevents
jailbreaks, privilege escalations, unauthorized imports, and reflective breakouts.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from src.sandbox.secure_sandbox import SecureSandbox, ASTSecurityValidator

def test_legitimate_scientific_code():
    sandbox = SecureSandbox(timeout_seconds=5)
    clean_code = """
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
result = float(np.dot(a, b))
print(f"Result: {result}")
global __AGENT_METRICS__
__AGENT_METRICS__ = {"dot_product": result}
"""
    res = sandbox.execute(clean_code)
    assert res.success is True
    assert res.is_breakout_attempt is False
    assert res.security_violation is None
    assert res.metrics.get("dot_product") == 32.0

def test_block_os_system_breakout():
    sandbox = SecureSandbox(timeout_seconds=5)
    malicious_code = """
import os
os.system("echo 'pwned'")
"""
    res = sandbox.execute(malicious_code)
    assert res.success is False
    assert res.is_breakout_attempt is True
    assert "Blocked import of unauthorized system module: 'os'" in res.security_violation

def test_block_subprocess_breakout():
    sandbox = SecureSandbox(timeout_seconds=5)
    malicious_code = """
import subprocess
subprocess.run(["cmd.exe", "/c", "dir"])
"""
    res = sandbox.execute(malicious_code)
    assert res.success is False
    assert res.is_breakout_attempt is True
    assert "subprocess" in res.security_violation

def test_block_eval_exec_breakout():
    sandbox = SecureSandbox(timeout_seconds=5)
    malicious_code = """
cmd = "__import__('os').system('dir')"
eval(cmd)
"""
    res = sandbox.execute(malicious_code)
    assert res.success is False
    assert res.is_breakout_attempt is True
    assert "Blocked invocation of unsafe builtin function" in res.security_violation

def test_block_reflective_class_breakout():
    sandbox = SecureSandbox(timeout_seconds=5)
    malicious_code = """
subclasses = ().__class__.__base__.__subclasses__()
"""
    res = sandbox.execute(malicious_code)
    assert res.success is False
    assert res.is_breakout_attempt is True
    assert "Blocked reflective sandbox breakout attribute" in res.security_violation

def test_enforce_timeout_boundary():
    sandbox = SecureSandbox(timeout_seconds=2)
    hang_code = """
import time
while True:
    time.sleep(0.1)
"""
    res = sandbox.execute(hang_code)
    assert res.success is False
    assert res.exit_code == -2
    assert "timed out" in res.stderr.lower()

if __name__ == "__main__":
    test_legitimate_scientific_code()
    test_block_os_system_breakout()
    test_block_subprocess_breakout()
    test_block_eval_exec_breakout()
    test_block_reflective_class_breakout()
    test_enforce_timeout_boundary()
    print("[SUCCESS] All sandbox breakout prevention tests passed successfully!")
