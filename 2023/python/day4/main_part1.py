from dataclasses import dataclass


@dataclass
class Card:
    winning_numbers: list[int]
    numbers: list[int]

    @classmethod
    def from_line(cls, line: str):
        winning_numbers, numbers = line.split("|")
        winning_numbers = [
            int(x) for x in winning_numbers.split(":")[-1].split(" ") if x
        ]
        numbers = [int(x) for x in numbers.split(" ") if x]

        return cls(winning_numbers, numbers)

    def get_points(self) -> int:
        points = 0
        for number in self.numbers:
            if number in self.winning_numbers:
                if not points:
                    points = 1
                else:
                    points *= 2
        return points


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.read().splitlines()


def get_cards(lines: list[str]) -> list[Card]:
    return [Card.from_line(l) for l in lines]


def main():
    data = read_file("input.txt")
    cards = get_cards(data)
    total = sum(c.get_points() for c in cards)
    print(f"The solution is {total}")  # Solution: 24175


if __name__ == "__main__":
    main()
