from pathlib import Path

data = Path("day_5.txt").read_text()
# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32
# """

ranges, ingredients = data.split("\n\n")
ranges = ranges.split()
ingredients = ingredients.split()

ranges = [tuple(int(i) for i in r.split("-")) for r in ranges]
ingredients = [int(i) for i in ingredients]

num_fresh = 0
for ingredient in ingredients:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            num_fresh += 1
            break

print(f"{num_fresh=}")

ranges = sorted(ranges)
num_fresh = 0
min_cur, max_cur = -1, -1
for r in ranges:
    if min_cur <= r[0] <= max_cur:
        if r[1] <= max_cur:
            continue
        num_fresh += r[1] - max_cur
        max_cur = r[1]
    else:
        num_fresh += r[1] - r[0] + 1
        min_cur = r[0]
        max_cur = r[1]

print(f"{num_fresh=}")
