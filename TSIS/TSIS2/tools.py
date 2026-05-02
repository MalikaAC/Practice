import pygame
import math

class Tool:
    """Базовый класс инструмента"""
    def draw(self, surface, color, start_pos, end_pos, width):
        pass


class Brush(Tool):
    """Кисть (рисует линии)"""
    def draw(self, surface, color, start_pos, end_pos, width):
        if start_pos:
            pygame.draw.line(surface, color, start_pos, end_pos, width)


# ---------- SQUARE ----------
class SquareTool(Tool):
    """Рисует квадрат"""
    def draw(self, surface, color, start_pos, end_pos, width):
        size = max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))

        x = start_pos[0]
        y = start_pos[1]

        # направление рисования
        if end_pos[0] < start_pos[0]:
            x -= size
        if end_pos[1] < start_pos[1]:
            y -= size

        pygame.draw.rect(surface, color, (x, y, size, size), 2)


# ---------- RIGHT TRIANGLE ----------
class RightTriangleTool(Tool):
    """Прямоугольный треугольник"""
    def draw(self, surface, color, start_pos, end_pos, width):
        x1, y1 = start_pos
        x2, y2 = end_pos

        points = [
            (x1, y1),
            (x2, y1),
            (x1, y2)
        ]

        pygame.draw.polygon(surface, color, points, 2)


# ---------- EQUILATERAL TRIANGLE ----------
class EquilateralTriangleTool(Tool):
    """Равносторонний треугольник"""
    def draw(self, surface, color, start_pos, end_pos, width):
        x1, y1 = start_pos
        side = abs(end_pos[0] - start_pos[0])

        height = int((math.sqrt(3) / 2) * side)

        points = [
            (x1, y1),
            (x1 + side, y1),
            (x1 + side // 2, y1 - height)
        ]

        pygame.draw.polygon(surface, color, points, 2)


# ---------- RHOMBUS ----------
class RhombusTool(Tool):
    """Ромб"""
    def draw(self, surface, color, start_pos, end_pos, width):
        cx = (start_pos[0] + end_pos[0]) // 2
        cy = (start_pos[1] + end_pos[1]) // 2

        dx = abs(start_pos[0] - end_pos[0]) // 2
        dy = abs(start_pos[1] - end_pos[1]) // 2

        points = [
            (cx, cy - dy),
            (cx + dx, cy),
            (cx, cy + dy),
            (cx - dx, cy)
        ]

        pygame.draw.polygon(surface, color, points, 2)