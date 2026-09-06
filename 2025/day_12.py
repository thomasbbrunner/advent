from math import prod
import re
from pathlib import Path

data = """0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""
data = Path("day_12.txt").read_text()

shapes = []
shapes_comb = []
regions_sizes = []
regions_shapes = []

for d in data.split("\n\n"):
    # Check if shape.
    if re.match(r"\d:", d):
        shape_raw = []
        for l in d.split("\n")[1:]:
            shape_raw.append([])
            for c in l:
                shape_raw[-1].append(c)
        shape = tuple((i, j) for i in range(len(shape_raw)) for j in range(len(shape_raw[0])) if shape_raw[i][j] == "#")
        shapes.append(shape)

    # Check if regions.
    else:
        for l in d.split("\n"):
            match = re.match(r"(\d+)x(\d+): (.+)", l)
            regions_sizes.append((int(match[1]), int(match[2])))
            regions_shapes.append(tuple(int(m) for m in match[3].split()))

rot_90 = {
    (0, 0): (0, 2),
    (0, 1): (1, 2),
    (0, 2): (2, 2),
    (1, 0): (0, 1),
    (1, 1): (1, 1),
    (1, 2): (2, 1),
    (2, 0): (0, 0),
    (2, 1): (1, 0),
    (2, 2): (2, 0),
}
hflip = {
    (0, 0): (0, 2),
    (0, 1): (0, 1),
    (0, 2): (0, 0),
    (1, 0): (1, 2),
    (1, 1): (1, 1),
    (1, 2): (1, 0),
    (2, 0): (2, 2),
    (2, 1): (2, 1),
    (2, 2): (2, 0),
}

for shape in shapes:
    # 4 rotations * 2 flips
    shape_90 = tuple(sorted(rot_90[coord] for coord in shape))
    shape_180 = tuple(sorted(rot_90[coord] for coord in shape_90))
    shape_270 = tuple(sorted(rot_90[coord] for coord in shape_180))
    assert tuple(sorted(shape)) == tuple(sorted(rot_90[coord] for coord in shape_270))
    shape_flip = tuple(sorted(hflip[coord] for coord in shape))
    assert tuple(sorted(shape)) == tuple(sorted(hflip[coord] for coord in shape_flip))
    shape_90_flip = tuple(sorted(hflip[coord] for coord in shape_90))
    shape_180_flip = tuple(sorted(hflip[coord] for coord in shape_180))
    shape_270_flip = tuple(sorted(hflip[coord] for coord in shape_270))
    shapes_comb.append(tuple(set((shape, shape_90, shape_180, shape_270, shape_flip, shape_90_flip, shape_180_flip, shape_270_flip))))


regions_fits = [None for _ in range(len(regions_sizes))]
for ridx in range(len(regions_sizes)):
    rsize = regions_sizes[ridx]
    rshapes = regions_shapes[ridx]

    area_region = prod(rsize)
    # Sanity check: is the region large enough to fit all shapes?
    area_shapes = sum((num*len(shapes[idx]) for idx, num in enumerate(rshapes)))
    if area_region < area_shapes:
        regions_fits[ridx] = False
        continue

    # Sanity check: is the region so large, that the shapes will always fit?
    max_area_shapes = 9*sum(rshapes)
    if area_region >= max_area_shapes:
        regions_fits[ridx] = True
        continue

print(f"{sum(regions_fits)=}")
