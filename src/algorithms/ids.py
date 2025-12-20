from collections import deque
def dfs_depth_limited(graph, start, goal, depth_limit):

    stack = deque([(start, 0)])
    seen_depth = {}
    parent = {start: None}
    explored_count = 0

    deepest_node = start
    deepest_depth = 0

    while stack:
        vertex, current_depth = stack.pop()
        if current_depth > depth_limit:
            continue
        explored_count += 1

        # If we've seen this node before at a depth <= current_depth, skip
        prev = seen_depth.get(vertex)
        if prev is not None and prev <= current_depth:
            continue
        seen_depth[vertex] = current_depth

        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], True, current_depth, explored_count

        if current_depth > deepest_depth:
            deepest_depth = current_depth
            deepest_node = vertex

        # Deterministic neighbor order to keep runs consistent
        for neighbor in sorted(graph[vertex]):
            if current_depth + 1 <= depth_limit:
                if neighbor not in seen_depth or seen_depth.get(neighbor, float('inf')) > current_depth + 1:
                    parent[neighbor] = vertex
                stack.append((neighbor, current_depth + 1))

    path = []
    v = deepest_node
    while v is not None:
        path.append(v)
        v = parent.get(v)
    return path[::-1], False, None, explored_count

def ids(graph, start, goal, max_depth):
    total_explored = 0
    last_partial = [start]
    for depth in range(max_depth+1):
        path, found, depth_found, explored = dfs_depth_limited(
            graph, start, goal, depth)
        total_explored += explored

        if found:
            return path, depth_found, total_explored
        last_partial = path
    return last_partial, None, total_explored