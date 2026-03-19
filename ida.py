from utils import heuristic


def ida(farm, start, goal, E_max):
    bound = heuristic(start, goal)

    def search(path, g, bound):
        node = path[-1]
        f = g + heuristic(node, goal)

        #  energia + limite
        if f > bound or g > E_max:
            return f

        if node == goal:
            return path

        min_bound = float('inf')

        for neighbor in farm.neighbors(node):
            if neighbor in path:
                continue

            result = search(path + [neighbor], g + 1, bound)

            if isinstance(result, list):
                return result

            min_bound = min(min_bound, result)

        return min_bound

    path = [start]

    while True:
        result = search(path, 0, bound)

        if isinstance(result, list):
            return result

        if result == float('inf'):
            return None

        bound = result