import pygame # type: ignore
from constants import *
from circleshape import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        random_angle = random.uniform(20, 50)
        new_vector_1 = self.velocity.rotate(random_angle)
        new_vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        elif ASTEROID_MIN_RADIUS < self.radius < ASTEROID_MAX_RADIUS:
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = new_vector_1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = new_vector_2 * 1.2
        elif self.radius >= ASTEROID_MAX_RADIUS:
            a1 = Asteroid(self.position.x, self.position.y, new_radius)
            a1.velocity = new_vector_1 * 1.2
            a2 = Asteroid(self.position.x, self.position.y, new_radius)
            a2.velocity = new_vector_2 * 1.2


