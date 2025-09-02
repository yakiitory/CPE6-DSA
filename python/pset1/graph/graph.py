"""
    Author: Steven Ebreo
    Problem Set 1 : Graph
    Represent a friendship network using a graph
    Implement BFS and DFS traversals to explore the network
"""

def main():
    friendship_graph = {
        'Steven': ['Skealla', 'Faye', 'Oxy', 'Jup(iter)'],
        'Skealla': ['Steven', 'Oxy', 'Ralph'],
        'Ralph' : ['Skealla'],
        'Faye': ['Steven', 'Geanne'],
        'Geanne': ['Faye'],
        'Oxy': ['Steven', 'Jup(iter)'],
        'Jup(iter)': ['Steven', 'Oxy']
    }

    bfs_list = []
    bfs(friendship_graph, "Steven", bfs_list)
    print(*bfs_list, sep=", ")

    dfs_list = []
    dfs(friendship_graph, "Steven", dfs_list)
    print(*dfs_list, sep=", ")

def bfs(graph:dict, start:str, l:list):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            l.append(node)
            visited.append(node)
            queue.extend(graph[node])

def dfs(graph:dict, start:str, l:list):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            l.append(node)
            visited.append(node)
            stack.extend(graph[node])


if __name__ == "__main__":
    main()
