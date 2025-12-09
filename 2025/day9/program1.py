from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


points = [Point(*map(int, line.split(","))) for line in open("input.txt").readlines()]


maximum = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        area = (abs(points[i].x - points[j].x) + 1) * (
            abs(points[i].y - points[j].y) + 1
        )
        maximum = max(maximum, area)

print(maximum)
