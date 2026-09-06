import heapq
from pathlib import Path


if __name__ == "__main__":
    data = (Path(__file__).parent / "day_16.txt").read_text()
    
    def get_char_idxs(char: str):
        return [(row, col) for row, line in enumerate(data.splitlines()) for col, c in enumerate(line) if c == char]

    wall_idxs = set(get_char_idxs("#"))
    start_idx = get_char_idxs("S")[0]
    end_idx = get_char_idxs("E")[0]

    def diff_from_orientation(orientation: str) -> tuple[int, int]:
        if orientation == "N":
            return (-1, 0)
        if orientation == "E":
            return (0, 1)
        if orientation == "S":
            return (1, 0)
        if orientation == "W":
            return (0, -1)
    
    def next_orientation(orientation: str, clockwise: bool) -> str:
        if orientation == "N":
            return "E" if clockwise else "W"
        if orientation == "E":
            return "S" if clockwise else "N"
        if orientation == "S":
            return "W" if clockwise else "E"
        if orientation == "W":
            return "N" if clockwise else "S"
        
    
    def is_valid_coord(i: int, j :int) -> bool:
        return (i, j) not in wall_idxs

    # Part 1, Dijkstra
    visited = set()
    # (cost, idx, orientation)
    queue = [(0, start_idx, "E")]
    while queue:
        # print(queue)
        # breakpoint()
        cost, (i, j), orientation = heapq.heappop(queue)
        if ((i, j), orientation) in visited:
            continue

        if (i, j) == end_idx:
            break

        # Possible actions:
        # 1. Move straight ahead (same orientation), cost 1
        di, dj = diff_from_orientation(orientation)
        ci, cj = i+di, j+dj
        if is_valid_coord(ci, cj):
            heapq.heappush(queue, (cost+1, (ci, cj), orientation))

        # 2. Rotate 90 deg clockwise, cost 1000
        heapq.heappush(queue, (cost+1000, (i, j), next_orientation(orientation, True)))

        # 3. Rotate 90 deg counterclockwise, cost 1000
        heapq.heappush(queue, (cost+1000, (i, j), next_orientation(orientation, False)))

        visited.add(((i, j), orientation))
    
    print(f"{cost=}")

    # Part 2, Dijkstra
    visited = set()
    cost = {(start_idx, "E"): 0}
    parents = {(start_idx, "E"): set()}
    # (cost, path, orientation)
    queue = [(0, start_idx, "E")]
    while queue:
        cost, (i, j), orientation = heapq.heappop(queue)

        if ((i, j), orientation) in visited:
            continue

        if (i, j) == end_idx:
            if cost in paths_to_end_by_cost:
                paths_to_end_by_cost[cost].append(path)
                continue
            if len(paths_to_end_by_cost) > 1:
                break
            paths_to_end_by_cost[cost] = [path]
            continue

        # Possible actions:
        # 1. Move straight ahead (same orientation), cost 1
        di, dj = diff_from_orientation(orientation)
        ci, cj = i+di, j+dj
        if is_valid_coord(ci, cj):
            heapq.heappush(queue, (cost+1, (*path, (ci, cj)), orientation))

        # 2. Rotate 90 deg clockwise, cost 1000
        heapq.heappush(queue, (cost+1000, path, next_orientation(orientation, True)))

        # 3. Rotate 90 deg counterclockwise, cost 1000
        heapq.heappush(queue, (cost+1000, path, next_orientation(orientation, False)))

        visited.add((path, orientation))