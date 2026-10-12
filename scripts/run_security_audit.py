"""
Automated Penetration Testing & Security Audit
Runs attack payloads against the Code Execution Sandbox to verify that breakouts are 100% prevented.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.sandbox.secure_sandbox import SecureSandbox

PAYLOADS = [
    ("OS Command Execution", "import os\nos.system('whoami')"),
    ("Subprocess Shell Spawn", "import subprocess\nsubprocess.call(['whoami'])"),
    ("Dynamic Code Evaluation", "eval('__import__(\"os\").getcwd()')"),
    ("Builtin Function Compilation", "exec('compile(\"a=1\", \"\", \"single\")')"),
    ("Reflective Subclass Enumeration", "x = ().__class__.__bases__[0].__subclasses__()"),
    ("Network Socket Creation", "import socket\ns = socket.socket()"),
    ("Path Traversal via Open", "with open('../../../../../etc/passwd', 'r') as f: data = f.read()"),
    ("Sys Exit Denial of Service", "import sys\nsys.exit(0)")
]

def run_audit():
    print("\n" + "="*70)
    print("  AUTOMATED SANDBOX PENETRATION & BREAKOUT AUDIT")
    print("  Target: Zaalima Execution Sandbox")
    print("="*70)

    sandbox = SecureSandbox(timeout_seconds=5)
    total = len(PAYLOADS)
    blocked_count = 0

    for idx, (name, code) in enumerate(PAYLOADS, 1):
        res = sandbox.execute(code)
        is_blocked = (not res.success) and (res.is_breakout_attempt or res.security_violation is not None)
        status_text = "[BLOCKED / PREVENTED]" if is_blocked else "[BREACH / FAILED]"
        print(f"[{idx}/{total}] Attack: {name:<35} -> {status_text}")
        if is_blocked:
            blocked_count += 1
            print(f"       Diagnostic: {res.security_violation}")

    print("-"*70)
    print(f"Audit Summary: {blocked_count}/{total} attacks neutralized ({blocked_count/total*100:.1f}% Defense Efficacy)")
    print("="*70 + "\n")
    assert blocked_count == total, "Sandbox failed to prevent one or more penetration payloads!"

if __name__ == "__main__":
    run_audit()
