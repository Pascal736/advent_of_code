from dataclasses import dataclass
from collections import deque


@dataclass
class Card:
    id: int
    winning_numbers: set[int]
    numbers: set[int]

    @classmethod
    def from_line(cls, line: str):
        winning_numbers, numbers = line.split("|")
        id_ = int(winning_numbers.split(":")[0].split(" ")[-1])
        winning_numbers = {
            int(x) for x in winning_numbers.split(":")[-1].split(" ") if x
        }
        numbers = {int(x) for x in numbers.split(" ") if x}

        return cls(id_, winning_numbers, numbers)

    @property
    def n_matches(self) -> int:
        return len(self.winning_numbers & self.numbers)


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.read().splitlines()


def get_cards(lines: list[str]) -> dict[int, Card]:
    return {i: Card.from_line(l) for i, l in enumerate(lines, start=1)}


def main():
    data = read_file("input.txt")
    cards_mapping = get_cards(data)
    total_cards = 0
    remaining_cards = deque(cards_mapping.values())
    while remaining_cards:
        card = remaining_cards.popleft()
        total_cards += 1
        for match in range(1, card.n_matches + 1):
            id_ = card.id + match
            remaining_cards.append(cards_mapping[id_])

    print(f"The solution is {total_cards}") # Solution 18846301


if __name__ == "__main__":
    main()
