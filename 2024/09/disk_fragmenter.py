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


#### Part 2 ####
disk_blocks = []
for i, block in enumerate(disk_map):
    if i % 2 == 0:
        file_id = i // 2
    else:
        file_id = None
    size = int(block)
    # if size > 0:
    disk_blocks.append((size, file_id))


k = len(disk_blocks) - 1  # defrag cursor
while k > 0:
    size, file_id = disk_blocks[k]
    if file_id is None:
        k -= 1
        continue
    for j in range(k):
        space, fid = disk_blocks[j]
        if fid is None and size <= space:  # found space
            if size == space:
                # just swap blocks
                disk_blocks[j], disk_blocks[k] = disk_blocks[k], disk_blocks[j]
                break
            disk_blocks[k] = (size, None)
            disk_blocks[j] = (space - size, None)
            disk_blocks.insert(j, (size, file_id))
            k += 1  # move cursor with extra block created by insertion at j
            break
    k -= 1  # move cursor

checksum = 0
idx_true = 0
for size, file_id in disk_blocks:
    if file_id is None:
        idx_true += size
        continue
    for i in range(size):
        checksum += idx_true * file_id
        idx_true += 1

print(checksum)
