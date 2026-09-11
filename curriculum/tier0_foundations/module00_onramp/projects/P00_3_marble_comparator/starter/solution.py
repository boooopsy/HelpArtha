#!/usr/bin/env python3
"""
starter/solution.py - Reference Implementation for P00_3 Mechanical Stream Comparator

Simulates a Turing Tumble "interceptor" circuit: marbles drop one after
another, and a comparator gate watches each pair of consecutive marbles.
The moment two neighbors differ, the physical circuit halts (an
interceptor blocks the ramp). If every neighbor matches, the marbles
run all the way through.
"""
from typing import Any, Dict, List, Optional


def solve(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input:
        {"stream": [int or str, ...]}  # sequence of marble values, len 1-8

    Output:
        {
          "stream": [...],
          "halted": bool,          # True if two neighbors ever differed
          "halt_index": int|None,  # index of the SECOND item in the first
                                    # differing pair, or None if never halted
          "checks": int            # how many neighbor pairs were checked
                                    # before halting (or in total, if it
                                    # never halts)
        }
    """
    if not isinstance(input_data, dict):
        raise ValueError("Invalid input format: dictionary expected.")

    stream = input_data.get("stream", [])
    if not isinstance(stream, list) or not (1 <= len(stream) <= 8):
        raise ValueError("stream must be a list of 1 to 8 values.")

    checks = 0
    halt_index: Optional[int] = None

    for i in range(1, len(stream)):
        checks += 1
        if stream[i] != stream[i - 1]:
            halt_index = i
            break

    return {
        "stream": stream,
        "halted": halt_index is not None,
        "halt_index": halt_index,
        "checks": checks,
    }


if __name__ == "__main__":
    test_sample = {"stream": [1, 1, 1, 2, 1]}
    print("Self-test result:", solve(test_sample))
