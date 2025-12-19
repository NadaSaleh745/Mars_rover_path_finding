from collections import deque
def dfs(graph, start, goal):
    stack = deque([(start, 0)])
    visited = {start}
    parent = {start: None}

    while stack:
        vertex, depth = stack.pop()
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], depth
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, depth + 1))
                if neighbor not in parent:
                    parent[neighbor] = vertex

    return None, None