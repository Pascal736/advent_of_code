def read_input(path: str) -> list[int]:
    with open(path,"r" ) as f:
        content = f.readlines()
    content = [int(x.strip()) if x != '\n' else '' for x in content]
    return content

def count_calories(content: list) -> list(tuple([int, int])):
    out = []
    i = 1
    c = 0
    for calories in content:
        if not calories:
            out.append((i, c))
            c = 0
            i += 1
            continue
        c += calories
    return out

def find_best_elf(count: list[tuple[int, int]]) -> tuple[int, int]:
    return sorted(count, key=lambda x: x[1])[-1]



def main():
    content = read_input('./input.txt')
    count = count_calories(content)
    best_elf, max_calories = find_best_elf(count)
    print(f"The elf with the most calories is number {best_elf} with a total amount of calories of {max_calories}")

if __name__ == '__main__':
    main()