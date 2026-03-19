from utils import heuristic


def rbfs(farm, start, goal, E_max):
    def rbfs_rec(node, g, f_limit, path):
        if node == goal:
            return path, 0

        successors = []

        for n in farm.neighbors(node):
            if n in path:
                continue

            g_new = g + 1

            #  energia
            if g_new > E_max:
                continue

            f = g_new + heuristic(n, goal)
            successors.append([n, f, g_new])

        if not successors:
            return None, float('inf')

        while True:
            successors.sort(key=lambda x: x[1])
            best = successors[0]

            if best[1] > f_limit:
                return None, best[1]

            alt = successors[1][1] if len(successors) > 1 else float('inf')

            result, best[1] = rbfs_rec(
                best[0],
                best[2],
                min(f_limit, alt),
                path + [best[0]]
            )

            if result:
                return result, best[1]

    result, _ = rbfs_rec(start, 0, float('inf'), [start])
    return result