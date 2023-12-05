from copy import deepcopy
import functools
import itertools


def parse_map(lines):
    maps = [[int(x) for x in line.split()] for line in lines[1:]]

    def m(num):
        for out, inp, ran in maps:
            if inp <= num < inp + ran:
                return out + (num - inp)
        return num

    return m


def parse_inversed_map(lines):
    maps = [[int(x) for x in line.split()] for line in lines[1:]]

    def im(num):
        for inp, out, ran in maps:
            if inp <= num < inp + ran:
                return out + (num - inp)
        return num

    return im


def get_seed_detector(seed_line):
    def seed_detector(seed):
        """Check if a seed exists as defined in Part Two"""
        for s, r in itertools.batched(seed_line, 2):
            if s <= seed < s + r:
                return True
        return False

    return seed_detector


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


def parse_input(lines, map_parser):
    seeds = [int(x) for x in lines.pop(0).split(":")[1].split()]
    blocks = parse_text_blocks(lines[1:])
    maps = [map_parser(x) for x in blocks]
    return seeds, maps


def find_locations_part_one(lines):
    seeds, maps = parse_input(lines, parse_map)
    return [functools.reduce(lambda x, y: y(x), maps, seed) for seed in seeds]


def find_minimal_location_part_two(lines):
    seeds, imaps = parse_input(lines, parse_inversed_map)
    detect = get_seed_detector(seeds)
    chained_imap = lambda l: functools.reduce(lambda x, y: y(x), reversed(imaps), l)

    loc = 0
    while True:
        if detect(chained_imap(loc)):
            return loc
        loc += 1


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    # print(min(find_locations_part_one(lines)))
    print(find_minimal_location_part_two(lines))
