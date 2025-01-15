import pygame
from constants import *

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.score = 0
        # Load heart image and scale it
        self.heart_image = pygame.image.load("assets/heart.png")
        self.heart_image = pygame.transform.scale(self.heart_image, (22, 20))
    
    def draw_heart(self, screen, x, y):
        screen.blit(self.heart_image, (x, y))
    
    def update_score(self, points):
        self.score += points
    
    def draw(self, screen, player):
        # Draw score
        score_text = self.font.render(f"Score: {self.score}", True, "white")
        screen.blit(score_text, (10, 10))
        
        # Draw hearts for lives
        start_x = SCREEN_WIDTH - 80
        start_y = 10
        spacing = 25
        for i in range(player.lives):
            self.draw_heart(screen, start_x + (i * spacing), start_y)