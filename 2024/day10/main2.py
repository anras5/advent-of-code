f = [[int(x) for x in line.strip()] for line in open("input.txt").readlines()]


def get_trails(f, i, j):
    nines = list()

    def walk(height, i, j):
        print(height, i, j)
        if i < 0 or i >= len(f) or j < 0 or j >= len(f[i]):
            return
        if f[i][j] == 9 and height == 9:
            nonlocal nines
            nines.append((i, j))
            return
        if i+1 < len(f) and f[i+1][j] == height + 1:
            walk(height + 1, i + 1, j)
        if i-1 >= 0 and f[i-1][j] == height + 1:
            walk(height + 1, i - 1, j)
        if j+1 < len(f[i]) and f[i][j+1] == height + 1:
            walk(height + 1, i, j + 1)
        if j-1 >= 0 and f[i][j-1] == height + 1:
            walk(height + 1, i, j - 1)


    walk(0, i, j)
    return len(nines)


score = 0
# main loop
for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] == 0:
            score += get_trails(f, i, j)

print(score)