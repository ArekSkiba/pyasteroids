import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius, hud=None):
        super().__init__(x, y, radius)
        self.hud = hud

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            if self.hud:
                self.hud.update_score(2)
            return
        else:
            if self.hud:
                self.hud.update_score(1)
        
            random_angle = random.uniform(20,50)
            vector_one = self.velocity.rotate(random_angle)
            vector_two = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            asteroid_one = Asteroid(self.position.x, self.position.y, new_radius, hud=self.hud)
            asteroid_two = Asteroid(self.position.x, self.position.y, new_radius, hud=self.hud)
            asteroid_one.velocity = vector_one  * 1.2
            asteroid_two.velocity = vector_two  * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt