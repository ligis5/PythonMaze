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

# where maze will start to form from
first_cell = grid.cells[random.randint(0, len(grid.cells))]
first_cell.color = (20,50,250)

def choose_wall(cell):
    cell_walls_exist = []
    for i in range(len(cell.walls)):
        if list(cell.walls.values())[i]:
            cell_walls_exist.append(list(cell.walls.keys())[i])
    if cell_walls_exist:
        return random.choice(cell_walls_exist)
    else: return False

def choose_rand_neighbour_cell(cell):
    n_cells = []
    for i in range(len(cell.neighbours)):
        key = list(cell.neighbours.keys())[i]
        if cell.neighbours[key]:
            n_cells.append(cell.neighbours[key])
    if n_cells: return random.choice(n_cells)

def maze_creation(cell):
    cell_wall = choose_wall(cell)
    if cell_wall:
        cell.set_wall_status(cell_wall, False)
        if cell_wall == "bottom": neighbour_wall = "top"
        if cell_wall == "top": neighbour_wall = "bottom"
        if cell_wall == "left": neighbour_wall = "right"
        if cell_wall == "right": neighbour_wall = "left"
        # choosing next cell based on last wall opened, right wall equals right neighbour cell etc.
        next_cell = cell.neighbours[cell_wall]
        if next_cell and next_cell.visited:
            next_cell.set_wall_status(neighbour_wall, False)
            maze_creation(next_cell)
        else:
           maze_creation(choose_rand_neighbour_cell(cell))
        cell.visited = True

maze_creation(first_cell)

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