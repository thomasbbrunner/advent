import math
from pathlib import Path
import itertools


data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""
data = Path("day_8.txt").read_text()

boxes = []
for line in data.splitlines():
    boxes.append(tuple(int(coord) for coord in line.split(",")))

num_boxes = len(boxes)
distances = [[float("inf") for _ in range(num_boxes)] for _ in range(num_boxes)]
for i in range(num_boxes):
    for j in range(num_boxes):
        if i >= j:
            continue
        distances[i][j] = (boxes[i][0] - boxes[j][0])**2 + (boxes[i][1] - boxes[j][1])**2 + (boxes[i][2] - boxes[j][2])**2

combinations = itertools.combinations(range(num_boxes), 2)
indices = sorted(combinations, key=lambda x: distances[x[0]][x[1]])

circuits = []
last_boxes = None
for box1, box2 in indices:
    circuit_box1 = None
    circuit_box2 = None
    for circuit in circuits:
        if box1 in circuit:
            circuit_box1 = circuit
        if box2 in circuit:
            circuit_box2 = circuit
    if circuit_box1 and circuit_box1 == circuit_box2:
        continue
    elif circuit_box1 and circuit_box2:
        circuits.remove(circuit_box1)
        circuits.remove(circuit_box2)
        circuits.append(circuit_box1 | circuit_box2)
        last_boxes = (box1, box2)
    elif circuit_box1:
        circuit_box1.add(box2)
        last_boxes = (box1, box2)
    elif circuit_box2:
        circuit_box2.add(box1)
        last_boxes = (box1, box2)
    else:
        circuits.append({box1, box2})

# Part 1 with indices[:1000]
# sorted_circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
# res = math.prod([len(c) for c in sorted_circuits[:3]])
# print(f"{res=}")

print(boxes[last_boxes[0]][0]*boxes[last_boxes[1]][0])

