import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Instatiating a player
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)

    gameLoopStat = True
    while gameLoopStat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60)/1000
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        #clock.tick(60)
        #dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()