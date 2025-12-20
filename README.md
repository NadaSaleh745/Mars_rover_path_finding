#  Mars Rover Path Planning Simulator


A high-fidelity simulation of autonomous Mars rover navigation using classical Artificial Intelligence search algorithms. This project generates 3D Martian terrain (including elevation changes and obstacles) and benchmarks various pathfinding strategies based on efficiency, cost, and feasibility.

---

##  Table of Contents
- [About the Project](#about-the-project)
- [Features](#features)
- [Terrain & Cost Model](#terrain--cost-model)
- [Algorithms Implemented](#algorithms-implemented)
- [Visualization](#visualization)
- [Installation & Usage](#installation--usage)
- [Results](#results)

---

##  About the Project

Autonomous navigation is critical for planetary rovers where real-time human control is impossible due to communication delays. This simulator models the challenges of traversing the Martian surface, including:
- **Steep Slopes:** Climbing requires more energy and poses a risk of sliding.
- **Hazardous Terrain:** Sand, rocks, and cliffs affect movement speed and safety.
- **Energy Constraints:** Finding the shortest path isn't always best; finding the most energy-efficient path is key.

The goal is to navigate a rover from a landing site to a scientific target using a weighted graph representation of the terrain.

---

##  Features

- **Procedural Terrain Generation:** Creates random grid maps with varying terrain types and smooth elevation rolling hills using Gaussian filtering.
- **Physics-Based Cost Function:** Movement cost is calculated based on:
  - Diagonal (octile) distance
  - Terrain friction (Sand vs. Rock).
  - Slope penalties (Moving uphill is costlier).
- **High-Fidelity 3D Visualization:** "Cinematic" animations of the rover traversing the path using Matplotlib and FFmpeg.
- **Comparative Analysis:** Benchmarks execution time, path length, and node expansion counts across algorithms.

---

##  Terrain & Cost Model

The simulation operates on an $N \times M$ grid where every cell $(x, y)$ has:
1. **Elevation ($Z$):** Height of the terrain.
2. **Terrain Type ($T$):**

| Terrain Type | Color Representation | Cost Factor | Description |
| :--- | :--- | :--- | :--- |
| **Sand** | Pale Goldenrod | 4 | Easy to traverse. |
| **Rough** | Sandy Brown | 8 | Moderate difficulty. |
| **Rocky** | Saddle Brown | 13 | Hard traversal. |
| **Cliff** | Dark Slate Grey | $\infty$ | Impassable obstacle. |

**Movement Cost Formula:**

$$
Cost = Distance \times TerrainFactor \times (1 + Slope)
$$


---

##  Algorithms Implemented

The project implements and compares the following search strategies:

### Uninformed Search
1. **Breadth-First Search (BFS):** Guarantees the shortest path in terms of *steps*, ignoring terrain cost.
2. **Depth-First Search (DFS):** Explores deep into the graph; memory efficient but produces non-optimal, winding paths.
3. **Iterative Deepening Search (IDS):** Combines the space efficiency of DFS with the completeness of BFS.
4. **Uniform Cost Search (UCS):** Explores based on cumulative path cost. Essential for energy-optimized navigation.

### Informed Search
5. **A\* (A-Star):** Uses a heuristic (Diagonal Distance + Terrain Weights) to guide the search towards the goal efficiently.
6. **Hill Climbing:** A local search algorithm that makes greedy choices. Fast, but can get stuck in local optima (dead ends).

---

##  Visualization

The project features a custom 3D visualization engine built with `matplotlib.animation`.

- **Interpolated Movement:** The rover doesn't just "jump" between cells; movement is smoothed and interpolated over the 3D surface.
- **Surface Smoothing:** Raw grid elevation is smoothed using Gaussian filters for a realistic look.
- **Heatmaps:** Visualizes the search space (nodes visited) for algorithms like A* and UCS, and the heuristic values for A* algorithm.

---

##  Installation & Usage

### Prerequisites
- Python 3.8+
- [FFmpeg](https://ffmpeg.org/) (Required for saving animations)

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mars-rover-path-finding.git
   cd mars-rover-path-finding
   ```

2. **Install dependencies:**
   ```bash
   pip install numpy matplotlib networkx scipy pandas ipython
   ```

3. **Run the Simulation:**
   Open the Jupyter Notebook to run experiments and generate animations.
   ```bash
   jupyter notebook src/problem/simulation.ipynb
   ```

---

## Results

The simulation compares algorithms based on:
- **Time:** Execution speed.
- **Nodes Explored:** Memory and computational efficiency.
- **Path Cost:** Total energy/effort for the rover.

*General findings:*
- **UCS** provides optimality but has to explore more nodes.
-  <b>A* </b> offers the best balance between speed and optimality.
- **BFS** is optimal for distance but dangerous for high-cost terrain.
- **Hill Climbing** is the fastest but often fails in complex mazes or cliffs.
