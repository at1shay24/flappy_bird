import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
GREEN = (0, 255, 0)

# Pipe settings
PIPE_WIDTH = 70
PIPE_GAP = 150  # Space between top and bottom pipes
PIPE_SPEED = 3  # Speed at which pipes move

class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)  # Random pipe height
        self.top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT - self.height - PIPE_GAP)

    def move(self):
        """Moves the pipe to the left."""
        self.x -= PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, screen):
        """Draws the pipes on the screen."""
        pygame.draw.rect(screen, GREEN, self.top_rect)
        pygame.draw.rect(screen, GREEN, self.bottom_rect)

# Pipe list
pipes = [Pipe(WIDTH + i * 200) for i in range(3)]  # Generates pipes at intervals

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))  # Clear screen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw pipes
    for pipe in pipes:
        pipe.move()
        pipe.draw(screen)

    # Remove pipes that move off-screen and add new ones
    if pipes[0].x + PIPE_WIDTH < 0:
        pipes.pop(0)  # Remove the first pipe
        pipes.append(Pipe(WIDTH))  # Add a new pipe at the end

    pygame.display.flip()  # Update display
    clock.tick(30)  # Control frame rate

pygame.quit()
