import pygame

CELL_SIZE = 30


WHITE = (255, 255, 255)
BLUE = (100, 149, 237)     # retângulo
YELLOW = (255, 255, 0)     # círculo
BLACK = (0, 0, 0)          # obstáculo
GREEN = (0, 255, 0)        # caminho
RED = (255, 0, 0)          # start/goal


def draw_grid(screen, farm, path=None, start=None, goal=None):
    for r in range(farm.rows):
        for c in range(farm.cols):
            rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            pos = (r, c)

            # cor base
            if farm.in_rectangle(pos):
                color = BLUE
            elif farm.in_circle(pos):
                color = YELLOW
            else:
                color = WHITE

            # obstáculo
            if pos in farm.obstacles:
                color = BLACK

            pygame.draw.rect(screen, color, rect)

            # borda
            pygame.draw.rect(screen, (200, 200, 200), rect, 1)

    # caminho
    if path:
        for pos in path:
            r, c = pos
            rect = pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GREEN, rect)

    # start / goal
    if start:
        r, c = start
        pygame.draw.rect(screen, RED, pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if goal:
        r, c = goal
        pygame.draw.rect(screen, RED, pygame.Rect(c*CELL_SIZE, r*CELL_SIZE, CELL_SIZE, CELL_SIZE))


def run_visualization(farm, path, start, goal):
    pygame.init()

    width = farm.cols * CELL_SIZE
    height = farm.rows * CELL_SIZE

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Farm Pathfinding")

    running = True

    while running:
        screen.fill(WHITE)

        draw_grid(screen, farm, path, start, goal)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()