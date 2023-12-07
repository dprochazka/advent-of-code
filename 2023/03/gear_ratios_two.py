from dataclasses import dataclass
from abc import ABC

from helpers import is_digit, is_symbol


@dataclass(frozen=True)
class Number:
    num: str
    pos: int

    @property
    def val(self):
        return int(self.num)

    def __len__(self):
        return len(self.num)


@dataclass(frozen=True)
class Symbol:
    sym: str
    pos: int


def check_adjacency(num: Number, sym: Symbol):
    # assuming sym and pos are on adjacent lines or the same line
    return sym.pos >= num.pos - 1 and sym.pos <= num.pos + len(num)


def parse_line(line):
    numbers = []
    symbols = []
    word = ""
    word_start = 0
    for j, char in enumerate(line):
        if is_digit(char):
            if not word:
                word_start = j
            word += char
            continue
        elif is_symbol(char):
            symbols.append(Symbol(char, j))
        if len(word):
            # mutlichar word ended
            numbers.append(Number(word, word_start))
            word = ""
    if len(word):
        # handle last word
        numbers.append(Number(word, word_start))

    return numbers, symbols


def find_part_numbers(input):
    output = []
    lines = [parse_line(line) for line in input]
    for i, _ in enumerate(lines):
        if i == 0:
            symbols = lines[0][1] + lines[1][1]
        elif i == len(lines) - 1:
            symbols = lines[i - 1][1] + lines[i][1]
        else:
            symbols = lines[i - 1][1] + lines[i][1] + lines[i + 1][1]
        for num in lines[i][0]:
            if any(check_adjacency(num, sym) for sym in symbols):
                output.append(num.val)
    return output


def find_gear_ratios(input):
    output = []
    lines = [parse_line(line) for line in input]
    for i, _ in enumerate(lines):
        if i == 0:
            numbers = lines[0][0] + lines[1][0]
        elif i == len(lines) - 1:
            numbers = lines[i - 1][0] + lines[i][0]
        else:
            numers = lines[i - 1][0] + lines[i][0] + lines[i + 1][0]
        for gear in (s for s in lines[i][1] if s.sym == "*"):
            adjacent_numbers = [n for n in numers if check_adjacency(n, gear)]
            if len(adjacent_numbers) == 2:
                output.append(adjacent_numbers[0].val * adjacent_numbers[1].val)
    return output


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
        part_numbers = find_part_numbers(lines)
        gear_ratios = find_gear_ratios(lines)
    print(sum(part_numbers))
    print(sum(gear_ratios))
