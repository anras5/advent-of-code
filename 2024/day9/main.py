filesystem = [int(x) for x in list(open("input.txt").read().strip())]

fs = []
_id = 0
for i, value in enumerate(filesystem):
    if i % 2 == 0:
        fs.extend([_id]*value)
        _id += 1
    else:
        fs.extend([-1]*value)

left = 0
right = len(fs) - 1
while True:
    if left >= right:
        break
    if fs[left] == -1 and fs[right] != -1:
        fs[left], fs[right] = fs[right], fs[left]
        left += 1
        right -= 1
    while fs[left] != -1:
        left += 1
    while fs[right] == -1:
        right -= 1

answer = 0
for i, value in enumerate(fs):
    if value == -1:
        break
    answer += i*value
    # print(answer)

print(answer)