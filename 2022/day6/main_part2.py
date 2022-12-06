def find_marker(text: str, n: int) -> int:
    for i in range(len(text)):
        chars = [c for c in text[i : i + n]]
        if len(set(chars)) == n:
            return i + n


def read_datastream_buffer(path: str) -> str:
    with open(path, "r") as f:
        return f.read()


def main():
    datastream_buffer = read_datastream_buffer("input.txt")
    marker_pos = find_marker(datastream_buffer, n=14)
    print(f"The marker is at position {marker_pos}")


if __name__ == "__main__":
    main()
