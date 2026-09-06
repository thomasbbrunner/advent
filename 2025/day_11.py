from collections import defaultdict
from pathlib import Path

data = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""
data = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""
data = Path("day_11.txt").read_text()

graph = defaultdict(list)
for line in data.splitlines():
    if not line: continue
    key, rem = line.split(":")
    values = rem.strip().split(" ")
    graph[key] = values

# DFS
paths = []
stack = [("you", ())]
while stack:
    node, path = stack.pop(-1)
    if node == "out":
        paths.append(path)
        continue
    for next_node in graph[node]:
        stack.append((next_node, path + (next_node,)))

print(f"{len(paths)=}")


# DFS part 2
# Path is: svr -> fft -> dac -> out
visited = {}
def dfs(node, visited_fft, visited_dac, num_paths, goal):
    if node == goal:
        return 1 if visited_fft and visited_dac else 0
    if (node, visited_fft, visited_dac) in visited:
        return visited[(node, visited_fft, visited_dac)]
    if node == "fft":
        visited_fft = True
    if node == "dac":
        visited_dac = True
    num_paths = sum(dfs(next_node, visited_fft, visited_dac, num_paths, goal) for next_node in graph[node])
    visited[(node, visited_fft, visited_dac)] = num_paths
    return num_paths

num_paths = dfs("svr", False, False, 1, "out")
print(f"{num_paths=}")
