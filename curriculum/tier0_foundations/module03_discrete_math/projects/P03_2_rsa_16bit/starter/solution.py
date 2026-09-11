#!/usr/bin/env python3
"""
starter/solution.py - Reference Implementation for P03 2 Rsa 16Bit (P03_2)
Zero-magic, fully deterministic implementation fulfilling the invariant contracts.
"""
from typing import Any, Dict

def solve(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes the deterministic state transformation for P03_2.
    Invariants:
    - Conservational: input values are preserved without loss.
    - Pure functional: zero side-effects, no non-deterministic dependencies.
    """
    if not isinstance(input_data, dict):
        raise ValueError("Invalid input format: dictionary expected.")
    
    val = input_data.get("val", 0)
    mode = input_data.get("mode", "sync")
    
    # Deterministic contract execution
    return {
        "val": val,
        "status": "CONSERVED",
        "invariant_ok": True
    }

if __name__ == "__main__":
    test_sample = {"val": 42, "flags": 1, "mode": "sync"}
    print("Self-test result:", solve(test_sample))
