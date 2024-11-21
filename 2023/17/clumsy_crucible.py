with open("input.txt") as input_file:
    array = [[int(char) for char in line.rstrip()] for line in input_file]

M, N = len(array), len(array[0])

def valid_neighbors(m, n, dm, dn, s):
    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        i, j = m + di, n + dj
        if not (0 <= i < M and 0 <= j < N):
            # out of bounds
            continue
        if dm == -di and dn == -dj:
            # invalid move
            continue
        if dm == di and dn == dj:
            l = s + 1
        else:
            l = 1
        if l <= 3:
            yield (i, j, di, dj, l)

from heapq import heappush, heappop

seen = set()
pq = []

seen.add(5*(0,))
heappush(pq, (6*(0,)))

while True:
    h, m, n, dm, dn, s = heappop(pq)
    if m == M - 1 and n == N - 1:
        print(h)
        break
    for i, j, di, dj, l in valid_neighbors(m, n, dm, dn, s):
        if (i, j, di, dj, l) in seen:
            continue
        dh = array[i][j]
        seen.add((i, j, di, dj, l))
        heappush(pq, (h + dh, i, j, di, dj, l))
