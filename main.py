from farm import Farm
from astar import astar
from ida import ida
from rbfs import rbfs
from grid import run_visualization
import time
import random
import tracemalloc


# CONFIG
rows, cols = 20, 20
circle_center = (10, 10)
radius = 5

rect_top_left = (2, 2)
rect_bottom_right = (10, 5)

start = (3, 3)
goal = (10, 13)

E_max = 50
random.seed(42) 


# SETUP
farm = Farm(
    rows,
    cols,
    rect_top_left,
    rect_bottom_right,
    circle_center,
    radius
)
farm.generate_obstacles(0.2)

# garante que start e goal não são obstáculos
farm.obstacles.discard(start)
farm.obstacles.discard(goal)

def run_astar(farm, start, goal, E_max):
    tracemalloc.start()
    t0 = time.perf_counter()

    path = astar(farm, start, goal, E_max)

    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    run_visualization(farm, path, start, goal)

    print("\n=== A* ===")
    print("Caminho:", path)
    print("Energia usada:", len(path) if path else None)
    print("Tempo:", t1 - t0)
    print("Memória:", peak)

def run_ida(farm, start, goal, E_max):
    tracemalloc.start()
    t0 = time.perf_counter()

    path = ida(farm, start, goal, E_max)

    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    run_visualization(farm, path, start, goal)

    print("\n=== IDA* ===")
    print("Caminho:", path)
    print("Energia usada:", len(path) if path else None)
    print("Tempo:", t1 - t0)
    print("Memória:", peak)


def run_rbfs(farm, start, goal, E_max):
    tracemalloc.start()
    t0 = time.perf_counter()

    path = rbfs(farm, start, goal, E_max)

    t1 = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    run_visualization(farm, path, start, goal)

    print("\n=== RBFS ===")
    print("Caminho:", path)
    print("Energia usada:", len(path) if path else None)
    print("Tempo:", t1 - t0)
    print("Memória:", peak)



# run_astar(farm, start, goal, E_max)
# run_ida(farm, start, goal, E_max)
run_rbfs(farm, start, goal, E_max)