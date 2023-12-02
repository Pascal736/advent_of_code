from dataclasses import dataclass
from collections import defaultdict


LIMITS = {"red": 12, "green": 13, "blue": 14}


@dataclass
class Game:
    id: int
    red: int
    green: int
    blue: int

    @classmethod
    def from_line(cls, line: str) -> "Game":
        id_ = int(line.split(":")[0].split(" ")[-1])
        draws = line.split(":")[-1]

        color_amount = defaultdict(float)

        for draw in draws.split(";"):
            colors = draw.split(",")
            for color in colors:
                _, number, color = color.split(" ")
                color = color.strip()

                color_amount[color] = max(color_amount[color], int(number))

        return cls(id=id_, **color_amount)

    def is_possible(self, limits: dict[str, int]) -> bool:
        for color, maximum in limits.items():
            if getattr(self, color) > maximum:
                return False
        return True


def read_file(path) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def main():
    lines = read_file("input.txt")
    games = [Game.from_line(l) for l in lines]
    total = sum({g.id for g in games if g.is_possible(LIMITS)})
    print(f"The answer is {total}")  # Solution: 2486


if __name__ == "__main__":
    main()
