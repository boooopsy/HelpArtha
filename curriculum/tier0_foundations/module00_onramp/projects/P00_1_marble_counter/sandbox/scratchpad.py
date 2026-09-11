"""
Scratchpad for the Marble 3-Bit Counter.

Before writing the real solve(), experiment here. Try to answer, by hand
first, then check with code:
  - If the counter is at binary 101 (5) and gets 3 more marbles, where
    does it land?
  - How many marbles does it take to go all the way around once, back
    to 0, starting from 0? From 3?
"""


def experiment():
    value = 0
    for i in range(1, 11):
        value = (value + 1) % 8
        print(f"pulse {i}: register = {value:03b} ({value})")


if __name__ == "__main__":
    experiment()
