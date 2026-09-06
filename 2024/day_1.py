from pathlib import Path


if __name__ == "__main__":
    data = Path("./2024/day_1.txt")
    l1, l2 = [], []

    for line in data.open("r"):
        n1, n2 = line.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

    l1.sort()
    l2.sort()

    diff = 0
    for n1, n2 in zip(l1, l2):
        diff += abs(n1 - n2)

    print(diff)

    score = 0
    counts: dict[int, int] = {}
    for n1 in l1:
        if n1 not in counts:
            counts[n1] = l2.count(n1)
        score += n1 * counts[n1]

    print(score)
