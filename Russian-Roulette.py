import pygame
import random

WIDTH = 800
FPS = 30

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

coordinates = {
    1:(mid_x, mid_x - (WIDTH / 8)),
    2:(mid_x + (WIDTH / 11), mid_x - (WIDTH / 11)),
    3:(mid_x + (WIDTH / 8), mid_x),
    4:(mid_x + (WIDTH / 11), mid_x + (WIDTH / 11)),
    5:(mid_x, mid_x + (WIDTH / 8)),
    6:(mid_x - (WIDTH / 11), mid_x + (WIDTH / 11)),
    7:(mid_x - (WIDTH / 8), mid_x),
    8:(mid_x - (WIDTH / 11), mid_x - (WIDTH / 11))
}

class bullet (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( ((WIDTH // 23)*2, (WIDTH // 23)*2) )
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (coordinates[1] )

    def Left(self, i ):
        self.rect.x = coordinates[i][1]
        


class tock (pygame.sprite.Sprite):
    def __init__(self,wid_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface( ((WIDTH // 23)*2, (WIDTH // 23)*2) )
        self.image.fill(GRAYF)
        self.rect = self.image.get_rect()
        self.rect.center = (wid_x)

def start_window():
    pygame.draw.rect(screen, GREEN,(mid_x - (WIDTH / 62), mid_x - (WIDTH / 4), (WIDTH / 28), (WIDTH / 16)))
    pygame.draw.circle(screen, METAL1, (mid_x, mid_x), (WIDTH / 5.55))
    pygame.draw.circle(screen, METAL2, (mid_x, mid_x), (WIDTH / 25))
    pygame.draw.circle(screen, BLACK, (mid_x, mid_x), (WIDTH / 50))
    '''
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 8), mid_x), (WIDTH / 23), width = 2) # 3
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 8), mid_x), (WIDTH / 23), width = 2) # 7
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x + (WIDTH / 8)), (WIDTH / 23), width = 2) # 5
    pygame.draw.circle(screen, GRAYF, (mid_x, mid_x - (WIDTH / 8)), (WIDTH / 23), width = 2) # 1
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 11), mid_x - (WIDTH / 11)), (WIDTH / 23), width = 2) # 2
    pygame.draw.circle(screen, GRAYF, (mid_x + (WIDTH / 11), mid_x + (WIDTH / 11)), (WIDTH / 23), width = 2) # 4
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 11), mid_x - (WIDTH / 11)), (WIDTH / 23), width = 2) # 8 
    pygame.draw.circle(screen, GRAYF, (mid_x - (WIDTH / 11), mid_x + (WIDTH / 11)), (WIDTH / 23), width = 2) # 6
    '''


pygame.init()
screen = pygame.display.set_mode((WIDTH, WIDTH))
background_image = pygame.image.load("map.jpg").convert()
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
bullet = bullet()
tock_1 = tock(coordinates[2])
tock_2 = tock(coordinates[3])
tock_3 = tock(coordinates[4])
tock_4 = tock(coordinates[5])
tock_5 = tock(coordinates[6])
tock_6 = tock(coordinates[7])
tock_7 = tock(coordinates[8])
all_sprites.add(bullet, tock_1, tock_2, tock_3, tock_4, tock_5, tock_6, tock_7)



running = True
while running:
    screen.blit(background_image, [0,0])
    start_window()
    clock.tick(FPS)
    bullet.Left(random.randint(1, 8))
    all_sprites.draw(screen)
        





    all_sprites.draw(screen)
    pygame.display.flip()
    for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

pygame.quit()