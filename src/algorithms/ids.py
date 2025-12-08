from collections import deque
def dfs_depth_limited(graph, start, goal, depth_limit):
    stack = deque([(start, 0)])
    visited = set()
    parent = {start: None}

    while stack:
        vertex, current_depth = stack.pop()
        if current_depth > depth_limit:
            continue
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]

        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
                stack.append((neighbor, current_depth + 1))
                if neighbor not in parent:
                    parent[neighbor] = vertex
    return None

def ids(graph, start, goal, max_depth):
    for depth in range(max_depth+1):
        path = dfs_depth_limited(graph, start, goal, depth)
        if path is not None:
            return path
    return None