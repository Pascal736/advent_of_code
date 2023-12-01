def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


CONVERT_NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_first_number(line: str) -> str:
    for i, e in enumerate(line):
        if e.isnumeric():
            return str(e)
        for number_text, number in CONVERT_NUMBERS.items():
            if number_text in line[: i + 1]:
                return number


def find_last_number(line: str) -> str:
    for i, e in zip(range(len(line)), line[::-1]):
        if e.isnumeric():
            return str(e)
        for number_text, number in CONVERT_NUMBERS.items():
            if number_text in line[-i - 1 :]:
                return number


def main():
    lines = read_file("input.txt")
    total = 0
    for line in lines:
        total += int(find_first_number(line) + find_last_number(line))

    print(f"The result is: {total}")  # Solution: 54824


if __name__ == "__main__":
    main()
