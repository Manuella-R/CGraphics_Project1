# 3D Flappy Sphere Game

This project is a modernized version of the classic Flappy Bird game, featuring a spherical bird in a 3D environment with gradient effects, as well as 3D-styled pipes. The objective is to control the vertical movement of the sphere and navigate it through the pipes while avoiding collisions.

## Project Description

The **3D Flappy Sphere Game** uses Python, Pygame, and Cairo to create a 3D effect with simple gameplay mechanics:
- Players control a spherical bird with a gradient effect that mimics realistic shading.
- The pipes are rendered with a 3D-like shading effect for visual depth.
- Players earn points by successfully navigating through the gaps in the pipes, with a lives system that allows multiple attempts before game over.

## Key Features
- **3D Gradient Effect:** The bird is rendered as a 3D sphere with a gradient effect created using Cairo, providing a visually engaging experience.
- **Pipe Class with 3D Shading:** The pipes have a shaded effect to simulate 3D depth.
- **Lives System:** Players have multiple lives, allowing several attempts before losing the game.

## Project Setup/Installation Instructions

### Prerequisites
Ensure that you have Python installed. You'll also need the following libraries:
- `pygame`
- `cairo`
- `random`
- `math`

### Steps to Set Up the Project

1. Clone this repository:
    ```bash
    git clone https://github.com/YourUsername/3D-Flappy-Sphere.git
    cd 3D-Flappy-Sphere
    ```

2. Install the necessary dependencies using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python flappy_sphere.py
    ```

## Usage Instructions

### How to Play

- Use the spacebar or mouse click to control the sphere's vertical movement.
- Navigate through the gaps between the pipes.
- Avoid collisions with the pipes; you will lose a life each time you hit a pipe.
- The game ends when you run out of lives.

### Input/Output

- **Input:** Spacebar or mouse clicks to control the bird's movement.
- **Output:** A score displayed on the screen showing how many pipes you've successfully passed through.

## Project Structure
3D-Flappy-Sphere/
│
├── flappy_sphere.py         # Main game file
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation


### Key Files

- `flappy_sphere.py`: The main script that contains the game logic, including the Bird and Pipe classes.
- `requirements.txt`: A list of dependencies required to run the project. [View the file](requirements.txt).


## Acknowledgements

- The **Flappy Bird** game was originally created by **Dong Nguyen** and released by **Gears Studio**. The game’s core concept and design heavily inspired the creation of this 3D version.
- Special thanks to the creators of **Pygame** and **Cairo**, whose libraries enabled the development of this interactive game.
- Additional resources and tutorials from various contributors on platforms like StackOverflow and GitHub were invaluable in overcoming implementation challenges.

## Screenshots

**3D Flappy Sphere in Action:**

![Flappy Sphere Gameplay](screenshots/flappy_sphere_gameplay.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
