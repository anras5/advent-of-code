from ortools.linear_solver import pywraplp


lines = [line for line in open("input.txt")]
lines_split = [line.split()[1:] for line in lines]

all_positions = [list(map(int, b[-1][1:-1].split(","))) for b in lines_split]
all_buttons = [
    [list(map(int, a[1:-1].split(","))) for a in b[:-1]] for b in lines_split
]

sum_ = 0
for i_problem in range(len(lines)):
    solver = pywraplp.Solver.CreateSolver("SCIP")
    positions = all_positions[i_problem]
    buttons = all_buttons[i_problem]
    x = {}
    for i in range(len(buttons)):
        x[i] = solver.IntVar(0, solver.infinity(), f"x_{i}")

    for i in range(len(positions)):
        solver.Add(
            solver.Sum([x[j] for j in range(len(buttons)) if i in buttons[j]])
            == positions[i]
        )

    solver.Minimize(solver.Sum([x[i] for i in range(len(buttons))]))

    # print(
    #     solver.ExportModelAsLpFormat(False).replace("\\", "").replace(",_", ","),
    #     sep="\n",
    # )

    status = solver.Solve()
    if status == pywraplp.Solver.OPTIMAL:
        sum_ += int(solver.Objective().Value())
        # print(int(solver.Objective().Value()))
    else:
        print(status)

print(sum_)
