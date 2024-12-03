with open("input.txt") as input_file:
    puzzle_input = input_file.read()

import re

#### Part1 ####
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", puzzle_input)
print(sum(map(lambda x: int(x[0]) * int(x[1]), matches)))


#### Part2 ####
switch = True
out = 0
for m in re.finditer(r"(do\(\))|(don't\(\))|(mul\((\d{1,3}),(\d{1,3})\))", puzzle_input):
    do, dont, _, a, b = m.groups()
    if do:
        switch = True
    elif dont:
        switch = False
    elif switch:
        out += int(a) * int(b)
print(out)
