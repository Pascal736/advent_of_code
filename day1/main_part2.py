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
    return sorted(count, key=lambda x: x[1], reverse=True)[:3]

def sum_of_top_three(count: list[tuple[int, int]]) -> int:
    return sum([x[1] for x in count])


def main():
    content = read_input('./input.txt')
    count = count_calories(content)
    top_three= find_best_elf(count)
    top_3_calories = sum_of_top_three(top_three)
    print(top_3_calories)

if __name__ == '__main__':
    main()