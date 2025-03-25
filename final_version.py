import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_X = 50
bird_y = HEIGHT // 2
BIRD_RADIUS = 15
g = 0.5
JUMP = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_VEL = -3

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_y_velocity = 0
score = 0
high_score = 0
pipes = []

def create_pipe():
    height = random.randint(100, 400)
    pipes.append([WIDTH, height, False])

def move_pipes():
    global score, PIPE_VEL
    for pipe in pipes:
        pipe[0] += PIPE_VEL
        if pipe[0] + PIPE_WIDTH < BIRD_X and not pipe[2]:
            pipe[2] = True
            score += 1
            PIPE_VEL -= 0.05
    if pipes and pipes[0][0] < -PIPE_WIDTH:
        pipes.pop(0)

def draw_pipes():
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, (pipe[0], 0, PIPE_WIDTH, pipe[1]))
        pygame.draw.rect(screen, GREEN, (pipe[0], pipe[1] + PIPE_GAP, PIPE_WIDTH, HEIGHT - pipe[1] - PIPE_GAP))

def check_collision():
    if bird_y - BIRD_RADIUS <= 0 or bird_y + BIRD_RADIUS >= HEIGHT:
        return True
    for pipe in pipes:
        if pipe[0] < BIRD_X + BIRD_RADIUS < pipe[0] + PIPE_WIDTH:
            if not (bird_y - BIRD_RADIUS > pipe[1] and bird_y + BIRD_RADIUS < pipe[1] + PIPE_GAP):
                return True
    return False

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
    bird_y += bird_y_velocity

    if frame_count % 90 == 0:
        create_pipe()
    move_pipes()
    
    draw_pipes()
    pygame.draw.circle(screen, BLUE, (BIRD_X, int(bird_y)), BIRD_RADIUS)

    if check_collision():
        print("Game Over: You hit a pipe!")
        running = False

    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(30)
    frame_count += 1

screen.fill(WHITE)
font = pygame.font.SysFont(None, 48)
game_over_text = font.render("Game Over", True, BLACK)
score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
screen.blit(score_text, (WIDTH//2 - 100, HEIGHT//2))
pygame.display.update()
pygame.time.delay(2000)

pygame.quit()
