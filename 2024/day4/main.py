count_xmas = 0

f = open("input.txt", "r").readlines()
f = [list(x.strip()) for x in f]

# rows
for line in f:
    for i in range(0, len(line)-3):
        if line[i:i+4] == ['X', 'M', 'A', 'S'] or line[i:i+4] == ['S', 'A', 'M', 'X']:
            count_xmas += 1

# columns
for i in range(0, len(f[0])):
    column = [x[i] for x in f]
    for j in range(0, len(column)-3):
        if column[j:j+4] == ['X', 'M', 'A', 'S'] or column[j:j+4] == ['S', 'A', 'M', 'X']:
            count_xmas += 1

# diagonals
for i in range(0, len(f)-3):
    for j in range(0, len(f[0])-3):
        if [f[i][j], f[i+1][j+1], f[i+2][j+2], f[i+3][j+3]] == ['X', 'M', 'A', 'S'] or [f[i][j], f[i+1][j+1], f[i+2][j+2], f[i+3][j+3]] == ['S', 'A', 'M', 'X']:
            count_xmas += 1
        if [f[i][j+3], f[i+1][j+2], f[i+2][j+1], f[i+3][j]] == ['X', 'M', 'A', 'S'] or [f[i][j+3], f[i+1][j+2], f[i+2][j+1], f[i+3][j]] == ['S', 'A', 'M', 'X']:
            count_xmas += 1

print(count_xmas)

count_xmas = 0
# X-MAS
for i in range(0, len(f)-2):
    for j in range(0, len(f[0])-2):
        if (
                ([f[i][j], f[i+1][j+1], f[i+2][j+2]] == ['M', 'A', 'S'] or [f[i][j], f[i+1][j+1], f[i+2][j+2]] == ['S', 'A', 'M'])
                and
                ([f[i][j+2], f[i+1][j+1], f[i+2][j]] == ['M', 'A', 'S'] or [f[i][j+2], f[i+1][j+1], f[i+2][j]] == ['S', 'A', 'M'])
        ):
            count_xmas += 1

print(count_xmas)