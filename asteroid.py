import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        print("Split method started")  # Add this before anything else
        self.kill()
        print (f"just killed with {self.radius}")
        if self.radius <= ASTEROID_MIN_RADIUS:
            print("in the return loop")
            return
        else:
            print("Trying to create split")
            split_angle = random.uniform(20,50)
            velocity_split1 = self.velocity.rotate(split_angle)
            velocity_split2 = self.velocity.rotate(-split_angle)
            new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid1.velocity = velocity_split1 * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius)
            asteroid2.velocity = velocity_split2 * 1.2
            for group in self.groups():  # This gets all groups the sprite is in
                group.add(asteroid1, asteroid2)

