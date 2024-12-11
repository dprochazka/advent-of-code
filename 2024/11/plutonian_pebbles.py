from collections import defaultdict

with open("input.txt") as input_file:
    stones = [int(x) for x in input_file.read().split()]

stones_map = defaultdict(int)  # stone: count
for stone in stones:
    stones_map[stone] += 1

BLINKS = 25  # part 1 
BLINKS = 75  # part 2
stones_map2 = defaultdict(int)
for _ in range(BLINKS):
    for stone, count in stones_map.items():
        if stone == 0:
            stones_map2[1] += count
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            mid = len(s) // 2
            s1, s2 = int(s[:mid]), int(s[mid:])
            stones_map2[s1] += count
            stones_map2[s2] += count
        else:
            stones_map2[2024 * stone] += count
    stones_map = stones_map2
    stones_map2 = defaultdict(int)

print(sum(stones_map.values()))
