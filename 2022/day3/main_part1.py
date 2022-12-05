import string
from dataclasses import dataclass


PRIORITIES = {
    **{l: i for i, l in enumerate(string.ascii_lowercase, start=1)},
    **{l: i for i, l in enumerate(string.ascii_uppercase, start=27)},
}


@dataclass
class Rucksack:
    first_compartment: set[str]
    second_compartment: set[str]

    @property
    def common_item(self) -> str:
        return self.first_compartment.intersection(self.second_compartment).pop()


def sum_of_priorities(rucksacks: list[Rucksack]) -> int:
    return sum(PRIORITIES[r.common_item] for r in rucksacks)


def get_rucksacks_from_input(path: str) -> list[Rucksack]:
    with open(path, "r") as f:
        user_input = f.readlines()
    out = []
    for line in user_input:
        line = line.strip("\n")
        middle = len(line) // 2
        rucksack = Rucksack(
            first_compartment=set(line[:middle]), second_compartment=set(line[middle:])
        )
        out.append(rucksack)
    return out


def main():
    rucksacks = get_rucksacks_from_input("input.txt")
    priorities = sum_of_priorities(rucksacks)
    print(priorities)


if __name__ == "__main__":
    main()
