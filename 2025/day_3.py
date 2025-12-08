
from itertools import count
from pathlib import Path

data = Path("day_3.txt").read_text().splitlines()
# data = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]
# data = ["987654", "811119", "234278", "818921"]


joltages = []
for bank in data:
    dig1 = int(bank[0])
    dig2 = int(bank[1])
    for jolt_str in bank[2:]:
        jolt = int(jolt_str)

        if dig2 > dig1:
            dig1 = dig2
            dig2 = jolt

        elif jolt > dig2:
            dig2 = jolt

    joltages.append(dig1*10 + dig2)

print(f"{sum(joltages)=}")


num_digits = 12
joltages = []
for bank in data:
    digs = []
    
    for idx, jolt_str in enumerate(bank):
        jolt = int(jolt_str)
        remaining = len(bank) - idx

        while True:
            if remaining <= num_digits - len(digs):
                digs.append(jolt)
                break

            elif digs and jolt > digs[-1]:
                digs.pop()

            elif len(digs) < num_digits:
                digs.append(jolt)
                break
            
            else:
                break

    joltages.append(sum([d*10**i for i, d in enumerate(reversed(digs))]))

print(f"{joltages=}")
print(f"{sum(joltages)=}")
