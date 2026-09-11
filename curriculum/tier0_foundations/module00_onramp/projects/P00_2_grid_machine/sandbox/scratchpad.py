"""
Scratchpad for the Token Grid State Machine.

Walk through this on paper first with a small row of tokens like
[5, 2, 4, 1] before trusting the code:
  - How many times does the pointer compare two neighbors in total?
  - How many of those comparisons actually cause a swap?
  - After one full left-to-right pass, where does the largest number end up?
"""


def experiment():
    cells = [5, 2, 4, 1]
    arr = list(cells)
    for pass_end in range(len(arr) - 1, 0, -1):
        for i in range(pass_end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        print("after a pass:", arr)


if __name__ == "__main__":
    experiment()
