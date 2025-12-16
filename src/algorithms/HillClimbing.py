import heapq
import math
from threading import currentThread


def diagonal_heuristic(a, b):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])
    D = 1
    D2 = math.sqrt(2)
    return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)

def energy_aware_heuristic(a, b, terrain_map, elevation_map, terrain_cost):
    base_dist = diagonal_heuristic(a, b)

    terrain_factor = terrain_cost[terrain_map[a]]
    elevation_penalty = abs(elevation_map[a] - elevation_map[b])

    return base_dist * terrain_factor + 0.1 * elevation_penalty

def hillclimbing(graph, start, goal, terrain_map, elevation_map, terrain_cost):
    current = start
    path = [start]

    while current != goal:
        neighbors = list(graph[current].keys())

        if not neighbors:
            return None, float('inf')

        next_node = min(
            neighbors,
            key=lambda n: energy_aware_heuristic(n, goal, terrain_map, elevation_map, terrain_cost)
        )

        if energy_aware_heuristic(next_node, goal, terrain_map, elevation_map, terrain_cost) >= energy_aware_heuristic(current, goal, terrain_map, elevation_map, terrain_cost):
            return None, float('inf')

        current = next_node
        path.append(current)

    return path, len(path) - 1