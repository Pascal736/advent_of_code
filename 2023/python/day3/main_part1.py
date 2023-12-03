from dataclasses import dataclass
from pprint import pprint


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.readlines()


def merge_to_single_line(data: list[str]) -> (str, int):
    line_length = len(data[0].strip())
    return ("".join(data).replace("\n", ""), line_length)


@dataclass
class Number:
    value: int
    start_index: int
    end_index: int

    def is_adjacent(self, symbol_positions: set[int], line_length: int) -> bool:
        neighbours = set([self.start_index - 1, self.end_index])
        upper_neighbours = set(
            range(self.start_index - line_length - 1, self.end_index - line_length + 1)
        )
        lower_neighbours = set(
            range(self.start_index + line_length - 1, self.end_index + line_length + 1)
        )
        adjacent_indices = neighbours | lower_neighbours | upper_neighbours

        if symbol_positions & adjacent_indices:
            return True
        else:
            return False


def get_positions_and_values(data: str, line_length: int) -> (list[Number], set[int]):
    start_index = None
    numbers = []
    symbol_positions = set()

    for i, e in enumerate(data):
        if e.isnumeric() and (start_index is None):
            start_index = i
        elif not e.isnumeric() or (i % line_length == 0):
            if start_index is not None:
                end_index = i
                value = int(data[start_index:end_index])
                numbers.append(Number(value, start_index, end_index))
                start_index = None
        if e != "." and not e.isnumeric():
            symbol_positions.add(i)

    return numbers, symbol_positions


def main():
    data = read_file("input.txt")
    data, line_length = merge_to_single_line(data)
    numbers, symbol_positions = get_positions_and_values(data, line_length)
    total = sum(
        n.value for n in numbers if n.is_adjacent(symbol_positions, line_length)
    )
    print(f"The solution is {total}")  # Solution: 533775


if __name__ == "__main__":
    main()
