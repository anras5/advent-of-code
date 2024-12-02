# task 1
l1 = sum([
    all([
        1 <= a[i + 1] - a[i] <= 3 if a[0] < a[-1] else 1 <= a[i] - a[i + 1] <= 3
        for i in range(len(a) - 1)
    ])
    for a in [[int(x) for x in line.split(' ')] for line in open("input.txt", "r").read().split("\n")]
])


# task 2
l2 = [[int(x) for x in line.split(' ')] for line in open("input.txt", "r").read().split("\n")]
l3 = [False]*len(l2)
for ai, a in enumerate(l2):
    if all([
        1 <= a[i + 1] - a[i] <= 3 if a[0] < a[-1] else 1 <= a[i] - a[i + 1] <= 3
        for i in range(len(a) - 1)
    ]):
        l3[ai] = True
        continue
    for i in range(len(a)):
        b = a[:i] + a[i + 1:]
        if all([
            1 <= b[i + 1] - b[i] <= 3 if b[0] < b[-1] else 1 <= b[i] - b[i + 1] <= 3
            for i in range(len(b) - 1)
        ]):
            l3[ai] = True
            break

print(sum(l3))