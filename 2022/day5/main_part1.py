from dataclasses import dataclass
from collections import defaultdict


@dataclass
class CrateStacks:
    crates_diagram: str
    moves: list['CrateMove']
    stacks = defaultdict(list)
    
    def __post_init__(self):
        for row in self.crates_diagram:
            for j, e in enumerate(row):
                if e.isalpha():
                    self.stacks[j].append(e)
                if e.isnumeric():
                    self.stacks[int(e)] = self.stacks[j][::-1]
                    if j != int(e):
                        del self.stacks[j]
    
    def execute_moves(self):
        for move in self.moves:
            for _ in range(move.n_elements_to_move):
                e = self.stacks[move.source_crate].pop()
                self.stacks[move.target_crate].append(e)

    def get_solution(self):
        return ''.join(v[-1] for v in self.stacks.values())
        
@dataclass
class CrateMove:
    command: str

    @property
    def source_crate(self) -> int:
        return int(self.command.split(' ')[3])

    @property
    def target_crate(self) -> int:
        return int(self.command.split(' ')[-1])

    @property
    def n_elements_to_move(self) -> int:
        return int(self.command.split(' ')[1])


def read_user_input(path) -> CrateStacks :
    with open("input.txt", "r") as f:
        file = f.read()

    moves = file[file.index('move'):].split('\n')
    moves = [CrateMove(x) for x in moves]
    crates_diagram = file[:file.index('move')][:-2].split("\n")

    return CrateStacks(crates_diagram, moves=moves) 

def main():
    crate_stacks = read_user_input('input.txt')
    crate_stacks.execute_moves()
    print(crate_stacks.get_solution())

if __name__ == '__main__':
    main()