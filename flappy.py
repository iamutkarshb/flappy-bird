import pygame,sys

pygame.init()

def draw_base():
    screen.blit(base_surface,(base_x_pos,450))
    screen.blit(base_surface,(base_x_pos+288,450))

def create_pipe():
    new_pipe =pipe_surface.get_rect(midtop =(350,256))
    return new_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface,pipe)

screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()

gravity = 0.25
bird_movement = 0

bg_surface =pygame.image.load("assets/background-day.png").convert()
base_surface =pygame.image.load("assets/base.png").convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface = pygame.image.load('assets\pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = 0
                bird_movement -= 6
        if event.type == SPAWNPIPE:
            pipe_list.append(create_pipe())


    screen.blit(bg_surface,(0,0))
    
    bird_movement += gravity
    bird_rect.centery +=bird_movement


    screen.blit(bird_surface,bird_rect) 

    pipe_list=move_pipes(pipe_list)
    draw_pipes(pipe_list)

    base_x_pos -=1
    draw_base()
    if base_x_pos<=-288:
        base_x_pos=0

    pygame.display.update()
    clock.tick(120)