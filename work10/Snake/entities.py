import pygame
import random

class Snake:
    """
    Класс, представляющий змейку.
    Отвечает за движение, хранение координат тела и отрисовку.
    """
    def __init__(self, width, height, cell_size):
        """
        Инициализация змейки.
        
        :param width: Ширина игрового поля.
        :param height: Высота игрового поля.
        :param cell_size: Размер одной ячейки (сетки).
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.length = 1
        self.positions = [(width // 2, height // 2)]
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = (0, 255, 0)

    def get_head_position(self):
        """
        Возвращает текущие координаты головы змейки (первый элемент в списке positions).
        """
        return self.positions[0]

    def update(self):
        """
        Обновляет позицию змейки на основе текущего направления.
        Проверяет столкновения со стенами и собственным телом.
        
        :return: False, если произошло столкновение (конец игры), True в противном случае.
        """
        cur = self.get_head_position()
        x, y = cur
        if self.direction == pygame.K_UP:
            y -= self.cell_size
        elif self.direction == pygame.K_DOWN:
            y += self.cell_size
        elif self.direction == pygame.K_LEFT:
            x -= self.cell_size
        elif self.direction == pygame.K_RIGHT:
            x += self.cell_size

        new = (x, y)
        
        # Проверка столкновения: с телом (начиная со 2-го сегмента) или границами экрана
        if new in self.positions[2:] or x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        
        # Добавляем новую голову в начало списка
        self.positions.insert(0, new)
        # Если длина превышена (не съели еду), удаляем последний сегмент хвоста
        if len(self.positions) > self.length:
            self.positions.pop()
        return True

    def draw(self, surface):
        """
        Отрисовывает каждый сегмент змейки на заданной поверхности.
        
        :param surface: Поверхность Pygame для рисования.
        """
        for p in self.positions:
            rect = pygame.Rect((p[0], p[1]), (self.cell_size, self.cell_size))
            pygame.draw.rect(surface, self.color, rect)

class Food:
    """
    Класс, представляющий еду на игровом поле.
    Появляется в случайном месте, выровненном по сетке.
    """
    def __init__(self, width, height, cell_size):
        """
        Инициализация объекта еды.
        
        :param width: Ширина поля.
        :param height: Высота поля.
        :param cell_size: Размер ячейки.
        """
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.position = (0, 0)
        self.color = (213, 50, 80)
        self.randomize_position()

    def randomize_position(self):
        """
        Генерирует новые случайные координаты для еды, кратные размеру ячейки.
        """
        self.position = (random.randint(0, (self.width // self.cell_size) - 1) * self.cell_size,
                         random.randint(0, (self.height // self.cell_size) - 1) * self.cell_size)

    def draw(self, surface):
        """
        Отрисовывает еду на экране в виде цветного квадрата.
        
        :param surface: Поверхность Pygame для рисования.
        """
        rect = pygame.Rect((self.position[0], self.position[1]), (self.cell_size, self.cell_size))
        pygame.draw.rect(surface, self.color, rect)