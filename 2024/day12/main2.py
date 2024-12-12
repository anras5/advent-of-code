field = [list(line.strip()) for line in open("input.txt").readlines()]
unique_plots = set((x for row in field for x in row))

# discover returns the size of a region and its perimeter given a starting point (x, y) and a plot
# it also changes the region to 0s
def discover(x, y, plot):
    area = 0
    walls_vertical_left, walls_vertical_right = [], []
    walls_horizontal_up, walls_horizontal_down = [], []
    stack = [((x, y), (-100, -100))]
    visited = set()
    while stack:
        (x, y), prev = stack.pop(0)
        if (x, y) in visited and field[x][y] == f'0{plot}':
            continue
        visited.add((x, y))
        if x < 0 or y < 0 or x >= len(field) or y >= len(field[0]) or field[x][y] != plot:
            if x < 0:
                walls_horizontal_down.append((x, y))
            elif x >= len(field):
                walls_horizontal_up.append((x, y))
            elif y < 0:
                walls_vertical_right.append((x, y))
            elif y >= len(field[0]):
                walls_vertical_left.append((x, y))
            elif prev[0] == x and prev[1] == y-1:
                walls_vertical_left.append((x, y))
            elif prev[0] == x and prev[1] == y+1:
                walls_vertical_right.append((x, y))
            elif prev[1] == y and prev[0] == x-1:  # previous was higher
                walls_horizontal_up.append((x, y))
            elif prev[1] == y and prev[0] == x+1:  # previous was lower
                walls_horizontal_down.append((x, y))
            continue
        area += 1
        field[x][y] = f'0{plot}'
        stack.append(((x + 1, y), (x, y)))
        stack.append(((x - 1, y), (x, y)))
        stack.append(((x, y + 1), (x, y)))
        stack.append(((x, y - 1), (x, y)))

    print(plot)
    walls_vertical_left.sort(key=lambda x: x[1])
    walls_vertical_right.sort(key=lambda x: x[1])
    walls_horizontal_up.sort(key=lambda x: x[0])
    walls_horizontal_down.sort(key=lambda x: x[0])

    # count number of vertical walls
    number_walls_vertical_left = 0
    for y in set([y for x, y in walls_vertical_left]):
        walls_vertical_with_y = [x for x, y_ in walls_vertical_left if y_ == y]

        current_wall = []
        i = walls_vertical_with_y.index(min(walls_vertical_with_y))
        while walls_vertical_with_y:
            if walls_vertical_with_y[i] + 1 in walls_vertical_with_y:
                current_wall.append(walls_vertical_with_y[i])
                i = walls_vertical_with_y.index(walls_vertical_with_y[i] + 1)
            else:
                current_wall.append(walls_vertical_with_y[i])
                for value in current_wall:
                    walls_vertical_with_y.remove(value)
                number_walls_vertical_left += 1
                if walls_vertical_with_y:
                    i = walls_vertical_with_y.index(min(walls_vertical_with_y))
                    current_wall = []

    number_walls_vertical_right = 0
    for y in set([y for x, y in walls_vertical_right]):
        walls_vertical_with_y = [x for x, y_ in walls_vertical_right if y_ == y]

        current_wall = []
        i = walls_vertical_with_y.index(min(walls_vertical_with_y))
        while walls_vertical_with_y:
            if walls_vertical_with_y[i] + 1 in walls_vertical_with_y:
                current_wall.append(walls_vertical_with_y[i])
                i = walls_vertical_with_y.index(walls_vertical_with_y[i] + 1)
            else:
                current_wall.append(walls_vertical_with_y[i])
                for value in current_wall:
                    walls_vertical_with_y.remove(value)
                number_walls_vertical_right += 1
                if walls_vertical_with_y:
                    i = walls_vertical_with_y.index(min(walls_vertical_with_y))
                    current_wall = []

    # count number of horizontal walls
    number_walls_horizontal_up = 0
    for x in set([x for x, y in walls_horizontal_up]):
        walls_horizontal_with_x = [y for x_, y in walls_horizontal_up if x_ == x]

        current_wall = []
        i = walls_horizontal_with_x.index(min(walls_horizontal_with_x))
        while walls_horizontal_with_x:
            if walls_horizontal_with_x[i] + 1 in walls_horizontal_with_x:
                current_wall.append(walls_horizontal_with_x[i])
                i = walls_horizontal_with_x.index(walls_horizontal_with_x[i] + 1)
            else:
                current_wall.append(walls_horizontal_with_x[i])
                for value in current_wall:
                    walls_horizontal_with_x.remove(value)
                number_walls_horizontal_up += 1
                if walls_horizontal_with_x:
                    i = walls_horizontal_with_x.index(min(walls_horizontal_with_x))
                    current_wall = []

    number_walls_horizontal_down = 0
    for x in set([x for x, y in walls_horizontal_down]):
        walls_horizontal_with_x = [y for x_, y in walls_horizontal_down if x_ == x]

        current_wall = []
        i = walls_horizontal_with_x.index(min(walls_horizontal_with_x))
        while walls_horizontal_with_x:
            if walls_horizontal_with_x[i] + 1 in walls_horizontal_with_x:
                current_wall.append(walls_horizontal_with_x[i])
                i = walls_horizontal_with_x.index(walls_horizontal_with_x[i] + 1)
            else:
                current_wall.append(walls_horizontal_with_x[i])
                for value in current_wall:
                    walls_horizontal_with_x.remove(value)
                number_walls_horizontal_down += 1
                if walls_horizontal_with_x:
                    i = walls_horizontal_with_x.index(min(walls_horizontal_with_x))
                    current_wall = []

    print(f'{number_walls_vertical_left=}')
    print(f'{number_walls_vertical_right=}')
    print(f'{number_walls_horizontal_up=}')
    print(f'{number_walls_horizontal_down=}')

    print("|left\t", walls_vertical_left)
    print("|right\t", walls_vertical_right)
    print("-up\t", walls_horizontal_up)
    print("-down\t", walls_horizontal_down)
    return area, number_walls_vertical_left + number_walls_vertical_right + number_walls_horizontal_down + number_walls_horizontal_up


_sum = 0
l = []
for plot in unique_plots:

    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            if field[i][j] == plot:
                area, perimeter = discover(i, j, plot)
                _sum += area * perimeter
                l.append((plot, perimeter, area, area * perimeter))
            j += 1
        i += 1

for line in sorted(l, key=lambda x: (x[0], x[1], x[2], x[3])):
    print(f"{line[0]}: perimeter = {line[1]}, area = {line[2]}, price = {line[3]}")

print(_sum)