import pygame
from cell import Cell
import random
import numpy as np

pygame.init()

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
grid_cell_size = 40

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creating 2D array
def grid_array():
    outer_wall_zone = grid_cell_size / 2
    i = outer_wall_zone
    x = []
    while i < SCREEN_WIDTH - outer_wall_zone:
        x.append(i)
        i+=grid_cell_size
    j = outer_wall_zone
    y = []
    while j < SCREEN_HEIGHT - outer_wall_zone:
        y.append(j)
        j += grid_cell_size

    x_array = np.array(x)
    y_array = np.array(y)
    X, Y = np.meshgrid(x_array, y_array)
    return X, Y

grid = grid_array()

def find_neighbours(cells):
    # finding neighbours and assigning neighbouring cells.
    # i for number in row, j for number in column and multiply by row or column to get correct cell, because cells are in 1D array
    r = len(grid[0][0])
    c = len(grid[1][0])
    for i in range(r):
        for j in range(c):
            neighbours = {"top": None, "left": None, "bottom": None, "right": None}
            if i < 0 or i >= r or j < 0 or j >= c:
                neighbours.update({"top": None, "left": None, "bottom": None, "right": None})
            if i > 0 and i < r - 1:
                neighbours.update({"left": (cells[(i - 1) + j * c]), "right": (cells[(i + 1) + j * c])})
            if j > 0 and j < c - 1:
                neighbours.update({"top": (cells[i + (j - 1) * r]), "bottom": (cells[i + (j + 1) * r])})
            cells[i + j * r].set_neighbours(neighbours)

def create_cells(g):
    c = []
    for i in range(len(g[0])):
        for j in range(len(g[1])):
            c.append(Cell(screen, g[0][i][j], g[1][i][j], grid_cell_size))
    return c

cells = create_cells(grid)

find_neighbours(cells)
cells[10].set_color((0,100,0))
cells[10].neighbours["right"].set_color((100, 100 ,100))

#
# def create_maze(c):
#     starting_cell = random.randint(0, len(c))
#     print(starting_cell)
#
# create_maze(cells)

loop = True

while loop:
    screen.fill((0,0,0))
    i = 0
    while i < len(cells):
        cells[i].draw_cell()
        r = random.randint(0, 10)
        if r > 7:
            cells[i].set_wall_status(random.choice([True, False]),random.choice([True, False]),random.choice([True, False]),random.choice([True, False]))
        i+= 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(5)
    pygame.display.update()

pygame.quit()