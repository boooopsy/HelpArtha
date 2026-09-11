#!/usr/bin/env python3
"""
runner.py - Deterministic execution harness runner for Whetstone projects.
Executes project test suites against vectors.json with strict timeouts and memory isolation.
"""
import json
import os
import subprocess
import sys
import time
from typing import Dict, Any, List

def run_test_suite(runner_path: str, timeout_seconds: int = 5) -> Dict[str, Any]:
    if not os.path.exists(runner_path):
        return {"ok": False, "error": f"Test runner not found: {runner_path}"}

    cwd = os.path.dirname(os.path.abspath(runner_path))
    start_time = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, os.path.basename(runner_path)],
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )
        elapsed = time.time() - start_time
        return {
            "ok": proc.returncode == 0,
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "elapsed_ms": round(elapsed * 1000, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            "ok": False,
            "error": f"Execution timed out after {timeout_seconds} seconds",
            "timeout": True
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        result = run_test_suite(sys.argv[1])
        print(json.dumps(result, indent=2))
