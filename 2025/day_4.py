import itertools 
from pathlib import Path

data = Path("day_4.txt").read_text()
# data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

char_map = {
    ".": 0,
    "@": 1,
    "x": 2,
}

def kernel(row: int, col: int, arr: list[list[str]]) -> int:
    prev_row = row - 1 if row - 1 >= 0 else None
    next_row = row + 1 if row + 1 < len(arr) else None
    prev_col = col - 1 if col - 1 >= 0 else None
    next_col = col + 1 if col + 1 < len(arr[0]) else None
    vals = [
        # N
        arr[prev_row][col] == "@" if prev_row is not None else False,
        # NE
        arr[prev_row][next_col] == "@" if prev_row is not None and next_col is not None else False,
        # E
        arr[row][next_col] == "@" if next_col is not None else False,
        # SE
        arr[next_row][next_col] == "@" if next_row is not None and next_col is not None else False,
        # S
        arr[next_row][col] == "@" if next_row is not None else False,
        # SW
        arr[next_row][prev_col] == "@" if next_row is not None and prev_col is not None else False,
        # W
        arr[row][prev_col] == "@" if prev_col is not None else False,
        # NW
        arr[prev_row][prev_col] == "@" if prev_row is not None and prev_col is not None else False,
    ]
    return sum(vals)

removed = 0
prev_removed = -1
arr = [[char for char in line] for line in data.splitlines()]

while True:
    for i, j in itertools.product(range(len(arr)), range(len(arr[0]))):
        if arr[i][j] != "@":
            continue
        if kernel(i, j, arr) < 4:
            arr[i][j] = "x"
            removed += 1
    
    if removed == prev_removed:
        break
    prev_removed = removed
    

print(f"{removed=}")
print("\n".join(["".join(line) for line in arr]))
