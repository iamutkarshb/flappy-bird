import pygame,sys

pygame.init()

screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
bg_surface =pygame.image.load("assets/background-day.png").convert()
base_surface =pygame.image.load("assets/base.png").convert()
base_x_pos = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surface,(0,0))
    base_x_pos -=1
    screen.blit(base_surface,(base_x_pos,450))
    pygame.display.update()
    clock.tick(120)