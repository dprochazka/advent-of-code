with open("input.txt") as input_file:
    lines = [line.rstrip() for line in input_file]

import itertools

M, N = len(lines), len(lines[0])

#### Part1 ####
DIR8 = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
count = 0
for i, j in itertools.product(range(M), range(N)):
    if lines[i][j] == "X":
        for di, dj in DIR8:
            found = False
            for k, c in enumerate("MAS", 1):
                m, n = i + k * di, j + k * dj
                if not ((0 <= m < M) and (0 <= n < N)):
                    # out of bounds
                    found = False
                    break
                if lines[m][n] == c:
                    found = True
                else:
                    found = False
                    break
            if found:
                count += 1

print(count)

#### Part 2 ####
count = 0
for i, j in itertools.product(range(1, M - 1), range(1, N - 1)):
    if lines[i][j] == "A":
        for di, dj in ((1, 1), (1, -1)):
            found = False
            if (lines[i + di][j + dj] == "M" and lines[i - di][j - dj] == "S") or (
                lines[i + di][j + dj] == "S" and lines[i - di][j - dj] == "M"
            ):
                found = True
            else:
                found = False
                break
        if found:
            count += 1

print(count)
