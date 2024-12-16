import math

m = [list(x) for x in open("input.txt").read().split("\n")]
# find start
start = None
for i in m:
    for j in i:
        if j == "S":
            start = (m.index(i), i.index(j))
            break

m_cost = [[math.inf for _ in range(len(m[0]))] for _ in range(len(m))]
m_cost[start[0]][start[1]] = 0


def calculate_costs():
    q = [(start, "<")]
    while q:
        (i, j), d = q.pop(0)

        if i - 1 >= 0 and m[i - 1][j] in [".", "E"]:
            if d == "^" and m_cost[i][j] + 1 < m_cost[i - 1][j]:
                m_cost[i - 1][j] = m_cost[i][j] + 1
                q.append(((i - 1, j), "^"))
            elif d != "^" and m_cost[i][j] + 1001 < m_cost[i - 1][j]:
                m_cost[i - 1][j] = m_cost[i][j] + 1001
                q.append(((i - 1, j), "^"))
        if i + 1 < len(m) and m[i + 1][j] in [".", "E"]:
            if d == "v" and m_cost[i][j] + 1 < m_cost[i + 1][j]:
                m_cost[i + 1][j] = m_cost[i][j] + 1
                q.append(((i + 1, j), "v"))
            elif d != "v" and m_cost[i][j] + 1001 < m_cost[i + 1][j]:
                m_cost[i + 1][j] = m_cost[i][j] + 1001
                q.append(((i + 1, j), "v"))
        if j - 1 >= 0 and m[i][j - 1] in [".", "E"]:
            if d == "<" and m_cost[i][j] + 1 < m_cost[i][j - 1]:
                m_cost[i][j - 1] = m_cost[i][j] + 1
                q.append(((i, j - 1), "<"))
            elif d != "<" and m_cost[i][j] + 1001 < m_cost[i][j - 1]:
                m_cost[i][j - 1] = m_cost[i][j] + 1001
                q.append(((i, j - 1), "<"))
        if j + 1 < len(m[0]) and m[i][j + 1] in [".", "E"]:
            if d == ">" and m_cost[i][j] + 1 < m_cost[i][j + 1]:
                m_cost[i][j + 1] = m_cost[i][j] + 1
                q.append(((i, j + 1), ">"))
            elif d != ">" and m_cost[i][j] + 1001 < m_cost[i][j + 1]:
                m_cost[i][j + 1] = m_cost[i][j] + 1001
                q.append(((i, j + 1), ">"))


calculate_costs()

# find end
end = None
for i in m:
    for j in i:
        if j == "E":
            end = (m.index(i), i.index(j))
            break

print(m_cost[end[0]][end[1]])

# for i in m_cost:
#     print(i)


def find_best_paths():
    q = [(end)]
    while q:
        i, j = q.pop(0)

        if m[i][j] == "S":
            break

        # for a given m_cost[i][j] find adjacent cells with minimum cost
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(m) and 0 <= y < len(m[x]) and (m_cost[x][y] < m_cost[i][j]):
                q.append((x, y))
                if m[x][y] == ".":
                    m[x][y] = "X"


find_best_paths()
# for i in m:
    # print("".join(i))
