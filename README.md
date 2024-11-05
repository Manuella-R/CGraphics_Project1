---

# Computer graphics

This repository contains four interactive simulation projects in Python, demonstrating physics concepts in both 2D and 3D environments. Each project includes dynamic object interactions, from bouncing objects to a classic brick breaker game and a 3D flappy bird-style sphere game.

## Projects

### 1. 2D Ball Bounce Simulation (`bouncing_2D.py`)

This project simulates multiple balls bouncing within a 2D environment using OpenCV. Balls respond to mouse clicks, causing them to bounce away, mimicking real-life collision and response.

- **Key Features:**
  - Random initial velocity for each ball.
  - Realistic edge detection to prevent balls from escaping the frame.
  - Adjustable gravity and bounce dynamics on user interaction.
- **Dependencies:** `numpy`, `opencv-python`, `random`

### 2. 3D Sphere Bounce Simulation (`bouncing_sphere.py`)

This simulation uses VPython to model a 3D environment where spheres bounce within a confined box. Spheres interact with box boundaries and user mouse clicks, applying a bouncing effect with velocity dampening.

- **Key Features:**
  - 3D perspective with boundary constraints and random initial velocity.
  - Damping effect for realistic energy loss on collision.
  - User-controlled interactions to alter sphere trajectory.
- **Dependencies:** `vpython`, `random`, `time`

### 3. Brick Breaker Game (`brickbreaker.py`)

This classic game replicates a 3D-styled brick breaker using Pygame. The player controls a paddle to bounce the ball, aiming to break all bricks. Losing lives resets the game.

- **Key Features:**
  - Interactive paddle movement and ball physics.
  - 3D visual effects for paddle and brick graphics.
  - Adjustable difficulty with varying brick patterns.
- **Dependencies:** `pygame`, `math`

### 4. 3D Flappy Sphere Game (`flappy_sphere.py`)

This game is inspired by "Flappy Bird" but features a spherical bird with a 3D gradient effect, along with 3D-styled pipes. Players control the bird's vertical movement to navigate through pipes while avoiding collisions.

- **Key Features:**
  - Bird class with a 3D gradient effect created using Cairo for realistic sphere shading.
  - Pipe class with shading to simulate a 3D appearance.
  - Lives system to allow multiple attempts before game over.
- **Dependencies:** `pygame`, `random`, `cairo`, `math`

## Installation and Setup

1. Clone this repository:
    ```bash
    git clone https://github.com/MAnuella-R/CGraphics_Project1.git
    cd CGraphics_Project1
    ```

2. Install dependencies:
    ```bash
    pip install numpy opencv-python vpython pygame pycairo
    ```

3. Run each simulation individually:
   - **2D Ball Bounce:** `python bouncing_2D.py`
   - **3D Sphere Bounce:** `python bouncing_sphere.py`
   - **Brick Breaker:** `python brickbreaker.py`
   - **3D Flappy Sphere:** `python flappy_sphere.py`

## Screenshots

*(Optional: Add screenshots of each simulation here.)*

## License

This repository is licensed under the MIT License.

