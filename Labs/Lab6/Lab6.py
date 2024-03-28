# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#
# Return true if you can finish all courses. Otherwise, return false.
#
# Constraints:
#   • 1 <= numCourses <= 2000
#   • 0 <= prerequisites.length <= 5000
#   • prerequisites[i].length == 2
#   •  0 <= ai, bi < numCourses
#   •  All the pairs prerequisites[i] are unique.
from collections import deque


def canFinish(numCourses, prerequisites):
    # Set up adjacency list, indegrees, and resulting list
    adj = []
    for i in range(numCourses):     # Create list of adjacencies based on numCourses
        adj.append([])

    indegree = [0] * numCourses     # Create list of amounts of indegrees for each course-to-take
    result = []

    # Create two lists of courses-to-take and prerequisites
    # Establish an adjacency for each pair
    # Increment the indegrees for the course-to-take
    for j in prerequisites:
        class_take = j[0]
        class_need = j[1]
        adj[class_need].append(class_take)
        indegree[class_take] += 1

    # Toposort time
    # If a course to take's indegree == 0, slap it into a queue
    que = deque()
    for i in range(numCourses):
        if indegree[i] == 0:
            que.append(i)

    # As a course-to-take's indegree reaches 0, put it in the result
    while que:
        current = que.popleft()
        result.append(current)

        # As a course-to-take is being examined in the adjacency list, remove an indegree from its next course
        for k in adj[current]:
            indegree[k] -= 1

            if indegree[k] == 0:
                que.append(k)

    return len(result) == numCourses


numCourses = 2
prerequisites = [[1, 0]]

print(canFinish(numCourses, prerequisites))