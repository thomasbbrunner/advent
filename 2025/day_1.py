from pathlib import Path



data = Path("day_1.txt")
with data.open("r") as f:
    lines = f.readlines()

idx = 50
counts = 0

for line in lines:
    sign = 1 if line[0] == "R" else -1
    val = int(line[1:])
    idx += sign * val
    idx %= 100
    if idx == 0:
        counts += 1

print(f"Part 1: {counts=}")

idx = 50
wrap = 100
counts = 0
for line in lines:
    sign = 1 if line[0] == "R" else -1
    val = int(line[1:])
    for _ in range(val):
        idx += sign
        idx %= wrap
        if idx == 0: counts += 1
print(f"Part 2: {counts=}")
