import pygame
import random
import math
from constants import *

class Particle:
    def __init__(self, position):
        self.position = pygame.Vector2(position)
        self.random_angle = random.uniform(0, math.pi * 2)  # In radians
        self.line_length = random.uniform(5, 15)  # Random length
        self.start_lifetime = 2
        self.lifetime = self.start_lifetime
        # Define explosion colors
        explosion_colors = [
            (255, 255, 255),  # white
            (255, 255, 0),    # yellow
            (255, 165, 0),    # orange
            (255, 0, 0)       # red
        ]
        self.color = random.choice(explosion_colors)
        
        speed = random.uniform(2, 5)  # Random speed between 2 and 5
        self.velocity = pygame.Vector2(
            math.cos(self.random_angle) * speed,
            math.sin(self.random_angle) * speed
        )
        
        # Calculate end position correctly
        self.end_position = pygame.Vector2(
            self.position.x + math.cos(self.random_angle) * self.line_length,
            self.position.y + math.sin(self.random_angle) * self.line_length
        )
        self.lifetime = 2

    def draw(self, screen):
        # Calculate fade ratio (1.0 to 0.0)
        fade_ratio = self.lifetime / self.start_lifetime
        # Create fading color by multiplying original color with fade ratio
        color = (
            int(self.color[0] * fade_ratio),
            int(self.color[1] * fade_ratio),
            int(self.color[2] * fade_ratio)
        )
        pygame.draw.line(screen, color, self.position, self.end_position, width=1)
    
    def update(self):
        self.position += self.velocity
        self.end_position += self.velocity
        self.lifetime -= 0.05  # Try adjusting this value to change fade speed
        
    def is_alive(self):
        return self.lifetime > 0