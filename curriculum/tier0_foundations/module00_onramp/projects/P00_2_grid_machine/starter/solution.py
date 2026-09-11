#!/usr/bin/env python3
"""
starter/solution.py - Reference Implementation for P00_2 Token Grid State Machine

Simulates an "ASCII grid runner": a pointer that walks along a row of 8
numbered token cells and performs an in-place bubble sort, recording
every comparison and every swap as if a person were physically walking
along the grid moving tokens.
"""
from typing import Any, Dict, List


def solve(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Input:
        {"cells": [int, ...]}   # up to 8 integers on the token grid

    Output:
        {
          "cells": [int, ...],        # original input, unchanged
          "sorted_cells": [int, ...], # final sorted order
          "comparisons": int,         # total pointer comparisons made
          "swaps": int,               # total token swaps made
          "trace": [                  # one entry per pointer step
             {"pointer": int, "compared": [int,int], "swapped": bool}
          ]
        }
    """
    if not isinstance(input_data, dict):
        raise ValueError("Invalid input format: dictionary expected.")

    cells = input_data.get("cells", [])
    if not isinstance(cells, list) or not (1 <= len(cells) <= 8):
        raise ValueError("cells must be a list of 1 to 8 integers.")
    if not all(isinstance(x, int) for x in cells):
        raise ValueError("all cells must be integers.")

    arr = list(cells)
    n = len(arr)
    comparisons = 0
    swaps = 0
    trace: List[Dict[str, Any]] = []

    for pass_end in range(n - 1, 0, -1):
        for pointer in range(pass_end):
            left, right = arr[pointer], arr[pointer + 1]
            comparisons += 1
            did_swap = False
            if left > right:
                arr[pointer], arr[pointer + 1] = right, left
                swaps += 1
                did_swap = True
            trace.append({
                "pointer": pointer,
                "compared": [left, right],
                "swapped": did_swap,
            })

    return {
        "cells": cells,
        "sorted_cells": arr,
        "comparisons": comparisons,
        "swaps": swaps,
        "trace": trace,
    }


if __name__ == "__main__":
    test_sample = {"cells": [5, 2, 4, 1]}
    print("Self-test result:", solve(test_sample))
