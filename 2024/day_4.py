from pathlib import Path
import numpy as np

def check_xmas(data: np.ndarray) -> bool:
    s = ''.join(data)
    return s == "XMAS" or s == "SAMX"


if __name__ == "__main__":
    data = Path("./2024/day_4.txt").read_text()
    data = np.array([[c for c in line] for line in data.split()])
    num_lines = len(data)
    line_len = len(data[0])
    num_matches = 0

    # Horizontal
    for i in range(num_lines):
        for j in range(line_len-3):
            if check_xmas(data[i,j:j+4]):
                num_matches += 1

    # Vertical
    for i in range(line_len):
        for j in range(num_lines-3):
            if check_xmas(data[j:j+4,i]):
                num_matches += 1


    # Diagonal \
    for i in range(num_lines-3):
        for j in range(line_len-3):
            idxs = ((i, j), (i+1, j+1), (i+2, j+2), (i+3, j+3))
            d = (data[idx] for idx in idxs)
            if check_xmas(d):
                num_matches += 1

    # Diagonal /
    for i in range(num_lines-3):
        for j in range(3, line_len):
            idxs = ((i, j), (i+1, j-1), (i+2, j-2), (i+3, j-3))
            d = (data[idx] for idx in idxs)
            if check_xmas(d):
                num_matches += 1

    print(f"{num_matches=}")

    # X-MAS
    num_matches = 0
    for i in range(num_lines-2):
        for j in range(line_len-2):
            d = [data[i+k,j+k] for k in range(3)] + [data[i+2-k,j+k] for k in range(3)]
            s = "".join(d)
            if s in ("MASMAS", "MASSAM", "SAMMAS", "SAMSAM"):
                num_matches += 1

    print(f"{num_matches=}")