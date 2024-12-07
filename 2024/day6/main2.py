from copy import deepcopy

m = [list(x) for x in open("input.txt", "r").read().split("\n")]

RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3

initial_position = [0, 0]
direction = UP
new_obstacles = set()

# find starting position
search = True
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == "^":
            initial_position = [i, j]
            search = False
        if not search:
            break
    if not search:
        break

# delete ^ from the input
m[initial_position[0]][initial_position[1]] = "."

# main loop
for a in range(len(m)):
    for b in range(len(m[a])):
        mm = deepcopy(m)
        if m[a][b] == ".":
            mm[a][b] = "#"
        else:
            continue
        positions = set()
        position = initial_position.copy()
        direction = UP

        # check if there will be loop
        while True:
            positions.add((tuple(position), direction))
            i, j = position

            # check if end of the field
            if direction == RIGHT and j + 1 >= len(mm[i]):
                break
            elif direction == UP and i - 1 < 0:
                break
            elif direction == LEFT and j - 1 < 0:
                break
            elif direction == DOWN and i + 1 >= len(mm):
                break

            # check if we can move the position
            if direction == RIGHT and mm[i][j + 1] == ".":
                position[1] += 1
            elif direction == UP and mm[i - 1][j] == ".":
                position[0] -= 1
            elif direction == LEFT and mm[i][j - 1] == ".":
                position[1] -= 1
            elif direction == DOWN and mm[i + 1][j] == ".":
                position[0] += 1
            else:
                direction = (direction - 1) % 4

            if (tuple(position), direction) in positions:
                new_obstacles.add((a, b))
                break


# pprint(m)
print(len(new_obstacles))
