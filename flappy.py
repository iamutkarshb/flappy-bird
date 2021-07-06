import pygame,sys,random

pygame.init()

def draw_base():
    screen.blit(base_surface,(base_x_pos,450))
    screen.blit(base_surface,(base_x_pos+288,450))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe =pipe_surface.get_rect(midtop =(350,random_pipe_pos))
    top_pipe =pipe_surface.get_rect(midbottom =(350,random_pipe_pos-150))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >=512:    
            screen.blit(pipe_surface,pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 450:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3 ,1)
    return new_bird



screen = pygame.display.set_mode((288,512))
clock = pygame.time.Clock()


gravity = 0.25
bird_movement = 0
game_active=True

bg_surface =pygame.image.load("assets/background-day.png").convert()
base_surface =pygame.image.load("assets/base.png").convert()
base_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
bird_rect = bird_surface.get_rect(center = (50,256))

pipe_surface = pygame.image.load('assets\pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)
pipe_height = [200,300,400]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (50,256)
                bird_movement = 0


        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())


    screen.blit(bg_surface,(0,0))

    if game_active:    
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery +=bird_movement
        screen.blit(rotated_bird,bird_rect) 
        game_active = check_collision(pipe_list)

        pipe_list=move_pipes(pipe_list)
        draw_pipes(pipe_list)

    base_x_pos -=1
    draw_base()
    if base_x_pos<=-288:
        base_x_pos=0

    pygame.display.update()
    clock.tick(120)