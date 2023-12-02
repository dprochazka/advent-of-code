import re

def parse_line(line):
    numbers = re.findall("[0-9]", line)
    return int(numbers[0] + numbers[-1])

def calibrate_trebuchet(input_file):    
    return sum((parse_line(line) for line in input_file))

if __name__ == "__main__":
    with open("input") as input_file:
        print(calibrate_trebuchet(input_file))