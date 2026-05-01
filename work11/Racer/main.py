import pygame, sys, random

pygame.init()
pygame.mixer.init()

# ---------- SETTINGS ----------
WIDTH, HEIGHT = 400, 600
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,215,0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")
clock = pygame.time.Clock()

# ---------- LOAD ----------
background = pygame.image.load("images/AnimatedStreet.png")
player_img = pygame.image.load("images/Player.png")
enemy_img = pygame.image.load("images/Enemy.png")

# яркая монета (чтобы точно видеть)
coin_img = pygame.Surface((30,30))
coin_img.fill(YELLOW)

# ---------- SOUND ----------
crash_sound = pygame.mixer.Sound("sounds/crash.wav")
coin_sound = pygame.mixer.Sound("sounds/coin.mp3")

pygame.mixer.music.load("sounds/background.wav")
pygame.mixer.music.play(-1)

# ---------- VARIABLES ----------
SCORE = 0
coins_collected = 0
enemy_speed = 5
N = 5
game_over = False

font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 40)

# ---------- PLAYER ----------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, HEIGHT-80)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

# ---------- ENEMY ----------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH//2, -60)

    def move(self):
        global SCORE
        self.rect.y += enemy_speed

        if self.rect.top > HEIGHT:
            self.rect.y = -60
            self.rect.x = random.randint(40, WIDTH-40)
            SCORE += 1

# ---------- COIN ----------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), -20)
        self.value = random.choice([1,2,3])

    def move(self):
        self.rect.y += 3
        if self.rect.top > HEIGHT:
            self.kill()

# ---------- OBJECTS ----------
player = Player()
enemy = Enemy()

coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group(player, enemy)

# стартовые монеты
for _ in range(3):
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

last_coin_time = pygame.time.get_ticks()

# ---------- GAME LOOP ----------
while True:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        # спавн монет
        if current_time - last_coin_time > 800:
            coin = Coin()
            coins.add(coin)
            all_sprites.add(coin)
            last_coin_time = current_time

        player.move()
        enemy.move()

        for coin in coins:
            coin.move()

        # ❗ КОЛЛИЗИЯ (БЕЗ ВЫХОДА)
        if player.rect.colliderect(enemy.rect):
            pygame.mixer.music.stop()
            crash_sound.play()
            game_over = True   # ← главное: НЕ закрываем игру

        # сбор монет
        collected = pygame.sprite.spritecollide(player, coins, True)
        for coin in collected:
            coin_sound.play()
            coins_collected += 1
            SCORE += coin.value

            if coins_collected % N == 0:
                enemy_speed += 1

    # ---------- DRAW ----------
    screen.blit(background, (0,0))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    score_text = font_small.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(score_text, (10,10))

    # ❗ GAME OVER экран (игра НЕ закрывается)
    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(RED)
        screen.blit(overlay, (0,0))

        text = font_big.render("GAME OVER", True, BLACK)
        screen.blit(text, (60, HEIGHT//2))

    pygame.display.update()
    clock.tick(FPS)