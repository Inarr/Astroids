import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameLoopStat = True
    while gameLoopStat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()


if __name__ == "__main__":
    main()