import random


class Farm:
    def __init__(self, rows, cols, rect_top_left, rect_bottom_right, circle_center, radius):
        self.rows = rows
        self.cols = cols

        # retângulo
        self.r1, self.c1 = rect_top_left
        self.r2, self.c2 = rect_bottom_right

        # círculo
        self.cx, self.cy = circle_center
        self.radius = radius

        self.obstacles = set()

    def generate_obstacles(self, rect_density=0.1, circle_density=0.3):
        for r in range(self.rows):
            for c in range(self.cols):
                pos = (r, c)

                if self.in_rectangle(pos):
                    if random.random() < rect_density:
                        self.obstacles.add(pos)

                elif self.in_circle(pos):
                    if random.random() < circle_density:
                        self.obstacles.add(pos)

    def in_bounds(self, pos):
        r, c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_obstacle(self, pos):
        return pos in self.obstacles

    def in_circle(self, pos):
        r, c = pos
        return (r - self.cx)**2 + (c - self.cy)**2 <= self.radius**2

    def in_rectangle(self, pos):
        r, c = pos
        return self.r1 <= r <= self.r2 and self.c1 <= c <= self.c2

    def is_valid_region(self, pos):
        return self.in_rectangle(pos) or self.in_circle(pos)

    def neighbors(self, pos):
        r, c = pos
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        valid = []
        for dr, dc in directions:
            new = (r+dr, c+dc)

            if not self.in_bounds(new):
                continue

            if not self.is_valid_region(new):  # 🔥 AQUI
                continue

            if self.is_obstacle(new):
                continue

            valid.append(new)

        return valid