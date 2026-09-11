#!/usr/bin/env python3
"""
ast_verifier.py - Pure Python AST Invariant Verifier for Whetstone
Validates student code without execution: checks AST structure, forbidden tokens,
ensures zero-magic dependency bounds, and validates invariant rules.
"""
import ast
import sys
from typing import List, Dict, Any

class InvariantViolation(Exception):
    pass

class ASTVerifier:
    def __init__(self, forbidden_modules: List[str] = None, forbidden_calls: List[str] = None):
        self.forbidden_modules = forbidden_modules or ["os", "sys", "subprocess", "socket", "eval", "exec"]
        self.forbidden_calls = forbidden_calls or ["eval", "exec", "compile", "__import__"]

    def verify_python_source(self, code_str: str) -> Dict[str, Any]:
        try:
            tree = ast.parse(code_str)
        except SyntaxError as e:
            return {"valid": False, "error": f"Syntax Error: {e}"}

        violations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name in self.forbidden_modules:
                        violations.append(f"Forbidden import: {alias.name}")
            elif isinstance(node, ast.ImportFrom):
                if node.module in self.forbidden_modules:
                    violations.append(f"Forbidden import from: {node.module}")
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in self.forbidden_calls:
                    violations.append(f"Forbidden function call: {node.func.id}")

        if violations:
            return {"valid": False, "violations": violations}
        return {"valid": True, "node_count": len(list(ast.walk(tree)))}

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            src = f.read()
        res = ASTVerifier().verify_python_source(src)
        print(res)
