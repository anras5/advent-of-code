lines = [list(line.strip()) for line in open("input.txt")]
lines = [["0" if value == "." else value for value in line] for line in lines]

for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            if lines[i - 1][j] == "S":
                lines[i][j] = "1"
            if lines[i - 1][j].isdigit() and int(lines[i - 1][j]) > 0:
                lines[i][j] = str(int(lines[i - 1][j]) + int(lines[i][j]))

        elif lines[i][j] == "^":
            if (
                lines[i - 1][j].isdigit()
                and int(lines[i - 1][j]) > 0
                and j > 0
                and j < len(lines[i]) - 1
            ):
                if lines[i][j - 1] != "^":
                    lines[i][j - 1] = str(int(lines[i][j - 1]) + int(lines[i - 1][j]))
                if lines[i][j + 1] != "^":
                    lines[i][j + 1] = str(int(lines[i][j + 1]) + int(lines[i - 1][j]))

counter = sum(int(value) for value in lines[-1])
print(counter)
