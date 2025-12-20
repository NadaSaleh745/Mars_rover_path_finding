import heapq
import math

def energy_aware_heuristic(a, b, average_terrain_cost):
    dx = abs(a[0] - b[0])
    dy = abs(a[1] - b[1])

    # Diagonal (octile) distance
    D = 1
    D2 = math.sqrt(2)
    distance = D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
    return distance * average_terrain_cost

def hill_climbing(graph, start, goal, average_terrain_cost):
    current = start
    path = [start]
    explored_count = 0
    while current != goal:
        neighbors = list(graph[current].keys())

        if not neighbors:
            return False, path, explored_count


        next_node = min(
            neighbors,
            key=lambda n: energy_aware_heuristic(n, goal, average_terrain_cost)
        )

        explored_count += 1

        h_next = energy_aware_heuristic(next_node, goal, average_terrain_cost)
        h_curr = energy_aware_heuristic(current, goal, average_terrain_cost)

        if h_next >= h_curr:
            return False, path, explored_count

        current = next_node
        path.append(current)

    return True, path, explored_count