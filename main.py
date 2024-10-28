import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Creating Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Instatiating a player
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    astroidfield = AsteroidField()

    gameLoopStat = True
    while gameLoopStat:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        dt = clock.tick(60)/1000
        #player.update(dt)
        #player.draw(screen)
        for element in updatable:
            element.update(dt)
        
        for element in asteroids:
            if player.check_collision(element):
                #print("Game Over!")
                sys.exit("Game over!")

        for element in drawable:
            element.draw(screen)

        pygame.display.flip()
        #clock.tick(60) 
        #dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()