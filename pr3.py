
import time

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

h = {'A': 6, 'B': 4, 'C': 3, 'D': 5,
     'E': 2, 'F': 1, 'G': 0}


def get_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    path.reverse()
    return path


def cost(path):
    total = 0
    for i in range(len(path) - 1):
        for node, c in graph[path[i]]:
            if node == path[i + 1]:
                total += c
                break
    return total


# Greedy Best First Search
def greedy(start, goal):
    open_list = [start]
    parent = {start: None}
    visited = []

    while open_list:
        current = open_list[0]

        for node in open_list:
            if h[node] < h[current]:
                current = node

        open_list.remove(current)
        visited.append(current)

        if current == goal:
            return get_path(parent, goal), visited

        for node, c in graph[current]:
            if node not in parent:
                parent[node] = current
                open_list.append(node)

    return None, visited


# A* Search
def astar(start, goal):
    open_list = [start]
    g = {start: 0}
    parent = {start: None}
    visited = []

    while open_list:
        current = open_list[0]

        for node in open_list:
            if g[node] + h[node] < g[current] + h[current]:
                current = node

        open_list.remove(current)
        visited.append(current)

        if current == goal:
            return get_path(parent, goal), visited

        for node, c in graph[current]:
            new_g = g[current] + c

            if node not in g or new_g < g[node]:
                g[node] = new_g
                parent[node] = current

                if node not in open_list:
                    open_list.append(node)

    return None, visited


# Run Greedy
t = time.perf_counter()
gp, gv = greedy('A', 'G')
gt = time.perf_counter() - t

# Run A*
t = time.perf_counter()
ap, av = astar('A', 'G')
at = time.perf_counter() - t

# Output
print("GREEDY BEST FIRST SEARCH")
print("Path:", gp)
print("Cost:", cost(gp))
print("Nodes visited:", len(gv))
print("Time:", gt)

print("\nA* SEARCH")
print("Path:", ap)
print("Cost:", cost(ap))
print("Nodes visited:", len(av))
print("Time:", at)

print("\nCOMPARISON")
print("Greedy uses h(n)")
print("A* uses g(n) + h(n)")
print("Greedy is not always optimal")
print("A* gives optimal path with admissible heuristic")
