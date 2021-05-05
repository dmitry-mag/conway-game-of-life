import pygame
import numpy as np


# constants
DOT_SIZE = 20
FIELD_WIDTH = 60
FIELD_HEIGHT = 30
SCREEN_WIDTH = DOT_SIZE * FIELD_WIDTH
SCREEN_HEIGHT = DOT_SIZE * FIELD_HEIGHT
FPS = 3
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

# window initialization
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('game of life')
clock = pygame.time.Clock()

# create start array with empty borders
cell_array = np.random.randint(0, 2, (FIELD_HEIGHT, FIELD_WIDTH))
cell_array[0,:] = 0
cell_array[-1,:] = 0
cell_array[:,0] = 0
cell_array[:,-1] = 0


def next_generation(array):
    """ return new generation array """
    cell_array_new = np.zeros_like(array)
    for row in range(1, FIELD_HEIGHT - 1):
        for cell in range(1, FIELD_WIDTH - 1):
            neighbor_sum = array[row - 1: row + 2, 
                cell - 1: cell + 2].sum() - array[row, cell]
            if array[row][cell] == 1 and 1 < neighbor_sum < 4:
                    cell_array_new[row][cell] = 1
            elif neighbor_sum == 3:
                    cell_array_new[row][cell] = 1
    return cell_array_new
                

def draw_field(array):
    for row in range(FIELD_HEIGHT):
        for cell in range(FIELD_WIDTH):
            if array[row][cell] == 1:
                pygame.draw.rect(screen, GREEN, pygame.Rect(DOT_SIZE * cell,
                DOT_SIZE * row, DOT_SIZE, DOT_SIZE))


# main loop
run = True
first_run = True
while run:
    clock.tick(FPS)
    screen.fill(GRAY)

    # input handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # calculations and first draw
    if first_run:
        draw_field(cell_array)
        pygame.display.update()
        first_run = False
        continue
    
    cell_array = next_generation(cell_array)

    # draw field
    draw_field(cell_array)
    pygame.display.update()

pygame.quit()
