import pygame
import numpy as np

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def grid_array():
    i = 20
    x = []
    while i < SCREEN_WIDTH:
        x.append(i)
        i+=20
    j = 20
    y = []
    while j < SCREEN_HEIGHT:
        y.append(j)
        j += 20

    x_array = np.array(x)
    y_array = np.array(y)
    X, Y = np.meshgrid(x_array, y_array)
    return X, Y

def draw_cells(grid):
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[0]):
            j+=1
            k = 0
            while k < len(grid[0][0]):
                print(grid[i][j][k])
                # pygame.draw.line(screen, (255, 0, 100), (grid[i][j][k], grid[1][0][0]), (grid[i][j][k], grid[1][0][0]),2)
                k+=1
        i+=1

loop = True

while loop:
    screen.fill((0,0,0))
    draw_cells(grid_array())
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(10)
    pygame.display.update()

pygame.quit()