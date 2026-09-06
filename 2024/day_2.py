from pathlib import Path


def is_safe(levels: list[int]) -> bool:
    diffs = [levels[i] - levels[i-1] for i in range(1, len(levels))]
    return all(1 <= d <= 3 for d in diffs) or all(-3 <= d <= -1 for d in diffs)


if __name__ == "__main__":
    data = Path("./2024/day_2.txt").read_text()

    num_safe = 0
    for report in data.splitlines():
        levels = [int(r) for r in report.split()]
        for i in range(len(levels)):
            levels_skip = levels[:i] + levels[i+1:]
            if is_safe(levels_skip):
                num_safe += 1
                break

    print(num_safe)
