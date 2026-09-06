from pathlib import Path
import re


if __name__ == "__main__":
    data = Path("./2024/day_3.txt").read_text()
    pattern = re.compile(r"mul\((\d+)\,(\d+)\)|don't\(\)|do\(\)")
    matches = pattern.finditer(data)

    res = 0
    enabled = True
    for match in matches:
        if match[0] == "do()":
            enabled = True
            continue
        if match[0] == "don't()":
            enabled = False
            continue
        
        if enabled:
            a, b = match[1], match[2]
            res += int(a)*int(b)
    
    print(res)