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


def find_all_mirrors(block):
    s = []
    for n in find_horizontal_mirrors(block):
        s.append(100 * n)
    for n in find_horizontal_mirrors(transpose_block(block)):
        s.append(n)
    return s


def find_first_mirror(block, blacklist):
    for n in find_horizontal_mirrors(block):
        if n and 100 * n not in blacklist:
            return 100 * n
    for n in find_horizontal_mirrors(transpose_block(block)):
        if n and n not in blacklist:
            return n


def solve_part_one(lines):
    return sum([sum(find_all_mirrors(b)) for b in parse_text_blocks(lines)])


def solve_part_two(lines):
    blocks = parse_text_blocks(lines)
    s = 0
    for block in blocks:
        orig_mirror = find_first_mirror(block, blacklist=[])
        breakme = False
        for i, row in enumerate(block):
            for j, char in enumerate(row):
                test_block = deepcopy(block)
                char = "#" if char == "." else "."
                test_block[i] = row[:j] + char + row[j + 1 :]
                mirror = find_first_mirror(
                    test_block, blacklist=[orig_mirror]
                )  # has to be improved...
                if mirror and mirror != orig_mirror:
                    s += mirror
                    breakme = True
                    break
            if breakme:
                break
    return s


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(solve_part_one(lines))
    print(solve_part_two(lines))
