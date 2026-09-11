#!/usr/bin/env python3
"""
starter/solution.py - Reference Implementation for P00_1 Marble Counter

A Turing Tumble marble machine is a real, physical 3-bit binary counter:
each time a marble drops through the mechanism it acts like one clock
pulse, and the three gear-bits flip according to normal binary counting
rules (000 -> 001 -> 010 -> ... -> 111 -> 000, wrapping around).

This function simulates that mechanism in software: no gears, but the
exact same math a 3-bit counter does.
"""
from typing import Any, Dict, List


def solve(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Simulate a 3-bit binary up-counter receiving a sequence of marble
    drops (clock pulses).

    Input:
        {
          "start": int   # initial register value, 0-7 (default 0)
          "pulses": int  # how many marbles are dropped (clock pulses)
        }

    Output:
        {
          "start": int,
          "pulses": int,
          "final_value": int,       # register value after all pulses, 0-7
          "trace": [int, ...],      # register value after each pulse
          "wraps": int              # how many times the counter overflowed
        }
    """
    if not isinstance(input_data, dict):
        raise ValueError("Invalid input format: dictionary expected.")

    start = input_data.get("start", 0)
    pulses = input_data.get("pulses", 0)

    if not isinstance(start, int) or not (0 <= start <= 7):
        raise ValueError("start must be an integer register value 0-7 (3 bits).")
    if not isinstance(pulses, int) or pulses < 0:
        raise ValueError("pulses must be a non-negative integer.")

    value = start
    trace: List[int] = []
    wraps = 0

    for _ in range(pulses):
        value += 1
        if value > 7:
            value = 0
            wraps += 1
        trace.append(value)

    return {
        "start": start,
        "pulses": pulses,
        "final_value": value,
        "trace": trace,
        "wraps": wraps,
    }


if __name__ == "__main__":
    test_sample = {"start": 5, "pulses": 4}
    print("Self-test result:", solve(test_sample))
