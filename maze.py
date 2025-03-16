import pygame

from grid import Grid

pygame.init()

SCREEN_WIDTH = 840
SCREEN_HEIGHT = 840
grid_cell_size = 40

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

grid = Grid(screen, SCREEN_WIDTH, SCREEN_HEIGHT, grid_cell_size)
grid.grid_array()
grid.create_cells()
grid.find_neighbours()
grid.change_cell_color()

#
# def create_maze(c):
#     starting_cell = random.randint(0, len(c))
#     print(starting_cell)
#
# create_maze(cells)

loop = True

while loop:
    screen.fill((0,0,0))
    grid.cells_change_status()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(5)
    pygame.display.update()

pygame.quit()