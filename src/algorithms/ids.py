from collections import deque
def dfs_depth_limited(graph, start, goal, depth_limit):
    """
    Depth-limited DFS.

    Returns:
        (path, found, depth_found)
        - path: list of nodes from start to current (goal path if found, else deepest partial)
        - found: bool indicating if goal was found within depth_limit
        - depth_found: the depth at which goal was found (integer) when found is True; None otherwise
    """
    stack = deque([(start, 0)])
    # Optional depth-aware visited: record the shallowest depth a node was seen at
    # This allows revisiting a node if we reached it at a shallower or equal depth,
    # which is important for IDS correctness within a single depth-limited run.
    seen_depth = {}
    parent = {start: None}

    deepest_node = start
    deepest_depth = 0

    while stack:
        vertex, current_depth = stack.pop()
        if current_depth > depth_limit:
            continue
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], True, current_depth

        # If we've seen this node before at a depth <= current_depth, skip
        prev = seen_depth.get(vertex)
        if prev is not None and prev <= current_depth:
            continue
        seen_depth[vertex] = current_depth

        if current_depth > deepest_depth:
            deepest_depth = current_depth
            deepest_node = vertex

        # Deterministic neighbor order to keep runs consistent
        for neighbor in sorted(graph[vertex]):
            if current_depth + 1 <= depth_limit:
                stack.append((neighbor, current_depth + 1))
                if neighbor not in parent:
                    parent[neighbor] = vertex

    path = []
    v = deepest_node
    while v is not None:
        path.append(v)
        v = parent[v]
    return path[::-1], False, None

def ids(graph, start, goal, max_depth):
    """
    Iterative Deepening Search.

    Returns:
        - If goal found: (path, depth_found)
        - If not found within max_depth: (partial_path, None)
    """
    last_partial = [start]
    for depth in range(max_depth+1):
        path, found, depth_found = dfs_depth_limited(graph, start, goal, depth)
        if found:
            return path, depth_found
        last_partial = path
    return last_partial, None