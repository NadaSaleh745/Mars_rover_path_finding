# Mars Rover Path Planning Using Classical Search Algorithms

## 1. Problem Description

Autonomous navigation is a critical challenge for planetary rovers operating on Mars. Due to significant communication delays between Earth and Mars, limited onboard energy resources, and hazardous terrain, a Mars rover must be capable of planning safe and efficient paths without real-time human intervention.

The objective of this project is to simulate Mars rover path planning on a 2D terrain map that represents realistic Martian surface conditions, including elevation changes, terrain difficulty, and obstacles. The rover must find a feasible or optimal path from a landing site to one or more scientific targets while minimizing traversal cost.

---

## 2. Project Objectives

The primary objectives of this project are:

- Model a Mars-like terrain using elevation and terrain-type maps.
- Convert the terrain into a weighted graph suitable for search algorithms.
- Implement and compare classical search algorithms for rover navigation:
  - Depth-First Search (DFS)
  - Breadth-First Search (BFS)
  - Uniform Cost Search (UCS)
  - Iterative Deepening Search (IDS)
  - A* Search
  - Hill Climbing
  - Genetic Algorithm
- Design a realistic movement cost model reflecting rover constraints.
- Analyze algorithm performance in the context of autonomous planetary exploration.

---

## 3. Mars Terrain Representation

### Elevation Map

- Represents height variations of the Martian surface.
- Steep elevation differences increase energy consumption and traversal risk.

### Terrain Map

Represents surface types such as:

- Flat regolith
- Sandy areas
- Rocky terrain
- Impassable obstacles (e.g., cliffs, large rocks)

### Traversability

- Cells exceeding the rover’s maximum slope or marked as obstacles are treated as non-traversable.
- Non-traversable cells are excluded from the navigation graph.

---

## 4. Rover Specifications

The simulated rover includes the following constraints:

- Maximum climbable slope
- Energy consumption based on:
  - Terrain type
  - Elevation change
  - Movement direction (straight vs. diagonal)
- Limited operational budget (energy and time)

These constraints directly influence the movement cost between adjacent grid cells.

---

## 5. Graph Construction

The terrain is converted into a weighted graph as follows:

- Each grid cell is modeled as a node.
- Edges connect neighboring cells in an 8-connected grid.
- Edge weights represent traversal cost computed from:
  - Base movement cost
  - Terrain difficulty
  - Elevation penalty
- Non-traversable cells are excluded from the graph.

The graph is implemented using **NetworkX**.

---

## 6. Search Algorithms

### Uninformed Search

- **Depth-First Search (DFS)**  
  Low memory usage but does not guarantee an optimal path.

- **Breadth-First Search (BFS)**  
  Finds the shortest path in terms of steps but has high memory usage.

- **Uniform Cost Search (UCS)**  
  Finds the minimum-cost path and is suitable for energy-aware navigation.

- **Iterative Deepening Search (IDS)**  
  Combines DFS space efficiency with BFS completeness.

### Informed Search

- **A\* Search**, using heuristics such as:
  - Euclidean distance to the target
  - Terrain-weighted distance
  - Elevation-aware heuristics
- **Hill Climbing**
- **Genetic Algorithm**

---

## 7. Path Reconstruction

All algorithms store parent relationships to reconstruct the rover’s path from the landing site to the target. Special care is taken in DFS and IDS to ensure that parent pointers reflect the first valid discovery of a node, preserving correctness in depth-limited searches.

---

## 8. Evaluation Criteria

The algorithms are compared based on:

- Path feasibility
- Total traversal cost
- Number of expanded nodes
- Execution time

---

## 9. Tools & Technologies

The following tools and technologies are used:

- **Python**
- **NumPy** — terrain and elevation modeling
- **NetworkX** — graph representation
- **heapq** — priority queues for UCS
- **collections.deque** — BFS and DFS queues and stacks

---

## 10. Expected Outcomes

- A working Mars rover path planning simulator
- Demonstrated trade-offs between classical search algorithms
- Evidence that cost-aware search methods (UCS and A*) are better suited for rover navigation than uninformed strategies
- A modular design allowing future expansion to multi-goal missions or real Mars terrain data

---

## 11. Conclusion

This project simulates the core challenges of autonomous Mars rover navigation using classical artificial intelligence search techniques. By modeling realistic terrain constraints and comparing multiple search strategies, the project provides valuable insight into the strengths and limitations of different path planning approaches for planetary exploration.
