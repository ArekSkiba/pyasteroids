import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from particle import Particle
from hud import HUD

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    clock = pygame.time.Clock()
    
    dt = 0
    particles = []
    hud = HUD()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField(hud=hud)

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if not player.invulnerable:
                if player.collision(obj):
                    player.invulnerable = True
                    player.invulnerability_timer = 3
                    player.lives -= 1
                    if player.lives <= 0:
                        print("Game over!")
                        sys.exit()
                    else:
                        # Respawn player at center of screen
                        player.position.x = SCREEN_WIDTH / 2
                        player.position.y = SCREEN_HEIGHT / 2

        # Separately check bullet collisions with asteroids
        for obj in asteroids:
            for x in shots:
                if x.collision(obj):
                    x.kill()
                    # Create particles at asteroid position before splitting
                    for _ in range(10):
                        particles.append(Particle(obj.position))
                    obj.split()
      
        particles = [particle for particle in particles if particle.is_alive()]
        for particle in particles:
            particle.update()            

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        for particle in particles:
            particle.draw(screen)
            hud.draw(screen, player)

        # Add HUD drawing here
        hud.draw(screen, player)    

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()