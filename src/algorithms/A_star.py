import heapq
import math

def diagonal_heuristic(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    D = 1
    D2 = math.sqrt(2)
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def A_star(graph, start, goal):
    heap = []
    heapq.heappush(heap, (0, start))
    parent = {start: None}
    g_cost = {start: 0}

    while heap:
        f, vertex = heapq.heappop(heap)
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], g_cost[goal]

        for neighbor in graph[vertex]:
            vertex_cost = graph[vertex][neighbor]['weight']
            new_g = g_cost[vertex] + vertex_cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = vertex
                f = new_g + diagonal_heuristic(neighbor, goal)
                heapq.heappush(heap, (f, neighbor))

    return None, float('inf')


