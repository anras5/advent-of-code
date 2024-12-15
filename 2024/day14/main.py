robots = []
with open("input.txt") as file:
    for line in file:
        l = line.strip().split(' ')
        p = [int(x) for x in l[0][2:].split(',')]
        v = [int(x) for x in l[1][2:].split(',')]
        robots.append([p, v])

# initiate the field
H = 103
W = 101
field = [[0 for _ in range(W)] for _ in range(H)]

for p, v in robots:
    field[p[1]][p[0]] += 1

for row in field:
    print(''.join([str(x) for x in row]))
print()

# simulate
for i in range(1, 101):
    for p, v in robots:

        # update field
        field[p[1]][p[0]] -= 1

        # update position
        p[0] = (p[0] + v[0]) % W
        p[1] = (p[1] + v[1]) % H

        # update field
        field[p[1]][p[0]] += 1

q1 = sum([sum(row) for row in [field[i][:W//2] for i in range(H//2)]])
q2 = sum([sum(row) for row in [field[i][W//2+1:] for i in range(H//2)]])
q3 = sum([sum(row) for row in [field[i][:W//2] for i in range(H//2+1, H)]])
q4 = sum([sum(row) for row in [field[i][W//2+1:] for i in range(H//2+1, H)]])
print(q1, q2, q3, q4)
print(q1*q2*q3*q4)
