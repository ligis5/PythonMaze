import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1000

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# change how big squares are
grid_density = 20

# Making 2D array
def grid_array():
    i = 0
    x = []
    while i < SCREEN_WIDTH:
        x.append({"x":i,"exist": True})
        i+=grid_density
    j = 0
    y = []
    while j < SCREEN_HEIGHT:
        y.append({"y":j,"exist": True})
        j += grid_density

    x_array = np.array(x)
    y_array = np.array(y)
    X, Y = np.meshgrid(x_array, y_array)
    return X, Y

# def mazify_grid():
#
#     pass

def draw_cells(grid):
        for j in range(len(grid[0])):
            for x in range(len(grid[0][0])):
                for y in range(len(grid[1][0])):
                    # X axis lines
                    pygame.draw.line(screen, (60, 60, 60), (grid[0][j][x]["x"], grid[1][j][y]["y"]), (grid[0][j][x]["x"] + grid_density, grid[1][j][y]["y"]),2)
                    # Y axis lines
                    pygame.draw.line(screen, (60, 60, 60), (grid[0][j][y]["x"], grid[1][j][x]["y"]),
                                     (grid[0][j][y]["x"], grid[1][j][x]["y"] + grid_density), 2)

loop = True


grid = grid_array()

while loop:
    screen.fill((0,0,0))
    draw_cells(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(10)
    pygame.display.update()

pygame.quit()