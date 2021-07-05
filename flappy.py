import pygame,sys

pygame.init()

screen = pygame.display.set_mode((288,512))
clock = pygame.time.clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(120)