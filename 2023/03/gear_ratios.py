import itertools
from helpers import is_digit, is_symbol

def find_part_numbers(input):
    part_numbers = []
    for j, line in enumerate(input):
        number = ""
        for k, char in enumerate(line):
            if is_digit(char):
                number += char
            elif len(number):
                # reached end of word
                for l, m in itertools.product(
                    range(max(j - 1, 0), min(j + 2, len(input))),  # rows
                    range(max(k - len(number) - 1, 0), k + 1),  # cols
                ):
                    if is_symbol(input[l][m]):
                        part_numbers.append(int(number))
                        break
                number = ""
        if len(number):
            # handle last word
            for l, m in itertools.product(
                range(max(j - 1, 0), min(j + 2, len(input))),  # rows
                range(max(len(line) - len(number) - 1, 0), len(line)),  # cols
            ):
                if is_symbol(input[l][m]):
                    part_numbers.append(int(number))
                    break
    return part_numbers


if __name__ == "__main__":
    with open("input.txt") as input_file:
        lines = [line.rstrip() for line in input_file]
        part_numbers = find_part_numbers(lines)
    print(sum(part_numbers))
