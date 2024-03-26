from collections import deque


def topo_sort(adjecency_list, V):
    # Stores indegrees of vertices
    indegree = [0] * V

    for i in range(V):
        for vertex in adjecency_list[i]:
            indegree[vertex] += 1
    print("indegree = ", indegree)

    # Queue that stores vertices with no indegrees
    que = deque()

    for i in range(V):
        if indegree[i] == 0:
            que.append(i)

    result = []

    # Slaps 0-indegree node to the results list
    while que:
        node = que.popleft()
        result.append(node)

        # Decreases next node in the queue's indegree
        for adjacent in adjecency_list[node]:
            indegree[adjacent] -= 1

            if indegree[adjacent] == 0:
                que.append(adjacent)

    # Check if there's a cycle
    if len(result) != V:
        print("There is a cycle in the graph.")
        return []

    return result


# Graph-building
nodes = 8

edges = [[0, 3], [1, 3], [1, 4], [1, 7], [2, 4], [3, 5], [3, 7], [4, 6], [4, 7], [5, 7], [6, 7]]

adj = []    # Adjacency list
for n in range(nodes):
    adj.append([])

for edge in edges:
    adj[edge[0]].append(edge[1])

print("adjacency = ", adj)


# Toposort time
print("Toposort: ")
result = topo_sort(adj, nodes)

print("result = ", result)
