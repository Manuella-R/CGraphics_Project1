import numpy as np
import random as r
import cv2
import time

class Vector:
    def __init__(self, x, y):
        self.vector = np.array([x, y])
    
    def __add__(self, other):
        return Vector(*(self.vector + other.vector))
    
    def __sub__(self, other):
        return Vector(*(self.vector - other.vector))
    
    def __mul__(self, scalar):
        return Vector(*(self.vector * scalar))
    
    def __truediv__(self, scalar):
        return Vector(*(self.vector / scalar))
    
    def to_tuple(self):
        return tuple(np.rint(self.vector).astype(int))


class Ball:
    def __init__(self, x, y, mass, color=None):
        self.position = Vector(x, y)
        self.mass = mass
        self.acceleration = Vector(0, 0)
        self.velocity = Vector(r.uniform(-2, 2), r.uniform(-2, 2))  # Random initial velocity
        self.color = color if color is not None else np.array([r.randint(0, 255) for _ in range(3)])

    def apply_force(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.acceleration *= 0  # Reset acceleration

    def check_edge(self, width, height):
        # Bounce off edges without sticking
        if self.position.vector[0] >= width or self.position.vector[0] <= 0:
            self.velocity.vector[0] *= -1  # Reverse X velocity
        if self.position.vector[1] >= height or self.position.vector[1] <= 0:
            self.velocity.vector[1] *= -1  # Reverse Y velocity

    def bounce_away(self, mouse_pos):
        # Calculate direction away from the mouse click
        direction = self.position - mouse_pos
        if np.linalg.norm(direction.vector) > 0:  # Avoid division by zero
            self.velocity = direction / np.linalg.norm(direction.vector) * 3  # Set a bounce velocity
