import pygame
import random
from grid import Grid

pygame.init()

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
grid_cell_size = 40

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, grid_cell_size)


def starting_cell():
    cell = grid.cells[random.randint(0, len(grid.cells))]
    return cell

starting_cell().color = (20,50,250)

def maze_creation(cells):
    for i in range(len(cells)):
        pass

# maze_creation(grid.cells)

loop = True

while loop:
    screen.fill((0,0,0))
    grid.show_cells()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(5)
    pygame.display.update()

pygame.quit()