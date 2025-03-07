import pygame

pygame.init()

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900

clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

loop = True

while loop:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    clock.tick(10)
    pygame.display.update()

pygame.quit()