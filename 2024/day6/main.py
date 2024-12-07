from pprint import pprint

m = [list(x) for x in open("input.txt", "r").read().split("\n")]

RIGHT, UP, LEFT, DOWN = 0, 1, 2, 3

position = [0, 0]
direction = UP
positions = set()

# find starting position
search = True
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] == "^":
            position = [i, j]
            search = False
        if not search:
            break
    if not search:
        break

# delete ^ from the input
m[position[0]][position[1]] = "."

# main loop
iterations = 0
while True:
    positions.add(tuple(position))

    i, j = position

    # check if end of the field
    if direction == RIGHT and j + 1 >= len(m[i]):
        break
    elif direction == UP and i - 1 < 0:
        break
    elif direction == LEFT and j - 1 < 0:
        break
    elif direction == DOWN and i + 1 >= len(m):
        break

    # check if we can move the position
    if direction == RIGHT and m[i][j + 1] == ".":
        position[1] += 1
    elif direction == UP and m[i - 1][j] == ".":
        position[0] -= 1
    elif direction == LEFT and m[i][j - 1] == ".":
        position[1] -= 1
    elif direction == DOWN and m[i + 1][j] == ".":
        position[0] += 1
    else:
        direction = (direction - 1) % 4

    positions.add(tuple(position))

    iterations += 1

# pprint(m)
for position in positions:
    m[position[0]][position[1]] = "X"
# pprint(m)
print(len(positions))

print(iterations)