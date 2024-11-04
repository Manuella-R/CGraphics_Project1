from vpython import sphere, vector, scene

# Create a scene
scene.title = "3D Sphere"
scene.width = 800
scene.height = 600

# Create a sphere at position (0, 0, 0) with radius 1 and color red
my_sphere = sphere(pos=vector(0, 0, 0), radius=1, color=vector(1, 0, 0))

# Keep the window open
while True:
    pass  # This keeps the window open
