from dataclasses import dataclass


@dataclass
class SectionRange:
    description: str

    @property
    def start(self):
        return int(self.description.split('-')[0])

    @property
    def end(self):
        return int(self.description.split('-')[1])

    def overlaps(self, other: 'SectionRange'):
        if set(range(self.start, self.end+1)).intersection(set(range(other.start, other.end+1))):
            return True
        else:
            return False


def read_sections(path: str) -> list[tuple[SectionRange]]:
    with open(path, 'r') as f:
        lines = f.readlines()
    out = []
    for line in lines:
        line = line.strip().split(',')
        out.append((SectionRange(line[0]), SectionRange(line[1])))

    return out


def main():
    sections_list = read_sections("input.txt")
    n_overlaps = 0
    for sections in sections_list:
        s1, s2 = sections
        if s1.overlaps(s2):
            n_overlaps += 1
    print(n_overlaps)


if __name__ == '__main__':
    main()
