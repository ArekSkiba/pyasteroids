import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

class ScoreManager:
    def __init__(self):
        self.score = 0

    def add_points(self, points):
        self.score += points

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    dt = 0
    score_manager = ScoreManager()
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField(score_manager=score_manager)

    Shot.containers = (shots, updatable, drawable)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if player.collision(obj):
                print("Game over!")
                sys.exit()

            for x in shots:
                if x.collision(obj):
                    print(f"Asteroid radius: {obj.radius}, Min radius for split: {ASTEROID_MIN_RADIUS}")
                    x.kill()
                    obj.split()

        screen.fill("black")     

        # Create surface for score and draw in onto the screen
        score_text = font.render(f"Score: {score_manager.score}", True, "white")
        screen.blit(score_text, (10, 10))  # (10, 10) gives a 10-pixel margin from the top-left corner

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()