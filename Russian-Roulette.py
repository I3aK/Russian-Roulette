import pygame
import random

WIDTH = 800

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (150, 50, 50)
GREEN = (50, 150, 50)
BLUE = (117, 187, 253)
GRAYF = (58, 58, 58)
METAL1 = (222, 224, 223)
METAL2 = (200, 204, 203)

mid_x = WIDTH // 2

class bullet (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((mid_x,mid_x - (WIDTH / 32)))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

def start_window():
    pygame.draw.rect(screen, RED,(mid_x - (WIDTH / 62), mid_x - (WIDTH / 4), (WIDTH / 28), (WIDTH / 16)))
    pygame.draw.circle(screen, METAL1, (mid_x, mid_x), (WIDTH / 5.55))
    pygame.draw.circle(screen, METAL2, (mid_x, mid_x), (WIDTH / 25))
    pygame.draw.circle(screen, BLACK, (mid_x, mid_x), (WIDTH / 50))
<<<<<<< HEAD
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 32), mid_x), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 32), mid_x), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x + (WIDTH / 32)), (WIDTH / 100), width = 2)
    #вурхняя точка
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x - (WIDTH / 32)), (WIDTH / 100), width = 2)

    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 44.4), mid_x - (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 44.4), mid_x + (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 44.4), mid_x - (WIDTH / 44.4)), (WIDTH / 100), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 44.4), mid_x + (WIDTH / 44.4)), (WIDTH / 100), width = 2)
=======
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 8), mid_x), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 8), mid_x), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x + (WIDTH / 8)), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x - (WIDTH / 8)), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 11), mid_x - (WIDTH / 11)), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 11), mid_x + (WIDTH / 11)), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 11), mid_x - (WIDTH / 11)), (WIDTH / 23), width = 2)
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 11), mid_x + (WIDTH / 11)), (WIDTH / 23), width = 2)

>>>>>>> e5b1d05c5552f917dd07e1fbb15e6a24dc4f8671

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