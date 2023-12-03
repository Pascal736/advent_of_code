from dataclasses import dataclass


def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return f.read().splitlines()


def merge_to_single_line(data: list[str]) -> (str, int):
    return ("".join(data), len(data[0]))


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

        return bool(symbol_positions & adjacent_indices)


def get_gear_neighbour_values(
    gear_position: int, numbers: list[Number], line_length: int
) -> int:
    neighbours = []
    for number in numbers:
        if number.is_adjacent({gear_position}, line_length):
            neighbours.append(number)
        if len(neighbours) == 2:
            return neighbours[0].value * neighbours[1].value
    return 0


def get_positions_and_values(data: str, line_length: int) -> (list[Number], set[int]):
    start_index = None
    numbers = []
    gear_positions = set()

    for i, e in enumerate(data):
        if e.isnumeric() and (start_index is None):
            start_index = i
        elif not e.isnumeric() or (i % line_length == 0):
            if start_index is not None:
                end_index = i
                value = int(data[start_index:end_index])
                numbers.append(Number(value, start_index, end_index))
                start_index = None
        if e == "*":
            gear_positions.add(i)

    return numbers, gear_positions


def main():
    data = read_file("input.txt")
    data, line_length = merge_to_single_line(data)
    numbers, gear_positions = get_positions_and_values(data, line_length)
    total = sum(
        get_gear_neighbour_values(g, numbers, line_length) for g in gear_positions
    )
    print(f"The solution is {total}")  # Solution: 78236071


if __name__ == "__main__":
    main()
