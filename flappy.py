import pygame,sys

pygame.init()

def draw_base():
    screen.blit(base_surface,(base_x_pos,450))
    screen.blit(base_surface,(base_x_pos+288,450))

screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()
bg_surface =pygame.image.load("assets/background-day.png").convert()
base_surface =pygame.image.load("assets/base.png").convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,256))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg_surface,(0,0))
    screen.blit(bird_surface,bird_rect)
    base_x_pos -=1
    draw_base()
    if base_x_pos<=-288:
        base_x_pos=0

    pygame.display.update()
    clock.tick(120)