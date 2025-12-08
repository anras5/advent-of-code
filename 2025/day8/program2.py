from dataclasses import dataclass
from math import sqrt
from collections import defaultdict


@dataclass
class Box:
    x: int
    y: int
    z: int


def distance(box1: Box, box2: Box):
    return sqrt(
        (box1.x - box2.x) ** 2 + (box1.y - box2.y) ** 2 + (box1.z - box2.z) ** 2
    )


boxes: list[Box] = [
    Box(*map(int, line.split(","))) for line in open("input.txt").readlines()
]
distances: dict[tuple[int, int], float] = {
    (i, j): distance(boxes[i], boxes[j])
    for i in range(len(boxes))
    for j in range(i + 1, len(boxes))
}

clusters: dict[int, list[int]] = defaultdict(list)
connected: dict[tuple[int, int], bool] = {
    (i, j): False for i in range(len(boxes) - 1) for j in range(i + 1, len(boxes))
}
while not all(connected.values()):
    m_i, m_j, minimum_distance = 0, 0, float("inf")
    for (i, j), d in distances.items():
        if d < minimum_distance and not connected[(i, j)]:
            minimum_distance = d
            m_i, m_j = i, j

    if not any(m_i in cluster for cluster in clusters.values()) and not any(
        m_j in cluster for cluster in clusters.values()
    ):
        new_cluster = max(clusters.keys(), default=0) + 1
        clusters[new_cluster] = [m_i, m_j]
    elif any(m_i in cluster for cluster in clusters.values()) and not any(
        m_j in cluster for cluster in clusters.values()
    ):
        cluster_number = next(k for k, cluster in clusters.items() if m_i in cluster)
        clusters[cluster_number].append(m_j)
    elif any(m_j in cluster for cluster in clusters.values()) and not any(
        m_i in cluster for cluster in clusters.values()
    ):
        cluster_number = next(k for k, cluster in clusters.items() if m_j in cluster)
        clusters[cluster_number].append(m_i)
    else:
        for k_i, cluster_i in clusters.items():
            if m_i in cluster_i:
                for k_j, cluster_j in clusters.items():
                    if m_j in cluster_j:
                        del clusters[k_j]
                        clusters[k_i].extend(cluster_j)
                        for i in range(len(clusters[k_i])):
                            for j in range(len(clusters[k_i])):
                                if clusters[k_i][i] < clusters[k_i][j]:
                                    connected[(clusters[k_i][i], clusters[k_i][j])] = (
                                        True
                                    )
                        break
                break

    print(sum(connected.values()))

last_box_1 = boxes[m_i]
last_box_2 = boxes[m_j]
print(last_box_1, last_box_2)
print(last_box_1.x * last_box_2.x)
