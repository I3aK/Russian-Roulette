import pygame
import random

WIDTH = 800

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (50, 150, 50)
GREEN = (0, 255, 0)
BLUE = (117, 187, 253)
GRAYF = (58, 58, 58)
METAL1 = (222, 224, 223)
METAL2 = (200, 204, 203)

mid_x = WIDTH // 2

def start_window():
    pygame.draw.rect(screen, RED,(mid_x - (WIDTH / 100), mid_x - (WIDTH / 10), (WIDTH / 100), (WIDTH / 100)))
    pygame.draw.circle(screen, METAL1, (mid_x, mid_x), (WIDTH / 5.55))
    pygame.draw.circle(screen, METAL2, (mid_x, mid_x), (WIDTH / 25))
    pygame.draw.circle(screen, BLACK, (mid_x, mid_x), (WIDTH / 50))
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 32), mid_x), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 32), mid_x), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x + (WIDTH / 32)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x - (WIDTH / 32)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 44.4), mid_x - (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 44.4), mid_x + (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 44.4), mid_x - (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 44.4), mid_x + (WIDTH / 44.4)), (WIDTH / 100), width = 2)

pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
background_image = pygame.image.load("map.jpg").convert()

running = True
while running:
    screen.blit(background_image, [0,0])
    start_window()








    pygame.display.flip()
    for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

pygame.quit()