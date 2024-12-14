from pulp import LpMinimize, LpProblem, LpVariable, lpSum, value

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
            problem.append((int(p_x), int(p_y)))
            problems.append(problem)


tokens = 0
for p in problems:

    problem = LpProblem("problem", LpMinimize)

    a = LpVariable("a_var")
    b = LpVariable("b_var")

    problem += a * p[0][0] + b * p[1][0] == p[2][0]
    problem += a * p[0][1] + b * p[1][1] == p[2][1]

    obj = lpSum([a*3, b*1])
    problem += obj
    print(problem)
    problem.solve()

    if problem.status == 1:
        tokens += value(problem.objective)

print(tokens)