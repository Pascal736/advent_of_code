import string
from dataclasses import dataclass
from functools import reduce


PRIORITIES = {
    **{l: i for i, l in enumerate(string.ascii_lowercase, start=1)},
    **{l: i for i, l in enumerate(string.ascii_uppercase, start=27)},
}


@dataclass
class Rucksack:
    items: list[str]

    @property
    def first_compartment(self) -> set[str]:
        middle = len(self.items) // 2
        return set(self.items[:middle])

    @property
    def second_compartment(self) -> set[str]:
        middle = len(self.items) // 2
        return set(self.items[middle:])

    @property
    def common_item(self) -> str:
        return self.first_compartment.intersection(self.second_compartment).pop()

    def get_common_items(self, *other: 'Rucksack') -> set[str]:
        return reduce(lambda x, y: set(x).intersection(set(y)), [self.items, *(o.items for o in other)])


def sum_of_priorities(badges: list[set[str]]) -> int:
    return sum(PRIORITIES[b.pop()] for b in badges)


def find_badges(rucksacks: list[list[Rucksack]]) -> list[str]:
    badges = []
    for group in rucksacks:
        badge = group[0].get_common_items(*group[1:])
        print(badge)
        badges.append(badge)
    return badges


def get_rucksacks_from_input(path: str, group_size: int) -> list[list[Rucksack]]:
    with open(path, "r") as f:
        user_input = f.readlines()
    out = []
    group = []
    for i, line in enumerate(user_input):
        if (i % group_size == 0) and (i != 0):
            out.append(group)
            assert len(group) == 3
            group = []
        line = line.strip("\n")
        rucksack = Rucksack(line)
        group.append(rucksack)
    out.append(group)
    return out


def main():
    rucksacks = get_rucksacks_from_input("input.txt", group_size=3)
    badges = find_badges(rucksacks)
    priorities = sum_of_priorities(badges)
    print(priorities)


if __name__ == "__main__":
    main()
