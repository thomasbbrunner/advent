from itertools import count
from pathlib import Path

data = Path("day_2.txt").read_text()
# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
ranges = data.strip().split(",")


nums = []
for r in ranges:
    minv, maxv = r.split("-")
    minv = int(minv)
    maxv = int(maxv)
    for num in range(minv, maxv+1):
        num_str = str(num)
        if len(num_str) % 2 != 0:
            continue
        if num_str[:len(num_str)//2] != num_str[len(num_str)//2:]:
            continue
        nums.append(num)
print(f"{sum(nums)=}")


nums = []
for r in ranges:
    minv, maxv = r.split("-")
    minv = int(minv)
    maxv = int(maxv)

    for num in range(minv, maxv+1):
        num_str = str(num)

        for repeated in count(2):
            if repeated > len(num_str):
                break
            if len(num_str) % repeated != 0:
                continue
            part_len = len(num_str)//repeated
            part = num_str[:part_len]

            for other_part in (num_str[part_idx*part_len:(part_idx+1)*part_len] for part_idx in range(1, repeated)):
                if other_part != part:
                    break
            else:
                nums.append(num)
                break

print(f"{sum(nums)=}")
