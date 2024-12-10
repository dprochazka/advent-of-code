with open("input.txt") as input_file:
    disk_map = input_file.read()


#### Part 1 ####
disk = []
for i, block in enumerate(disk_map):
    if i % 2 == 0:
        file_id = i // 2
    else:
        file_id = None
    disk.extend(int(block) * (file_id,))

j = disk.index(None)  # move to
for k in range(1, len(disk)):  # move from
    if j >= len(disk) - k:
        break
    val = disk[-k]
    if val is None:
        continue
    disk[j], disk[-k] = val, None
    try:
        j = disk.index(None, j + 1)
    except ValueError:
        break

checksum = 0
for i, val in enumerate(disk):
    if val is None:
        break
    checksum += i * val

print(checksum)
