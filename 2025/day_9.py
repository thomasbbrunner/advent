from collections import defaultdict, deque
from itertools import chain, combinations, pairwise
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""
data = Path("day_9.txt").read_text()

tile_idxs = [tuple(int(char) for char in line.split(",")) for line in data.splitlines()]

areas = {
    comb: (abs(comb[0][0] - comb[1][0]) + 1) * (abs(comb[0][1] - comb[1][1]) + 1)
    for comb in combinations(tile_idxs, 2)
}
rectangles = sorted(areas, key=lambda x: areas[x], reverse=True)

print(f"{areas[rectangles[0]]=}")

lines = tile_idxs + [tile_idxs[0]]
for rect in rectangles:
    x_min, x_max = min(rect[0][0], rect[1][0]), max(rect[0][0], rect[1][0])
    y_min, y_max = min(rect[0][1], rect[1][1]), max(rect[0][1], rect[1][1])

    intersects = False
    for l1, l2 in pairwise(lines):
        lx_min, lx_max = min(l1[0], l2[0]), max(l1[0], l2[0])
        ly_min, ly_max = min(l1[1], l2[1]), max(l1[1], l2[1])

        is_right = lx_min >= x_max
        is_left = lx_max <= x_min
        is_above = ly_min >= y_max
        is_below = ly_max <= y_min
        intersects = not (is_right or is_left or is_above or is_below)
        if intersects:
            break

    if not intersects:
        break

print(f"{areas[rect]=}")
