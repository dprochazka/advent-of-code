from copy import deepcopy
import itertools


# TODO create a utils package
def parse_text_blocks(lines):
    blocks = []
    block = []
    for line in lines:
        if line == "":
            blocks.append(deepcopy(block))
            block.clear()
            continue
        block.append(line)
    blocks.append(deepcopy(block))
    return blocks


def transpose_block(block):
    return ["".join(x) for x in zip(*block)]


def find_horizontal_mirrors(block):
    N = len(block)
    candidate_indices = []
    for i, (l1, l2) in enumerate(itertools.pairwise(block)):
        if l1 == l2:
            candidate_indices.append(i)
    for i in candidate_indices:
        i1 = i
        i2 = i + 1
        while i1 >= 0 and i2 < N:
            if block[i1] != block[i2]:
                break
            if i1 == 0 or i2 == N - 1:
                yield i + 1
            i1 -= 1
            i2 += 1


def find_mirrors(block):
    s = 0
    for n in find_horizontal_mirrors(block):
        s += 100 * n
    for n in find_horizontal_mirrors(transpose_block(block)):
        s += n
    return s


def solve_part_one(lines):
    return sum([find_mirrors(b) for b in parse_text_blocks(lines)])


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(solve_part_one(lines))
