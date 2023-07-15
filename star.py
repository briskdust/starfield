import random

# Screen dimensions
WIDTH, HEIGHT = 800, 800

# Starfield parameters
STAR_SPEED = 0.01
STAR_SIZE = 3


def translate_coordinates(x, y):
    """Translate (x, y) coordinates from a center origin to a top-left origin."""
    return WIDTH / 2 + x, HEIGHT / 2 + y


class Star:
    def __init__(self):
        # Position in 3D space
        self.x = random.uniform(-WIDTH / 2, WIDTH / 2)
        self.y = random.uniform(-HEIGHT / 2, HEIGHT / 2)
        self.z = random.uniform(0, WIDTH / 16)  # Distance from the screen (used for the 3D effect)

    def update(self):
        # Move star closer (decrease z)
        self.z -= STAR_SPEED

        # If the star has moved past the screen, reset it
        if self.z <= 0:
            self.__init__()

    def project(self):
        # Project the 3D position to 2D space
        x = self.x / self.z
        y = self.y / self.z
        return translate_coordinates(x, y)

    def get_radius(self):
        # Calculate star radius based on z (distance from screen)
        return STAR_SIZE / self.z

    def get_brightness(self):
        # Calculate star brightness based on z (distance from screen)
        return min(255, 255 / self.z)
