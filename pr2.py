#bfs dfs
import time

maze = [
    [0, 0, 0, 1, 0],
    [1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)


# BFS
def bfs():
    queue = [(start, [start])]
    visited = [start]
    nodes = 0

    while queue:
        current, path = queue.pop(0)
        nodes += 1

        if current == goal:
            return path, nodes

        r, c = current

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    queue.append(((nr, nc), path + [(nr, nc)]))


# DFS
def dfs():
    stack = [(start, [start])]
    visited = [start]
    nodes = 0

    while stack:
        current, path = stack.pop()
        nodes += 1

        if current == goal:
            return path, nodes

        r, c = current

        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < 5 and 0 <= nc < 5:
                if maze[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.append((nr, nc))
                    stack.append(((nr, nc), path + [(nr, nc)]))


# BFS
start_time = time.perf_counter()
bfs_path, bfs_nodes = bfs()
bfs_time = time.perf_counter() - start_time


# DFS
start_time = time.perf_counter()
dfs_path, dfs_nodes = dfs()
dfs_time = time.perf_counter() - start_time


# Results
print("----- BFS -----")
print("Path:", bfs_path)
print("Path Length:", len(bfs_path) - 1)
print("Nodes Explored:", bfs_nodes)
print("Execution Time:", bfs_time, "seconds")

print("\n----- DFS -----")
print("Path:", dfs_path)
print("Path Length:", len(dfs_path) - 1)
print("Nodes Explored:", dfs_nodes)
print("Execution Time:", dfs_time, "seconds")