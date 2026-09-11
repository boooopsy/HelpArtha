#!/usr/bin/env python3
"""
scheduler.py - Python FSRS-6 Engine for Whetstone Backend / CLI Worker
Pinned against py-fsrs 6.3.2. Provides calculation and stability updates.
"""
import math
import json
import os
import sys
from typing import Dict, Any, Optional

DEFAULT_WEIGHTS = [
    0.212, 1.2931, 2.3065, 8.2956, 6.4133, 0.8334, 3.0194, 0.001,
    1.8722, 0.1666, 0.796, 1.4835, 0.0614, 0.2629, 1.6483, 0.6014,
    1.8729, 0.5425, 0.0912, 0.0658, 0.1542
]

class FSRS6:
    def __init__(self, weights=None, desired_retention=0.9):
        self.w = weights or DEFAULT_WEIGHTS
        self.desired_retention = desired_retention
        self.decay = -self.w[20]
        self.factor = 0.9 ** (1.0 / self.decay) - 1.0

    def next_interval_days(self, stability: float) -> int:
        days = (stability / self.factor) * ((self.desired_retention ** (1.0 / self.decay)) - 1.0)
        return max(1, min(int(round(days)), 36500))

    def retrievability(self, stability: float, elapsed_days: float) -> float:
        if stability <= 0:
            return 0.0
        return (1.0 + self.factor * max(0.0, elapsed_days) / stability) ** self.decay

if __name__ == "__main__":
    f = FSRS6()
    print(f"FSRS-6 Initialized with decay={f.decay:.4f}, factor={f.factor:.4f}")
