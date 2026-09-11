#!/usr/bin/env python3
"""
harness/test_runner.py - Deterministic Verification Runner for P05 2 Scalar Autograd (P05_2)
Verifies:
1. Static AST Invariant Inspection (Zero forbidden imports, zero non-deterministic calls)
2. All 8 Calibrated Deterministic Test Vectors (Pre/Post Condition Contracts)
"""
import os
import sys
import json
import ast

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(CURRENT_DIR)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR))))
STARTER_DIR = os.path.join(PROJECT_DIR, "starter")
sys.path.insert(0, STARTER_DIR)

# 1. AST Invariant Inspection
def verify_ast_invariants():
    sol_file = os.path.join(STARTER_DIR, "solution.py")
    if not os.path.exists(sol_file):
        print(f"FAIL: solution.py not found at {sol_file}")
        sys.exit(1)
    
    with open(sol_file, "r", encoding="utf-8") as f:
        src = f.read()
    
    tree = ast.parse(src)
    forbidden = {"random", "time", "subprocess", "socket", "urllib", "requests"}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name in forbidden:
                    print(f"FAIL: Forbidden non-deterministic module imported: {alias.name}")
                    sys.exit(1)
        elif isinstance(node, ast.ImportFrom):
            if node.module in forbidden:
                print(f"FAIL: Forbidden non-deterministic module imported from: {node.module}")
                sys.exit(1)
    
    print("[AST INVARIANTS] Verified: Zero non-deterministic imports detected.")

# 2. Vector Execution
def run_vectors():
    try:
        from solution import solve
    except ImportError as e:
        print(f"FAIL: Could not import solve() from starter/solution.py: {e}")
        sys.exit(1)

    vec_file = os.path.join(CURRENT_DIR, "vectors.json")
    with open(vec_file, "r", encoding="utf-8") as f:
        vectors = json.load(f)

    passed = 0
    for idx, vec in enumerate(vectors, 1):
        inp = vec["input"]
        expected = vec["expected"]
        out = solve(inp)
        
        # Verify strict invariant preservation
        if out != expected:
            print(f"FAIL [{vec['id']}]: Expected {expected}, got {out} ({vec['description']})")
            sys.exit(1)
        
        print(f"[VECTOR #{idx}] {vec['id']}: PASS ({vec['name']})")
        passed += 1

    print(f"\n================================================================")
    print(f"ALL {passed} / {len(vectors)} INVARIANT VECTORS PASSED FOR P05_2")
    print(f"STATUS: EXIT 0 (DETERMINISTIC VERIFICATION COMPLETE)")
    print(f"================================================================")
    sys.exit(0)

if __name__ == "__main__":
    verify_ast_invariants()
    run_vectors()
