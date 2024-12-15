import time
import os

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
    print(''.join([str(x) if x > 0 else ' ' for x in row]))
print()

# simulate
i = 1
while True:
    print(i)
    for p, v in robots:

        # update field
        field[p[1]][p[0]] -= 1

        # update position
        p[0] = (p[0] + v[0]) % W
        p[1] = (p[1] + v[1]) % H

        # update field
        field[p[1]][p[0]] += 1

    # if there is a row with 10 robots next to each other, print the field
    for row in field:
        if [1]*10 in [row[i:i+10] for i in range(W-9)]:
            for row_n in field:
                print(''.join([str(x) if x > 0 else ' ' for x in row_n]))

            # wait for a space to be clicked to continue the loop
            while True:
                if input() == ' ':
                    os.system("clear")
                    break
    i += 1
