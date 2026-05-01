import pygame
from entities import Snake, Food

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    font = pygame.font.SysFont("Verdana", 20)

    snake = Snake(WIDTH, HEIGHT, CELL_SIZE)
    food = Food(WIDTH, HEIGHT, CELL_SIZE, snake.positions)

    score = 0
    running = True

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake.direction != pygame.K_DOWN:
                    snake.direction = event.key
                elif event.key == pygame.K_DOWN and snake.direction != pygame.K_UP:
                    snake.direction = event.key
                elif event.key == pygame.K_LEFT and snake.direction != pygame.K_RIGHT:
                    snake.direction = event.key
                elif event.key == pygame.K_RIGHT and snake.direction != pygame.K_LEFT:
                    snake.direction = event.key

        if not snake.update():
            snake = Snake(WIDTH, HEIGHT, CELL_SIZE)
            food = Food(WIDTH, HEIGHT, CELL_SIZE, snake.positions)
            score = 0

        if food.is_expired():
            food = Food(WIDTH, HEIGHT, CELL_SIZE, snake.positions)

        if snake.get_head_position() == food.position:
            snake.length += 1
            score += food.value
            food = Food(WIDTH, HEIGHT, CELL_SIZE, snake.positions)

        snake.draw(screen)
        food.draw(screen)

        text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()