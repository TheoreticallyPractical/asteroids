import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vec = self.velocity
            vec1 = vec.rotate(random_angle)
            vec2 = vec.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_astroid1.velocity = vec1 * 1.2
            new_astroid2.velocity = vec2 * 1.2


