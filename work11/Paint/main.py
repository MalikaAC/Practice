import pygame
import sys
from constants import *
from tools import (
    Brush,
    SquareTool,
    RightTriangleTool,
    EquilateralTriangleTool,
    RhombusTool
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint Shapes")

    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.fill(BLACK)

    clock = pygame.time.Clock()

    current_tool = Brush()
    current_color = BLUE
    width = 5

    drawing = False
    start_pos = None
    last_pos = None

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # ---------- КЛАВИШИ ----------
            if event.type == pygame.KEYDOWN:

                # цвета
                if event.key == pygame.K_r: current_color = RED
                elif event.key == pygame.K_g: current_color = GREEN
                elif event.key == pygame.K_b: current_color = BLUE

                # инструменты
                elif event.key == pygame.K_p:
                    current_tool = Brush()

                elif event.key == pygame.K_1:
                    current_tool = SquareTool()

                elif event.key == pygame.K_2:
                    current_tool = RightTriangleTool()

                elif event.key == pygame.K_3:
                    current_tool = EquilateralTriangleTool()

                elif event.key == pygame.K_4:
                    current_tool = RhombusTool()

                elif event.key == pygame.K_e:
                    current_tool = Brush()
                    current_color = BLACK  # ластик

                if event.key == pygame.K_ESCAPE:
                    return

            # ---------- МЫШЬ ----------
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                start_pos = event.pos
                last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing and not isinstance(current_tool, Brush):
                    current_tool.draw(canvas, current_color, start_pos, event.pos, width)

                drawing = False
                start_pos = None
                last_pos = None

            if event.type == pygame.MOUSEMOTION and drawing:
                if isinstance(current_tool, Brush):
                    current_tool.draw(canvas, current_color, last_pos, event.pos, width)
                    last_pos = event.pos

        # ---------- ОТРИСОВКА ----------
        screen.fill(BLACK)
        screen.blit(canvas, (0, 0))

        # preview фигур
        if drawing and not isinstance(current_tool, Brush):
            current_pos = pygame.mouse.get_pos()
            current_tool.draw(screen, current_color, start_pos, current_pos, width)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()