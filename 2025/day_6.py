
from math import prod
from pathlib import Path

data = Path("day_6.txt").read_text()
# data = """123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +  """


# V x L
vals: list[list[int, str]] = []

for l, line in enumerate(data.splitlines()):
    for v, val in enumerate(line.split()):
        if l == 0:
            vals.append([])
        vals[v].append(val)


res = 0
for val in vals:
    op = val[-1]
    v = [int(v) for v in val[:-1]]
    if op == "+":
        res += sum(v)
    elif op == "*":
        res += prod(v)

print(f"{res=}")


# C x L
chars: list[list[int]] = []
ops: list[str] = []

for l, line in enumerate(data.splitlines()):
    for c, char in enumerate(line):
        if l == 0:
            chars.append([])
        chars[c].append(char.strip())

chars.append([""])
res = 0
cur_op = ""
cur_vals = []
for idx, char in enumerate(chars):
    if idx == len(chars)-1 or all(c == "" for c in char):
        if cur_op == "+":
            res += sum(cur_vals)
        elif cur_op == "*":
            res += prod(cur_vals)
        cur_op = ""
        cur_vals = []
        continue

    if char[-1] != "":
        cur_op = char[-1]
    
    cur_vals.append(int("".join(char[:-1])))

print(f"{res=}")
