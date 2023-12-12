from collections import Counter
import itertools
import re


def bruteforce_hot_springs(line):
    record, checksum = line.split()
    checksum = [int(x) for x in checksum.split(",")]

    def check_line_variation(candidate, checksum):
        return [len(x) for x in re.findall("#+", candidate)] == checksum

    variations = 0
    for p in itertools.product(".#", repeat=Counter(record)["?"]):
        p = list(p)
        candidate = "".join(map(lambda x: p.pop(0) if x == "?" else x, record))
        if check_line_variation(candidate, checksum):
            variations += 1
    return variations


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
    print(sum([bruteforce_hot_springs(line) for line in lines]))
