from itertools import cycle
from pathlib import Path


if __name__ == "__main__":
    data = Path("./2024/day_6.txt").read_text()

    obstacles = set()
    start_pos = None
    lines = data.splitlines()
    grid_size = (len(lines), len(lines[0]))
    for line_idx, line in enumerate(lines):
        obs_idx = -1
        while True:
            try:
                obs_idx = line.index("#", obs_idx+1)
            except ValueError:
                break
            obstacles.add((line_idx, obs_idx))

        try:
            start_idx = line.index("^")
        except ValueError:
            continue
        start_pos = (line_idx, start_idx)
    
    def patrol(new_obstacle: tuple[int, int] | None) -> tuple[set[tuple[int, int]], bool]:
        dirs = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))

        cur_pos = start_pos
        cur_dir = next(dirs)
        is_cyclic = False

        visited = set()
        visited_with_dir = set()

        while True:
            visited.add(cur_pos)
            visited_with_dir.add((cur_pos, cur_dir))
            next_pos = (cur_pos[0] + cur_dir[0], cur_pos[1] + cur_dir[1])

            if next_pos in obstacles or (new_obstacle is not None and next_pos == new_obstacle):
                cur_dir = next(dirs)
                continue
                
            if (next_pos, cur_dir) in visited_with_dir:
                is_cyclic = True
                break

            if not (0 <= next_pos[0] < grid_size[0] and 0 <= next_pos[1] < grid_size[1]):
                break
                
            cur_pos = next_pos

        return visited, is_cyclic
    
    visited, _ = patrol(None)
    print(len(visited))

    test_set = visited.copy()
    num_cycles = 0
    for pos in test_set:
        _, is_cyclic = patrol(pos)
        num_cycles += is_cyclic

    print(num_cycles)
