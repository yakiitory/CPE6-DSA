graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"]
}

def bfs(start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(graph[node])

print("BFS starting from A:")
bfs("A")
