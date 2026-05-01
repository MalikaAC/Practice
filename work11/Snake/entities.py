import pygame
import random
import time

class Snake:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.length = 1
        self.positions = [(width // 2, height // 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = (0, 255, 0)

    def get_head_position(self):
        return self.positions[0]

    def update(self):
        x, y = self.get_head_position()

        if self.direction == pygame.K_UP:
            y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            x += self.cell_size

        new = (x, y)

        if new in self.positions[2:] or x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False

        self.positions.insert(0, new)

        if len(self.positions) > self.length:
            self.positions.pop()

        return True

    def draw(self, surface):
        for p in self.positions:
            rect = pygame.Rect(p[0], p[1], self.cell_size, self.cell_size)
            pygame.draw.rect(surface, self.color, rect)


class Food:
    def __init__(self, width, height, cell_size, snake_positions):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.value = random.choice([1, 2, 3])

        if self.value == 1:
            self.color = (0, 255, 0)
        elif self.value == 2:
            self.color = (255, 165, 0)
        else:
            self.color = (255, 0, 0)

        self.spawn_time = time.time()
        self.lifetime = 5

        self.position = (0, 0)
        self.randomize_position(snake_positions)

    def randomize_position(self, snake_positions):
        while True:
            pos = (
                random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size,
                random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size
            )
            if pos not in snake_positions:
                self.position = pos
                break

    def is_expired(self):
        return time.time() - self.spawn_time > self.lifetime

    def draw(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], self.cell_size, self.cell_size)
        pygame.draw.rect(surface, self.color, rect)