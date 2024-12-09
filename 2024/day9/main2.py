from collections import defaultdict

filesystem = [int(x) for x in list(open("input.txt").read().strip())]

fs = []
_id = 0
for i, value in enumerate(filesystem):
    if i % 2 == 0:
        fs.extend([_id] * value)
        _id += 1
    else:
        fs.extend([-1] * value)

# getting empty spaces
empty_spaces = defaultdict(list)
empty_indices = [i for i, value in enumerate(fs) if value == -1]
current = []
for i in range(len(empty_indices) - 1):
    if i == len(empty_indices) - 2:
        if empty_indices[i] + 1 == empty_indices[i + 1]:
            current.append(empty_indices[i])
            current.append(empty_indices[i + 1])
            empty_spaces[len(current)].append(current)
        else:
            current.append(empty_indices[i])
            empty_spaces[len(current)].append(current)
            empty_spaces[1].append([empty_indices[i + 1]])
        break

    if empty_indices[i] + 1 == empty_indices[i + 1]:
        current.append(empty_indices[i])
        continue

    current.append(empty_indices[i])
    empty_spaces[len(current)].append(current)
    current = []

# calculating new filesystem
new_fs = fs.copy()
right = len(fs) - 2
current = fs[-1]
length = 1
while right > 0:
    if current == -1:
        current = fs[right]
        right -= 1
        length = 1
        continue

    if current == fs[right]:
        right -= 1
        length += 1
        continue

    # find possible space
    possible_spaces = []
    for i in range(length, max(empty_spaces.keys()) + 1):
        if i in empty_spaces and empty_spaces[i]:
            possible_spaces.append(empty_spaces[i][0])

    # fill the space if there is a space
    if possible_spaces:
        space = list(sorted(possible_spaces, key=lambda x: x[0]))[0]
        if space[0] < right:
            for j in range(space[0], space[0] + length):
                new_fs[j] = current
            for j in range(right + 1, right + length + 1):
                new_fs[j] = -1
            empty_spaces[len(space)].pop(0)
            if len(space) > length:
                new_space = space[length:]
                empty_spaces[len(space) - length] = sorted([new_space] + empty_spaces[len(space) - length],
                                                           key=lambda x: x[0])

    current = fs[right]
    right -= 1
    length = 1

answer = 0
for i, value in enumerate(new_fs):
    if value == -1:
        continue
    answer += i * value

print(answer)
