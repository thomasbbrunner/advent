from functools import cache
from pathlib import Path

class Node:
    def __init__(self, pattern: str, subdesign: str) -> None:
        self.pattern = pattern
        self.subdesign = subdesign
        self.children = []
    
    def matches(self) -> bool:
        return self.subdesign.startswith(self.pattern)

    def remaining_subdesign(self) -> str:
        return self.subdesign[len(self.pattern):]


if __name__ == "__main__":
    data = (Path(__file__).parent / "day_19.txt").read_text()
#     data = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb
# """

    lines = data.splitlines()

    patterns_line = lines[0]
    patterns = set(p.strip() for p in patterns_line.split(","))

    designs = [design for design in lines[2:]]

    # Part 1, DFS
    @cache
    def dfs(subdesign: str) -> bool:
        for pattern in patterns:
            if not subdesign.startswith(pattern):
                continue
            if subdesign == pattern:
                return True
            if dfs(subdesign.removeprefix(pattern)):
                return True
        else:
            return False     

    matches = [False for _ in designs]
    for idx, design in enumerate(designs):
        matches[idx] = dfs(design)

    print(sum(matches))

    # Part 1, DP
    matches = 0
    for design in designs:
        dp = [False for _ in range(len(design)+1)]
        dp[0] = True

        for i in range(len(dp)):
            if not dp[i]:
                continue
            subdesign = design[i:]
            for pattern in patterns:
                if subdesign.startswith(pattern):
                    dp[i+len(pattern)] = True

        matches += dp[-1]
    
    print(matches)

    # Part 2, DFS

    @cache
    def dfs(subdesign: str) -> int:
        num_submatches = 0
        for pattern in patterns:
            if not subdesign.startswith(pattern):
                continue
            if subdesign == pattern:
                num_submatches += 1
                continue
            num_submatches += dfs(subdesign.removeprefix(pattern))

        return num_submatches     

    matches = [False for _ in designs]
    for idx, design in enumerate(designs):
        matches[idx] = dfs(design)

    print(sum(matches))

    # Part 2, DP
    matches = 0
    for design in designs:
        dp = [0 for _ in range(len(design)+1)]
        dp[0] = 1

        for i in range(len(dp)):
            if dp[i] == 0:
                continue
            subdesign = design[i:]
            for pattern in patterns:
                if subdesign.startswith(pattern):
                    dp[i+len(pattern)] += dp[i]

        matches += dp[-1]
    
    print(matches)
