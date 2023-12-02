from dataclasses import dataclass
from collections import defaultdict


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

    def power(self) -> int:
        return max(self.green, 1) * max(self.blue, 1) * max(self.red, 1)


def read_file(path) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def main():
    lines = read_file("input.txt")
    games = [Game.from_line(l) for l in lines]
    total = sum([g.power() for g in games])
    print(f"The answer is {total}")


if __name__ == "__main__":
    main()
