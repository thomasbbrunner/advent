from pathlib import Path
from itertools import product

if __name__ == "__main__":
    data = (Path(__file__).parent / "day_7.txt").read_text()

    equations = {}
    for line in data.splitlines():
        split = line.split(":")
        operand, vals = split[0], split[1]
        equations[int(operand)] = tuple(int(val) for val in vals.split())
    
    operators = ("add", "mul")
    for test, operands in equations.items():
        product(operators, len(operands))