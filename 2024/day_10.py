from collections import deque
from functools import cache
from pathlib import Path


if __name__ == "__main__":
    data = (Path(__file__).parent / "day_10.txt").read_text()
#     data = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# """

    def get_idxs_by_value(val: int) -> list[tuple[int, int]]:
        return [(i, j) for j in range(len(tmap[0])) for i in range(len(tmap)) if tmap[i][j] == val]

    tmap = [[int(char) for char in line] for line in data.splitlines()]
    heads = get_idxs_by_value(0)
    heads.sort()

    # Part 1, BFS
    scores = []
    for head in heads:
        found_ends = set()
        visited = set()
        queue = deque([head])
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue

            node_val = tmap[i][j]
            if node_val == 9:
                found_ends.add((i, j))
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)): 
                if not (0 <= i+di < len(tmap) and 0 <= j+dj < len(tmap[0])):
                    continue
                if tmap[i+di][j+dj] == node_val + 1:
                    queue.append((i+di, j+dj))

        scores.append(len(found_ends))

    print(f"{sum(scores)=}")

    # Part 1, DP
    dp = [[set() for _ in range(len(tmap[0]))] for _ in range(len(tmap))]
    idxs = get_idxs_by_value(9)
    for i, j in idxs:
        dp[i][j].add((i, j))

    for val in range(8, -1, -1):
        idxs = get_idxs_by_value(val)
        for i, j in idxs:
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if not (0 <= i+di < len(tmap) and 0 <= j+dj < len(tmap[0])):
                    continue
                if tmap[i+di][j+dj] == val + 1:
                    dp[i][j] |= dp[i+di][j+dj]
    
    idxs = get_idxs_by_value(0)
    print(f"{sum(len(dp[i][j]) for i, j in idxs)=}")

    # Part 2, BFS
    ratings = []
    for head in heads:
        found_paths = set()
        visited = set()
        queue = deque([(head, (head,))])
        while queue:
            (i, j), path = queue.popleft()
            if ((i, j), path) in visited:
                continue

            node_val = tmap[i][j]
            if node_val == 9:
                found_paths.add(path)
                continue

            visited.add(((i, j), path))

            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ci, cj = i+di, j+dj
                if not (0 <= ci < len(tmap) and 0 <= cj < len(tmap[0])):
                    continue

                if tmap[ci][cj] == node_val + 1:
                    queue.append(((ci, cj), (*path, (ci, cj))))

        ratings.append(len(found_paths))

    print(f"{sum(ratings)=}")

    # Part 2, DP
    dp = [[0 for _ in range(len(tmap[0]))] for _ in range(len(tmap))]
    idxs = get_idxs_by_value(9)
    for i, j in idxs:
        dp[i][j] = 1

    for val in range(8, -1, -1):
        idxs = get_idxs_by_value(val)
        for i, j in idxs:
            for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                ci, cj = i+di, j+dj
                if not (0 <= ci < len(tmap) and 0 <= cj < len(tmap[0])):
                    continue
                if val + 1 != tmap[ci][cj]:
                    continue
                dp[i][j] += dp[ci][cj]

    idxs = get_idxs_by_value(0)
    ratings = [dp[i][j] for i, j in idxs]
    print(f"{sum(ratings)=}")
