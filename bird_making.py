import pygame

# Bird settings
BIRD_X = 100  # Fixed x-position of the bird
BIRD_RADIUS = 20  # Size of the bird
GRAVITY = 0.5  # Gravity effect
JUMP_STRENGTH = -10  # Jump force

class Bird:
    def __init__(self):
        self.y = 300  # Starting y-position of the bird
        self.velocity = 0  # Initial speed (falling velocity)
        
    def jump(self):
        """Makes the bird jump when a key is pressed."""
        self.velocity = JUMP_STRENGTH  # Apply an upward force

    def move(self):
        """Applies gravity and moves the bird down."""
        self.velocity += GRAVITY  # Increase downward speed
        self.y += self.velocity  # Move bird down

    def draw(self, screen):
        """Draws the bird on the screen."""
        pygame.draw.circle(screen, (255, 255, 0), (BIRD_X, int(self.y)), BIRD_RADIUS)  # Yellow circle
