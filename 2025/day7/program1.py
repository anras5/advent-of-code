from pprint import pprint

lines = [list(line.strip()) for line in open("input.txt")]

counter = 0
for i in range(1, len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == ".":
            if lines[i - 1][j] == "S":
                lines[i][j] = "|"
            if lines[i - 1][j] == "|":
                lines[i][j] = "|"

        elif lines[i][j] == "^":
            if lines[i - 1][j] == "|" and j > 0 and j < len(lines[i]) - 1:
                is_split = False
                if lines[i][j - 1] != "^":
                    lines[i][j - 1] = "|"
                    is_split = True
                if lines[i][j + 1] != "^":
                    lines[i][j + 1] = "|"
                    is_split = True
                if is_split:
                    counter += 1

pprint(lines)
print(counter)
