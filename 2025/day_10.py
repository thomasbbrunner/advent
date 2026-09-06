from pathlib import Path
import re

data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""
# data = Path("day_10.txt").read_text()

lights_des = []
buttons_options = []
jolts_des = []
for line in data.splitlines():
    lights_str = re.findall(r"\[(.+)\]", line)
    button_str = re.findall(r"\(([\d,]+)\)", line)
    jolts_str = re.findall(r"\{([\d,]+)\}", line)

    lights_des.append(tuple(False if c == "." else True for c in lights_str[0]))
    buttons_options.append(tuple(tuple(int(c) for c in s.split(",")) for s in button_str))
    jolts_des.append(tuple(int(c) for c in jolts_str[0].split(",")))


# BFS
buttons_seq = []
for machine_idx in range(len(lights_des)):
    print(f"{machine_idx}/{len(lights_des)}")
    
    visited = set()
    lights_cur = [False for _ in lights_des[machine_idx]]
    queue = list(((b,), lights_cur.copy()) for b in buttons_options[machine_idx])

    while queue:
        buttons, lights = queue.pop(0)
        if frozenset(buttons) in visited:
            continue
        button = buttons[-1]
        for b in button:
            lights[b] = not lights[b]

        if all(l1 == l2 for l1, l2 in zip(lights, lights_des[machine_idx])):
            break

        for b in buttons_options[machine_idx]:
            if b == button:
                continue
            next_buttons = buttons + (b,)
            queue.append((next_buttons, lights.copy()))
        
        visited.add(frozenset(buttons))

    buttons_seq.append(buttons)

print(sum(len(b) for b in buttons_seq))


# BFS
buttons_seq = []
for machine_idx in range(len(jolts_des)):
    print(f"{machine_idx}/{len(jolts_des)}")
    # if machine_idx in (0,1): continue
    
    visited = set()
    jolts_cur = [0 for _ in jolts_des[machine_idx]]
    queue = list(((b,), jolts_cur.copy()) for b in buttons_options[machine_idx])

    while queue:
        buttons, jolts = queue.pop(0)
        if tuple(sorted(buttons)) in visited:
            continue
        button = buttons[-1]
        for b in button:
            jolts[b] += 1
        
        if any(j > j_des for j, j_des in zip(jolts, jolts_des[machine_idx])):
            visited.add(tuple(sorted(buttons)))
            continue

        if all(j == j_des for j, j_des in zip(jolts, jolts_des[machine_idx])):
            break

        for b in buttons_options[machine_idx]:
            next_buttons = buttons + (b,)
            if tuple(sorted(next_buttons)) in visited:
                continue
            queue.append((next_buttons, jolts.copy()))
        
        visited.add(tuple(sorted(buttons)))

    buttons_seq.append(buttons)

print(sum(len(b) for b in buttons_seq))