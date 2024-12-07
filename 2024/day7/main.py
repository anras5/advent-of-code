import itertools

f = open("input.txt", "r").read().split('\n')
f = [(x.split(':')[0], x.split(':')[1].strip().split(' ')) for x in f]

_sum = 0
operators = ['*', '+']
for eq in f:

    perms = list(itertools.product(operators, repeat=len(eq[1]) - 1))

    for perm in perms:
        eq_perm = []
        for i in range(len(eq[1])):
            eq_perm.append(int(eq[1][i]))
            if i < len(eq[1]) - 1:
                eq_perm.append(perm[i])

        value = eq_perm[0]
        for i in range(1, len(eq_perm), 2):
            if eq_perm[i] == '+':
                value += eq_perm[i + 1]
            elif eq_perm[i] == '*':
                value *= eq_perm[i + 1]

        if value == int(eq[0]):
            _sum += value
            break

print(_sum)
