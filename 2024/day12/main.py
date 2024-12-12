field = [list(line.strip()) for line in open("input.txt").readlines()]
unique_plots = set((x for row in field for x in row))

# discover returns the size of a region and its perimeter given a starting point (x, y) and a plot
# it also changes the region to 0s
def discover(x, y, plot):
    area = 0
    perimeter = 0
    stack = [(x, y)]
    visited = set()
    while stack:
        x, y = stack.pop(0)
        if (x, y) in visited and field[x][y] == f'0{plot}':
            continue
        visited.add((x, y))
        if x < 0 or y < 0 or x >= len(field) or y >= len(field[0]) or field[x][y] != plot:
            perimeter += 1
            continue
        area += 1
        field[x][y] = f'0{plot}'
        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))
    return area, perimeter


_sum = 0
for plot in unique_plots:

    i = 0
    while i < len(field):
        j = 0
        while j < len(field[i]):
            if field[i][j] == plot:
                area, perimeter = discover(i, j, plot)
                # print(plot, area, perimeter)
                _sum += area * perimeter
            j += 1
        i += 1

print(_sum)