import heapq
from utils import heuristic, reconstruct_path


def astar(farm, start, goal, E_max):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in farm.neighbors(current):
            tentative_g = g_score[current] + 1  # custo = 1

            #  RESTRIÇÃO DE ENERGIA
            if tentative_g > E_max:
                continue

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g

                f = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_list, (f, neighbor))
                came_from[neighbor] = current

    return None