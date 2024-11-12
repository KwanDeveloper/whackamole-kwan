import pygame
import random

HEADER = "Lab 10: Whack-a-mole!"

WIDTH, HEIGHT = 640, 512
COL, ROW = 20, 16

BG_COLOR, LINE_COLOR = "light green", (0, 0, 0)

MOLE_X, MOLE_Y = None, None

def new_round(screen):
    global MOLE_X, MOLE_Y
    x_unit, y_unit = WIDTH / COL, HEIGHT / ROW
    x, y = random.randrange(0, COL) * x_unit, random.randrange(0, ROW) * y_unit
    MOLE_X, MOLE_Y = (x, x + x_unit), (y, y + y_unit)
    draw_map(screen)
    spawn_mole(screen, (x, y))

def draw_map(screen):
    screen.fill(BG_COLOR)

    for i in range(1, COL):
        pygame.draw.line(screen, LINE_COLOR, (WIDTH / COL * i, 0), (WIDTH / COL * i, HEIGHT))

    for i in range(1, ROW):
        pygame.draw.line(screen, LINE_COLOR, (0, HEIGHT / ROW * i), (WIDTH, HEIGHT / ROW * i))

def spawn_mole(screen, position):
    mole_image = pygame.image.load("mole.png")
    screen.blit(mole_image, mole_image.get_rect(topleft=position))

def main():
    try:
        pygame.init()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(HEADER)

        clock = pygame.time.Clock()
        running = True

        new_round(screen)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if MOLE_X[0] < x < MOLE_X[1] and MOLE_Y[0] < y < MOLE_Y[1]:
                        new_round(screen)

            pygame.display.flip()

            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
