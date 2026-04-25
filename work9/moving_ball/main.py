import pygame
import sys
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moving Ball Game")
    clock = pygame.time.Clock()

    ball = Ball(x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball.move("UP", SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_DOWN:
                    ball.move("DOWN", SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_LEFT:
                    ball.move("LEFT", SCREEN_WIDTH, SCREEN_HEIGHT)
                elif event.key == pygame.K_RIGHT:
                    ball.move("RIGHT", SCREEN_WIDTH, SCREEN_HEIGHT)

        screen.fill(WHITE)
        ball.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)


if __name__ == "__main__":
    main()