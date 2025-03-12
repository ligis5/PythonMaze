import pygame
from cell import Cell
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
grid_cell_size = 40

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def grid_array():
    # used to create outside layer with no grid
    outer_wall_zone = grid_cell_size / 2
    i = outer_wall_zone
    grid = []
    while i < SCREEN_WIDTH - outer_wall_zone:
        j = outer_wall_zone
        while j < SCREEN_HEIGHT - outer_wall_zone:
            grid.append({"x":i,"y":j})
            j+= grid_cell_size
        i+= grid_cell_size
    return grid

def create_cells(grid):
    c = []
    for i in range(len(grid)):
        c.append(Cell(screen, grid_array()[i], grid_cell_size))
    return c

cells = create_cells(grid_array())

def create_maze(c):
    starting_cell = random.randint(0, len(c))
    print(starting_cell)

create_maze(cells)


loop = True

while loop:
    screen.fill((0,0,0))
    i = 0
    while i < len(grid_array()):
        cells[i].draw_cell()
        r = random.randint(0, 10)
        if r > 7:
            cells[i].change_wall_status(random.choice([True, False]),random.choice([True, False]),random.choice([True, False]),random.choice([True, False]))
        i+= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(5)
    pygame.display.update()

pygame.quit()