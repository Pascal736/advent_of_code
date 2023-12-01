def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def create_number_for_line(line: str) -> int:
    digits = [x for x in line if x.isdigit()]
    return int(digits[0] + digits[-1])


def main():
    lines = read_file("input.txt")
    numbers = [create_number_for_line(line) for line in lines]
    total = sum(numbers)
    print(f"The result is: {total}")  # Solution: 55386


if __name__ == "__main__":
    main()
