from pathlib import Path

data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""
data = Path("day_7.txt").read_text()

lines = data.splitlines()
line_len = len(lines[0])
num_lines = len(lines)
splitters = {(l, c) for l, line in enumerate(lines) for c, char in enumerate(line) if char == "^"}

beams = [(0, data.index("S"))]
splitters_visited = set()
while beams:
    beam = beams.pop()
    for i in range(beam[0], num_lines):
        if (i, beam[1]) not in splitters:
            continue
        if (i, beam[1]) in splitters_visited:
            break
        splitters_visited.add((i, beam[1]))
        beams.append((i, beam[1]-1))
        beams.append((i, beam[1]+1))
        break

print(f"{len(splitters_visited)=}")


splitters_visited = {}
def dfs(beam) -> int:    
    count = 0
    for i in range(beam[0], num_lines):
        if i == num_lines - 1:
            return 1
        elif (i, beam[1]) not in splitters:
            continue
        elif (i, beam[1]) in splitters_visited:
            return splitters_visited[(i, beam[1])]
        else:
            count += dfs((i, beam[1]-1)) + dfs((i, beam[1]+1))
            splitters_visited[(i, beam[1])] = count
            break

    return count

count = dfs((0, data.index("S")))

print(f"{count=}")
