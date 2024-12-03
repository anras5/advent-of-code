lines = open("input.txt", "r").readlines()

numbers = []
previous = {
    'u': 'm',
    'l': 'mu',
    '(': 'mul',
}
enabled = True


for line in lines:

    i = 0
    buffer = ""
    buffer_do = ""
    number_1 = None
    number_2 = None
    while i < len(line):

        if line[i] == "d":
            buffer_do = "d"
        elif line[i] == "o" and buffer_do == "d":
            buffer_do += "o"
        elif line[i] == "(" and buffer_do == "do":
            buffer_do += "("
        elif line[i] == ")" and buffer_do == "do(":
            buffer_do = ""
            enabled = True

        elif line[i] == "n" and buffer_do == "do":
            buffer_do += "n"
        elif line[i] == "'" and buffer_do == "don":
            buffer_do += "'"
        elif line[i] == "t" and buffer_do == "don'":
            buffer_do += "t"
        elif line[i] == "(" and buffer_do == "don't":
            buffer_do += "("
        elif line[i] == ")" and buffer_do == "don't(":
            buffer_do = ""
            enabled = False

        if enabled:
            if line[i] == "m":
                buffer = "m"
            elif line[i] == "u" and buffer == previous['u']:
                buffer += "u"
            elif line[i] == "l" and buffer == previous['l']:
                buffer += "l"
            elif line[i] == "(" and buffer == previous['(']:
                buffer += "("
            elif line[i].isdigit() and buffer == "mul(" and (number_1 is None or len(str(number_1)) <= 3):
                x = number_1 if number_1 is not None else ""
                number_1 = int(str(x) + line[i])
            elif line[i] == "," and buffer == "mul(" and number_1 is not None:
                buffer += ","
            elif line[i].isdigit() and buffer == "mul(," and (number_2 is None or len(str(number_2)) <= 3):
                x = number_2 if number_2 is not None else ""
                number_2 = int(str(x) + line[i])
            elif line[i] == ")" and buffer == "mul(," and number_1 is not None and number_2 is not None:
                numbers.append((number_1, number_2))
                buffer = ""
                number_1 = None
                number_2 = None
            else:
                buffer = ""
                number_1 = None
                number_2 = None

        i += 1

print(sum([x[0] * x[1] for x in numbers]))