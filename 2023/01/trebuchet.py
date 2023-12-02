import re


def parse_line(line):
    digits_dict = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    regex = "|".join(digits_dict.keys())

    # forward search
    first_digit = re.search(regex, line).group(0)
    first_digit = digits_dict[first_digit]

    # backward search
    def reverse(string):
        return string[::-1]

    second_digit = re.search(reverse(regex), reverse(line)).group(0)
    second_digit = digits_dict[reverse(second_digit)]

    return 10 * first_digit + second_digit


def calibrate_trebuchet(input_file):
    return sum((parse_line(line) for line in input_file))


if __name__ == "__main__":
    with open("input") as input_file:
        print(calibrate_trebuchet(input_file))
