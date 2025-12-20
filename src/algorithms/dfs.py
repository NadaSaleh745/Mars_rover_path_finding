from collections import deque
def dfs(graph, start, goal):
    stack = deque([(start, 0)])
    visited = {start}
    parent = {start: None}
    explored_count = 0

    while stack:
        vertex, depth = stack.pop()
        explored_count += 1
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], depth, explored_count
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, depth + 1))
                if neighbor not in parent:
                    parent[neighbor] = vertex

    return None, None, explored_count