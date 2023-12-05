from copy import deepcopy
import functools


def parse_map(lines):
    maps = [[int(x) for x in line.split()] for line in lines[1:]]

    def m(num):
        for out, inp, ran in maps:
            if inp <= num < inp + ran:
                return out + (num - inp)
        return num

    return m


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


def parse_input(lines):
    seeds = [int(x) for x in lines.pop(0).split(":")[1].split()]
    blocks = parse_text_blocks(lines[1:])
    maps = [parse_map(x) for x in blocks]
    return seeds, maps


def find_locations(lines):
    seeds, maps = parse_input(lines)
    return [functools.reduce(lambda x, y: y(x), maps, seed) for seed in seeds]


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(min(find_locations(lines)))
