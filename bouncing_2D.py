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
