from collections import deque
def dfs(graph, start, goal):
    stack = deque([start])
    visited = {start}
    parent = {start: None}

    while stack:
        vertex = stack.pop()
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
                parent[neighbor] = vertex

    return None