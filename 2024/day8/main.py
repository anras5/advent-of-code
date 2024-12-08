from collections import defaultdict

m = [list(x.strip()) for x in open("input.txt").readlines()]

antennas = defaultdict(list)
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] != '.':
            antennas[m[i][j]].append((i, j))

antinodes = set()
for k, l in antennas.items():
    for i in range(len(l)):
        for j in range(len(l)):
            if i == j:
                continue

            first = l[i]
            second = l[j]

            distance = second[0] - first[0], second[1] - first[1]
            antinode = first[0] - distance[0], first[1] - distance[1]
            if antinode[0] < 0 or antinode[0] >= len(m) or antinode[1] < 0 or antinode[1] >= len(m[0]):
                continue

            antinodes.add(antinode)

print(len(antinodes))