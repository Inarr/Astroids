import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x,y,radius)
        #self.add(self.containers)
        self.velocity = velocity
    
    def draw(self,screen):
        pygame.draw.circle(screen,"white",(self.position.x, self.position.y),SHOT_RADIUS,2)
    
    def update(self,dt):
        self.position += self.velocity * dt