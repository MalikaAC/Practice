import pygame
import sys
from datetime import datetime
from constants import *
from tools import (
    Brush,
    SquareTool,
    RightTriangleTool,
    EquilateralTriangleTool,
    RhombusTool
)

def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            continue

        if surface.get_at((x, y)) != target_color:
            continue

        surface.set_at((x, y), new_color)

        stack.append((x + 1, y))
        stack.append((x - 1, y))
        stack.append((x, y + 1))
        stack.append((x, y - 1))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Paint TSIS2")

    canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    canvas.fill(BLACK)

    clock = pygame.time.Clock()

    current_tool = Brush()
    current_color = BLUE
    width = 5

    drawing = False
    start_pos = None
    last_pos = None

    font = pygame.font.SysFont(None, 30)
    typing = False
    text = ""
    text_pos = (0, 0)

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if typing:
                    if event.key == pygame.K_RETURN:
                        img = font.render(text, True, current_color)
                        canvas.blit(img, text_pos)
                        typing = False
                        text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                    continue

                # цвета
                if event.key == pygame.K_r:
                    current_color = RED
                elif event.key == pygame.K_g:
                    current_color = GREEN
                elif event.key == pygame.K_b:
                    current_color = BLUE

                # размер кисти
                elif event.key == pygame.K_1:
                    width = 2
                elif event.key == pygame.K_2:
                    width = 5
                elif event.key == pygame.K_3:
                    width = 10

                # инструменты
                elif event.key == pygame.K_p:
                    current_tool = Brush()
                elif event.key == pygame.K_l:
                    current_tool = "line"
                elif event.key == pygame.K_f:
                    current_tool = "fill"
                elif event.key == pygame.K_t:
                    current_tool = "text"

                elif event.key == pygame.K_q:
                    current_tool = SquareTool()
                elif event.key == pygame.K_w:
                    current_tool = RightTriangleTool()
                elif event.key == pygame.K_e:
                    current_tool = EquilateralTriangleTool()
                elif event.key == pygame.K_4:
                    current_tool = RhombusTool()

                elif event.key == pygame.K_c:
                    canvas.fill(BLACK)

                # сохранение
                if event.key == pygame.K_s and (event.mod & pygame.KMOD_CTRL):
                    filename = f"paint_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    pygame.image.save(canvas, filename)
                    print("Saved:", filename)

                if event.key == pygame.K_ESCAPE:
                    return

            if event.type == pygame.MOUSEBUTTONDOWN:

                if current_tool == "fill":
                    flood_fill(canvas, *event.pos, current_color)
                    continue

                if current_tool == "text":
                    typing = True
                    text_pos = event.pos
                    text = ""
                    continue

                drawing = True
                start_pos = event.pos
                last_pos = event.pos

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    if current_tool == "line":
                        pygame.draw.line(canvas, current_color, start_pos, event.pos, width)
                    elif not isinstance(current_tool, Brush):
                        current_tool.draw(canvas, current_color, start_pos, event.pos, width)
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                if isinstance(current_tool, Brush):
                    pygame.draw.line(canvas, current_color, last_pos, event.pos, width)
                    last_pos = event.pos

        screen.fill(BLACK)
        screen.blit(canvas, (0, 0))

        if drawing:
            pos = pygame.mouse.get_pos()

            if current_tool == "line":
                pygame.draw.line(screen, current_color, start_pos, pos, width)
            elif not isinstance(current_tool, Brush):
                current_tool.draw(screen, current_color, start_pos, pos, width)

        if typing:
            img = font.render(text, True, current_color)
            screen.blit(img, text_pos)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()

"""
P — кисть
L — линия
F — заливка
T — текст
Q/W/E/4 — фигуры
1/2/3 — размер кисти
R/G/B — цвет
Ctrl + S — сохранить
C — очистить
"""