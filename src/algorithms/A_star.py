import heapq
import math
import numpy as np

def energy_aware_heuristic(a, b, average_terrain_cost):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])

    # Diagonal (octile) distance
    D = 1
    D2 = math.sqrt(2)
    distance = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    return distance * average_terrain_cost


def A_star(graph, start, goal, average_terrain_cost):
    heap = []
    heapq.heappush(heap, (0, start))
    parent = {start: None}
    g_cost = {start: 0}
    h_values = {}
    explored_count = 0
    visited = set()

    while heap:
        f, vertex = heapq.heappop(heap)
        explored_count += 1
        if vertex in visited: continue
        visited.add(vertex)

        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], g_cost[goal], h_values, explored_count, g_cost, visited

        for neighbor in graph[vertex]:
            vertex_cost = graph[vertex][neighbor]['weight']
            new_g = g_cost[vertex] + vertex_cost
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = vertex
                h = energy_aware_heuristic(neighbor, goal, average_terrain_cost)
                h_values[neighbor] = h
                f = new_g + h
                heapq.heappush(heap, (f, neighbor))

    return None, float('inf'), h_values, explored_count, g_cost, visited


