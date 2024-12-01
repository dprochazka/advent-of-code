with open("input.txt") as input_file:
    lines = [list(map(int, line.split())) for line in input_file]

col1, col2 = map(list, zip(*lines))


#### Part1 ####
print(sum(map(lambda x: abs(x[0] - x[1]), zip(sorted(col1), sorted(col2)))))


#### Part2 ####
from collections import Counter

count1 = Counter(col1)
count2 = Counter(col2)

print(sum(map(lambda val: val * count1[val] * count2[val], set(count1) & set(count2))))
