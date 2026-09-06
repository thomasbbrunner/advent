from pathlib import Path


if __name__ == "__main__":
    data = (Path(__file__).parent / "day_1.txt").read_text()
    lines = data.splitlines()

    # Part 1
    numbers = set(str(i) for i in range(0, 10))
    values = []
    for line in lines:
        first_digit, last_digit = None, None
        for char in line:
            if char in numbers:
                first_digit = char
                break

        for char in reversed(line):
            if char in numbers:
                last_digit = char
                break
        
        values.append(int(first_digit + last_digit))

    print(f"{sum(values)}")

    # Part 2
    word_to_number = {
         "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }
    values = []
    for line in lines:
        digits = []

        for i, char in enumerate(line):
            if char.isdigit():
                digits.append(char)
                continue

            for word, digit in word_to_number.items():
                if line.startswith(word, i):
                    digits.append(digit)
                    break

        first_digit, last_digit = digits[0], digits[-1]
        
        values.append(int(first_digit + last_digit))

    print(f"{sum(values)}")
