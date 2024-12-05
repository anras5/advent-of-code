rules = set()
updates = list()
correct_updates = list()

# parsing the input
with open("input.txt") as file:
    is_rule = True
    for line in file:
        line = line.strip()
        if line == "":
            is_rule = False
            continue
        if is_rule:
            parsed_line = [int(x) for x in line.split("|")]
            rules.add((parsed_line[0], parsed_line[1]))
        else:
            parsed_line = [int(x) for x in line.split(",")]
            updates.append(parsed_line)
            correct_updates.append(False)

# checking if the updates are in the right order
for iu, update in enumerate(updates):
    right_order = 0
    for i in range(len(update) - 1):
        for j in range(i, len(update)):
            if (update[i], update[j]) in rules:
                right_order += 1
    if right_order == sum([i for i in range(1, len(update))]):
        correct_updates[iu] = True

# getting the middle number of each correct update
answer = 0
for iu, correct_update in enumerate(correct_updates):
    if correct_update:
        answer += updates[iu][len(updates[iu]) // 2]

print(answer)


## TASK 2
incorrect_updates = list()
for iu, correct_update in enumerate(correct_updates):
    if not correct_update:
        incorrect_updates.append(updates[iu])

corrected_updates = list()
for iu, incorrect_update in enumerate(incorrect_updates):
    corrected_update = incorrect_update.copy()
    corrected = False

    # correcting the order of the update by swapping the numbers as long as the sequence is correct
    # (it does not break the inner loops)
    while not corrected:

        again = False
        for i in range(len(corrected_update) - 1):
            for j in range(i, len(corrected_update)):
                if (corrected_update[j], corrected_update[i]) in rules:
                    corrected_update[i], corrected_update[j] = corrected_update[j], corrected_update[i]
                    again = True
                    break
            if again:
                break
        
        # if the sequence is correct, we can stop
        if not again:
            corrected = True

    corrected_updates.append(corrected_update)

# getting the middle number of each corrected update
answer = 0
for iu, corrected_update in enumerate(corrected_updates):
    if corrected_update:
        answer += corrected_updates[iu][len(corrected_updates[iu]) // 2]

print(answer)