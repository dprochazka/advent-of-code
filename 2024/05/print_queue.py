rules = []
updates = []

with open("input.txt") as input_file:
    end_of_rules = False
    for line in input_file:
        line = line.rstrip()
        if not end_of_rules:
            if not line:
                end_of_rules = True
                continue
            rules.append(tuple(int(x) for x in line.split("|")))
        else:
            updates.append([int(x) for x in line.split(",")])
    lines = [line.rstrip() for line in input_file]

incorrectly_ordered = []

#### Part1 ####
result = 0
for n, upd in enumerate(updates):
    index = {x: i for i, x in enumerate(upd)}
    correct = True
    for a, b in rules:
        if a not in index or b not in index:
            # ignore missing page number
            continue
        if index[a] > index[b]:
            # rule broken
            correct = False
            incorrectly_ordered.append(n)
            break
    if correct:
        result += upd[len(upd) // 2]

print(result)

#### Part 2 ####
from collections import defaultdict
from functools import cmp_to_key

cmp_map = defaultdict(lambda: defaultdict(int))

for r in rules:
    cmp_map[r[0]][r[1]] = -1
    cmp_map[r[1]][r[0]] = 1

key = cmp_to_key(lambda a, b: cmp_map[a][b])

result = 0
for n in incorrectly_ordered:
    upd = updates[n]
    result += sorted(upd, key=key)[len(upd) // 2]

print(result)
