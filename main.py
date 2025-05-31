import pygame
from constants import *
from player import *



def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill((0,0,0))
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()



print("Starting Asteroids!")
print("Screen width: 1280")
print("Screen height: 720")

if __name__ == "__main__":
    main()