# Helper function that marks a node as visited and other adjacent nodes as visited
def toposort_helper(v, adj, visited, stack):
    # Mark current node as visited
    visited[v] = True

    # Recurrence calling to visit all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            toposort_helper(i, adj, visited, stack)

    # Put current vertex in the stack after visiting it
    stack.append(v)


def topo_sort(adj, V):
    stack = []

    # Sets up checklist for node visit
    visited = [False] * V

    # Iterates through nodes to make sure they are visited
    for i in range(V):
        if not visited[i]:
            toposort_helper(i, adj, visited, stack)

    while stack:
        print(stack.pop(), end=" ")


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
topo_sort(adj, nodes)
