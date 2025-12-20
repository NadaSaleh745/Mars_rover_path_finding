from collections import deque

def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start}
    parent = {start: None}
    explored_count = 0
    while queue:
        vertex = queue.popleft()
        explored_count += 1
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], explored_count
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                if neighbor not in parent:
                    parent[neighbor] = vertex
    return None, explored_count


