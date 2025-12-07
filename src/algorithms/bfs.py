from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)
    return None


