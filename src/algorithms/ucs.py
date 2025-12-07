import heapq

def ucs(graph, start, goal):
    heap = []
    heapq.heappush(heap, (0, start))
    parent = {start: None}
    cost_so_far = {start: 0}

    while heap:
        current_cost, vertex = heapq.heappop(heap)
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1], current_cost

        for neighbor in graph[vertex]:
            vertex_cost = graph[vertex][neighbor]['weight']
            new_cost = current_cost + vertex_cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                parent[neighbor] = vertex
                heapq.heappush(heap, (new_cost, neighbor))

    return None, float('inf')


