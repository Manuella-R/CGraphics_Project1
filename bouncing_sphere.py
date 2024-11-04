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

class Ball:
    def __init__(self, x, y, z, radius):
        self.sphere = sphere(pos=vector(x, y, z), radius=radius, color=vector(random.random(), random.random(), random.random()))
        self.velocity = vector(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))  # Reduced initial velocity

    def apply_force(self, force):
        # Apply gravity
        self.velocity += force

    def update(self):
        # Update position based on velocity
        self.sphere.pos += self.velocity

    def check_edge(self):
        # Check for edge collision and bounce with damping
        damping = 0.9  # Damping factor to reduce bounce energy
        if abs(self.sphere.pos.x) >= (box_size - self.sphere.radius):
            # Reposition slightly inside the box and reverse velocity
            self.sphere.pos.x = max(min(self.sphere.pos.x, box_size - self.sphere.radius), -box_size + self.sphere.radius)
            self.velocity.x *= -damping  # Reverse and dampen the velocity
        if abs(self.sphere.pos.y) >= (box_size - self.sphere.radius):
            # Reposition slightly inside the box and reverse velocity
            self.sphere.pos.y = max(min(self.sphere.pos.y, box_size - self.sphere.radius), -box_size + self.sphere.radius)
            self.velocity.y *= -damping  # Reverse and dampen the velocity
        if abs(self.sphere.pos.z) >= (box_size - self.sphere.radius):
            # Reposition slightly inside the box and reverse velocity
            self.sphere.pos.z = max(min(self.sphere.pos.z, box_size - self.sphere.radius), -box_size + self.sphere.radius)
            self.velocity.z *= -damping  # Reverse and dampen the velocity

# Create multiple balls with larger size
balls = []
for _ in range(1):  # Increased the number of balls for better visualization
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)
    radius = random.uniform(1.0, 1.5)  # Increased radius range
    balls.append(Ball(x, y, z, radius))

def mouse_click(evt):
    # Get the mouse click position
    mouse_pos = scene.mouse.pos
    for ball in balls:
        if (ball.sphere.pos - mouse_pos).mag < ball.sphere.radius:
            # Calculate a bounce away vector
            direction = (ball.sphere.pos - mouse_pos).norm()
            ball.velocity += direction * 2  # Bounce away with increased velocity

# Bind mouse click event
scene.bind('click', mouse_click)

# Main animation loop
while True:
    for ball in balls:
        ball.update()                         # Update ball position
        ball.check_edge()                    # Check for collisions

    # Keep the window responsive
    time.sleep(0.01)  # Control the frame rate
