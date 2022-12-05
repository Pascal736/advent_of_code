from functools import total_ordering


@total_ordering
class Move:
    def __init__(self, value: str | tuple, mapping: dict[str, str]) -> None:
        self.hand = mapping[value]

    def __gt__(self, other: 'Move'):
        if self.hand == 'Rock' and other.hand == 'Paper':
            return False
        if self.hand == 'Rock' and other.hand == 'Scissors':
            return True
        if self.hand == 'Paper' and other.hand == 'Scissors':
            return False
        if self.hand == 'Paper' and other.hand == 'Rock':
            return True
        if self.hand == 'Scissors' and other.hand == 'Rock':
            return False
        if self.hand == 'Scissors' and other.hand == 'Paper':
            return True

    def __eq__(self, other: 'Move') -> bool:
        if self.hand == other.hand:
            return True
        else:
            return False


def get_points_for_move(x: Move, y: Move) -> int:
    if x == y:
        result_points = 3
    elif x > y:
        result_points = 6
    else:
        result_points = 0

    move_points = point_mapping[x.hand]
    return result_points + move_points


def read_input(path: str) -> list[str]:
    with open(path, 'r') as f:
        rounds = f.readlines()
    return [(Move(x[0], mapping_other), Move((x[0],  x[2]), mapping_self)) for x in rounds]


mapping_self = {
    ('A', 'X'): 'Scissors',
    ('A', 'Y'): 'Rock',
    ('A', 'Z'): 'Paper',
    ('B', 'X'): 'Rock',
    ('B', 'Y'): 'Paper',
    ('B', 'Z'): 'Scissors',
    ('C', 'X'): 'Paper',
    ('C', 'Y'): 'Scissors',
    ('C', 'Z'): 'Rock',
}
mapping_other = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
}

point_mapping = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
}


def main():
    text_input = read_input('input.txt')
    scrore = 0
    for x, y in text_input:
        scrore += get_points_for_move(y, x)

    print(scrore)


if __name__ == '__main__':
    main()
