import pygame
import numpy


# constants
DOT_SIZE = 20
FIELD_WIDTH = 10
FIELD_HEIGHT = 10
SCREEN_WIDTH = DOT_SIZE * FIELD_WIDTH
SCREEN_HEIGHT = DOT_SIZE * FIELD_HEIGHT
FPS = 2

# window initialization
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game of life')
clock = pygame.time.Clock()

# main loop
run = True
while run:
    clock.tick(FPS)

    # input handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
