from collections import defaultdict

current = {int(x): 1 for x in open("input.txt").read().strip().split(' ')}

for i in range(75):
    print(i)
    prev = current.copy()
    current = defaultdict(int)
    for value in prev:
        if value == 0:
            current[1] += prev[value]
        elif len(str(value)) % 2 == 0:
            current[int(str(value)[:len(str(value))//2])] += prev[value]
            current[int(str(value)[len(str(value))//2:])] += prev[value]
        else:
            current[value*2024] += prev[value]

print(sum(v for v in current.values()))