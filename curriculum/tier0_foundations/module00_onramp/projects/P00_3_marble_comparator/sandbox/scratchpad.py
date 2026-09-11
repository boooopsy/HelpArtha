"""
Scratchpad for the Mechanical Stream Comparator.

Think of marbles dropping one at a time: [1, 1, 1, 2, 1].
  - Which pair of neighbors is the FIRST one that doesn't match?
  - What index does the interceptor trigger at?
  - What happens if the whole stream is identical, like [5,5,5,5]?
"""


def experiment():
    for stream in [[1, 1, 1, 2, 1], [7, 7, 7, 7], [3]]:
        halted = False
        idx = None
        for i in range(1, len(stream)):
            if stream[i] != stream[i - 1]:
                halted = True
                idx = i
                break
        print(stream, "-> halted:", halted, "at index:", idx)


if __name__ == "__main__":
    experiment()
