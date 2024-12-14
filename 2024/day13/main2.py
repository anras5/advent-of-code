problems = []
problem = []
with open("input.txt") as file:
    for line in file:
        if line.startswith("Button A"):
            problem = []
            a_x = line.split(" ")[2][2:-1]
            a_y = line.split(" ")[3][2:]
            problem.append((int(a_x), int(a_y)))
        elif line.startswith("Button B"):
            b_x = line.split(" ")[2][2:-1]
            b_y = line.split(" ")[3][2:]
            problem.append((int(b_x), int(b_y)))
        elif line.startswith("Prize:"):
            p_x = line.split(" ")[1][2:-1]
            p_y = line.split(" ")[2][2:]
            problem.append((int(p_x) + 10000000000000, int(p_y) + 10000000000000))
            problems.append(problem)

tokens = 0
for p in problems:

    b = (p[2][1] * p[0][0] - p[2][0] * p[0][1]) / (p[1][1] * p[0][0] - p[1][0] * p[0][1])
    a = (p[2][0] - p[1][0] * b) / p[0][0]

    # check if a and b are integers
    if a.is_integer() and b.is_integer():
        tokens += 3 * a + b

print(tokens)
