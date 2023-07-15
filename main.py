import pygame

from star import Star

# Screen dimensions
WIDTH, HEIGHT = 800, 800
# The number of stars in the starfield
NUM_STARS = 800


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    stars = [Star() for _ in range(NUM_STARS)]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # fill screen with black

        for star in stars:
            star.update()
            pos = star.project()
            radius = star.get_radius()
            brightness = star.get_brightness()
            color = (brightness, brightness, brightness)
            pygame.draw.circle(screen, color, (int(pos[0]), int(pos[1])), int(radius))

        pygame.display.flip()  # update display

    pygame.quit()


if __name__ == "__main__":
    main()
