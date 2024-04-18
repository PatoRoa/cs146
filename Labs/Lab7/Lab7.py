# n numbered cities from 0 to n - 1
# array edges, where edges[i] = [from, to, weight]
# int distanceThreshold

# Return city that reaches the least amount of cities with distanceThreshold
# If multiple cities have this same amount, pick the one with highest n
from typing import List


def findTheCity(n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    dist = [[0] * n for i in range(n)]

    for e in edges:
        dist[e[0]][e[1]] = e[2]
        dist[e[1]][e[0]] = e[2]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j != k:

                    if dist[i][j] == 0 and dist[i][k] != 0 and dist[k][j] != 0:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        

    topCity = 0
    topCityLen = float('inf')
    for i in range(len(dist)):

        counter = 0
        for j in dist[i]:
            if 0 < j <= distanceThreshold:
                counter += 1

        if topCityLen >= counter and topCity < i:
            topCityLen = counter
            topCity = i

    print(topCity)
    return topCity


# Driver code
n = 4
edges = [[0, 1, 3],
         [1, 2, 1],
         [1, 3, 4],
         [2, 3, 1]]

distanceThreshold = 4

# n = 5
# edges = [[0, 1, 2],
#          [0, 4, 8],
#          [1, 2, 3],
#          [1, 4, 2],
#          [2, 3, 1],
#          [3, 4, 1]]
#
# distanceThreshold = 2

findTheCity(n, edges, distanceThreshold)
