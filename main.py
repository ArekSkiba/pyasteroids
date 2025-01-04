import pygame

print("Starting asteroids!")

# import everything from constants module
# into the current file
from constants import *

print(f"Screen width: {SCREEN_WIDTH}")
print(f"Screen height: {SCREEN_HEIGHT}")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    clock = pygame.time.Clock()
    dt = 0
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick(60) / 1000
        print(dt)


if __name__ == "__main__":
    main()