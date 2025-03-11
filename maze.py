import pygame

pygame.init()

WALL_THICKNESS = 2

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# change how big squares are
grid_density = 40

# Making 2D array
def grid_array():
    i = 0
    grid = []
    while i <= SCREEN_WIDTH:
        i+=grid_density
        j = 0
        x_grid = []
        while j <= SCREEN_HEIGHT:
            x_grid.append([j])
            j += grid_density
        grid.append(x_grid)
    return grid

def find_walls(grid):

    pass

def mazify_grid(grid):

    pass

def draw_cells(grid):
        for j in range(len(grid[0])):
            for x in range(len(grid[0][0])):
                # X axis lines
                if x == 0 or x == len(grid[0][0]) - 1:
                    pygame.draw.rect(screen, (120, 0, 60), [grid[0][j][x]["x"], grid[1][j][0]["y"], grid[0][j][x]["x"] + grid_density, grid[1][j][0]["y"]], 2)
                else:
                    pygame.draw.line(screen, (60, 120, 60), (grid[0][j][x]["x"], grid[1][j][0]["y"]),
                                     (grid[0][j][x]["x"] + grid_density, grid[1][j][0]["y"]), 2)

                for y in range(len(grid[1][0])):
                    # Y axis lines
                    if y == 0 or y == len(grid[1][0]) - 1:
                        pygame.draw.line(screen, (120, 0, 60), (grid[0][j][y]["x"], grid[1][j][x]["y"]),
                                         (grid[0][j][y]["x"], grid[1][j][x]["y"] + grid_density), 2)
                    else:
                        pygame.draw.line(screen, (60, 120, 60), (grid[0][j][y]["x"], grid[1][j][x]["y"]),
                                     (grid[0][j][y]["x"], grid[1][j][x]["y"] + grid_density), 2)

loop = True


grid = grid_array()
find_walls(grid)

# mazify_grid(grid)
print(grid)
while loop:
    screen.fill((0,0,0))

    # draw_cells(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(10)
    pygame.display.update()

pygame.quit()