import pygame


class Ball:
    def __init__(self, x, y, radius=25, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.step = 20

    def move(self, direction, screen_width, screen_height):
        new_x = self.x
        new_y = self.y

        if direction == "UP":
            new_y -= self.step
        elif direction == "DOWN":
            new_y += self.step
        elif direction == "LEFT":
            new_x -= self.step
        elif direction == "RIGHT":
            new_x += self.step

        if (self.radius <= new_x <= screen_width - self.radius and
                self.radius <= new_y <= screen_height - self.radius):
            self.x = new_x
            self.y = new_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)