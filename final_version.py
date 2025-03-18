import pygame
import random


pygame.init()


WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, HEIGHT // 2
BIRD_RADIUS = 15
g = 0.5  
JUMP = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_VEL = -3

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_y_velocity = 0

pipes = []
def create_pipe():
    height = random.randint(100, 400)
    pipes.append([WIDTH, height])

def move_pipes():
    for pipe in pipes:
        pipe[0] += PIPE_VEL
    if pipes and pipes[0][0] < -PIPE_WIDTH:
        pipes.pop(0)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP))

clock = pygame.time.Clock()
running = True
frame_count = 0
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird_y_velocity = JUMP

    bird_y_velocity += g
    BIRD_Y += bird_y_velocity

    if frame_count % 90 == 0:
        create_pipe()
    move_pipes()
    
    draw_pipes()
    pygame.draw.circle(screen, BLUE, (BIRD_X, int(BIRD_Y)), BIRD_RADIUS)
    
    pygame.display.update()
    clock.tick(30)
    frame_count += 1
    
pygame.quit()
