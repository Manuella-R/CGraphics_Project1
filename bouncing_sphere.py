from vpython import sphere, vector, scene, curve
import random
import time

# Create a scene
scene.title = "3D Sphere Simulation"
scene.width = 800
scene.height = 600

# Create a box outline
box_size = 6
box_lines = [
    curve(pos=[vector(-box_size, -box_size, -box_size), vector(box_size, -box_size, -box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, -box_size, -box_size), vector(box_size, box_size, -box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, box_size, -box_size), vector(-box_size, box_size, -box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(-box_size, box_size, -box_size), vector(-box_size, -box_size, -box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(-box_size, -box_size, box_size), vector(box_size, -box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, -box_size, box_size), vector(box_size, box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, box_size, box_size), vector(-box_size, box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(-box_size, box_size, box_size), vector(-box_size, -box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(-box_size, -box_size, -box_size), vector(-box_size, -box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, -box_size, -box_size), vector(box_size, -box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(box_size, box_size, -box_size), vector(box_size, box_size, box_size)], color=vector(1, 1, 1)),
    curve(pos=[vector(-box_size, box_size, -box_size), vector(-box_size, box_size, box_size)], color=vector(1, 1, 1)),
]
