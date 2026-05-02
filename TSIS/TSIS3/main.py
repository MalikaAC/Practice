import pygame, sys, random, json, os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TSIS Racer")
clock = pygame.time.Clock()

BASE_DIR = os.path.dirname(__file__)

def path(folder, name):
    return os.path.join(BASE_DIR, folder, name)

background = pygame.image.load(path("images","AnimatedStreet.png"))
player_img = pygame.image.load(path("images","Player.png"))
enemy_img = pygame.image.load(path("images","Enemy.png"))

# ---------- SETTINGS ----------
def load_settings():
    try:
        with open(path("", "settings.json")) as f:
            return json.load(f)
    except:
        return {"sound": True, "difficulty": 5, "color": "blue"}  # ДОБАВЛЕНО color

def save_settings(s):
    with open(path("", "settings.json"), "w") as f:
        json.dump(s, f, indent=4)

settings = load_settings()

# ---------- SOUND ----------
def play_music():
    if settings["sound"]:
        pygame.mixer.music.load(path("sounds","background.wav"))
        pygame.mixer.music.play(-1)

def stop_music():
    pygame.mixer.music.stop()

crash_sound = pygame.mixer.Sound(path("sounds","crash.wav"))

# ---------- LEADERBOARD ----------
def save_score(name, score):
    file = path("", "leaderboard.json")
    try:
        with open(file) as f:
            data = json.load(f)
    except:
        data = []

    data.append({"name": name, "score": score})
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def load_scores():
    try:
        with open(path("", "leaderboard.json")) as f:
            return json.load(f)
    except:
        return []

# ---------- SPRITES ----------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # ДОБАВЛЕНО: копия и смена цвета
        self.image = player_img.copy()

        if settings.get("color") == "red":
            self.image.fill((255,0,0), special_flags=pygame.BLEND_MULT)
        elif settings.get("color") == "green":
            self.image.fill((0,255,0), special_flags=pygame.BLEND_MULT)
        # blue — стандарт

        self.rect = self.image.get_rect(center=(WIDTH//2, HEIGHT-80))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += 5

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.y = -60
        self.rect.x = random.randint(40, WIDTH-40)

    def move(self, speed):
        self.rect.y += speed
        if self.rect.top > HEIGHT:
            self.reset()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["nitro","shield","repair"])
        self.image = pygame.Surface((20,20))

        if self.type=="nitro": self.image.fill(BLUE)
        if self.type=="shield": self.image.fill(GREEN)
        if self.type=="repair": self.image.fill(RED)

        self.rect = self.image.get_rect(center=(random.randint(40,WIDTH-40), -20))

    def move(self):
        self.rect.y += 4
        if self.rect.top > HEIGHT:
            self.kill()

# ---------- NEW: OBSTACLE ----------
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30,30))
        self.image.fill((120,120,120))
        self.rect = self.image.get_rect(center=(random.randint(40, WIDTH-40), -20))

    def move(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.kill()

# ---------- TEXT ----------
font = pygame.font.SysFont("Verdana", 20)
big = pygame.font.SysFont("Verdana", 40)

def draw(text, x, y, f=font):
    screen.blit(f.render(text, True, BLACK), (x,y))

# ---------- NAME INPUT ----------
def get_name():
    name=""
    while True:
        screen.fill(WHITE)
        draw("Enter name:", 100,200, big)
        draw(name, 120,260, big)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN and name!="":
                    return name
                elif e.key==pygame.K_BACKSPACE:
                    name=name[:-1]
                else:
                    name+=e.unicode

# ---------- SCREENS ----------
def menu():
    while True:
        screen.fill(WHITE)
        draw("PLAY (1)",140,200)
        draw("LEADERBOARD (2)",100,240)
        draw("SETTINGS (3)",120,280)
        draw("QUIT (0)",140,320)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_1: return "play"
                if e.key==pygame.K_2: return "leader"
                if e.key==pygame.K_3: return "settings"
                if e.key==pygame.K_0: sys.exit()

def leaderboard_screen():
    data = load_scores()
    while True:
        screen.fill(WHITE)
        draw("TOP 10",140,60,big)

        y=120
        for d in data:
            draw(f"{d['name']} - {d['score']}",100,y)
            y+=30

        draw("ESC - back",120,500)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: sys.exit()
            if e.type==pygame.KEYDOWN and e.key==pygame.K_ESCAPE:
                return

def settings_screen():
    while True:
        screen.fill(WHITE)
        draw(f"Sound: {settings['sound']} (S)",100,200)
        draw(f"Difficulty: {settings['difficulty']} (+/-)",100,240)

        # ДОБАВЛЕНО
        draw(f"Car Color: {settings.get('color','blue')} (C)",100,280)

        draw("ESC - back",100,320)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type==pygame.QUIT: sys.exit()
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_s:
                    settings["sound"]=not settings["sound"]
                if e.key==pygame.K_EQUALS:
                    settings["difficulty"]+=1
                if e.key==pygame.K_MINUS:
                    settings["difficulty"]-=1

                # ДОБАВЛЕНО смена цвета
                if e.key == pygame.K_c:
                    if settings.get("color") == "blue":
                        settings["color"] = "red"
                    elif settings.get("color") == "red":
                        settings["color"] = "green"
                    else:
                        settings["color"] = "blue"

                if e.key==pygame.K_ESCAPE:
                    save_settings(settings)
                    return

# ---------- GAME ----------
def game():
    player = Player()
    enemy = Enemy()

    all_sprites = pygame.sprite.Group(player, enemy)
    powers = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()

    distance = 0
    score = 0
    speed = settings["difficulty"]

    active = None
    timer = 0
    lives = 1

    name = get_name()
    game_over = False

    play_music()

    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: sys.exit()

            if game_over and e.type==pygame.KEYDOWN:
                if e.key==pygame.K_r:
                    save_score(name, score)
                    return

        if not game_over:
            distance += 1
            score = distance // 5

            if random.randint(1,100)==1:
                p=PowerUp()
                powers.add(p)
                all_sprites.add(p)

            if random.randint(1,120)==1:
                o = Obstacle()
                obstacles.add(o)
                all_sprites.add(o)

            player.move()
            enemy.move(speed)

            for p in powers:
                p.move()

            for o in obstacles:
                o.move()

            if player.rect.colliderect(enemy.rect):
                if active=="shield":
                    active=None
                    enemy.reset()
                elif lives>0:
                    lives-=1
                    enemy.reset()
                else:
                    stop_music()
                    crash_sound.play()
                    game_over=True

            if pygame.sprite.spritecollide(player, obstacles, True):
                if active=="shield":
                    active=None
                elif lives>0:
                    lives-=1
                else:
                    stop_music()
                    crash_sound.play()
                    game_over=True

            got = pygame.sprite.spritecollide(player, powers, True)
            for p in got:
                if p.type=="repair":
                    lives += 1
                else:
                    active=p.type
                    timer=pygame.time.get_ticks()

            if active=="nitro":
                speed=10
                if pygame.time.get_ticks()-timer>4000:
                    speed=settings["difficulty"]
                    active=None

        screen.blit(background,(0,0))

        for s in all_sprites:
            screen.blit(s.image,s.rect)

        draw(f"Score: {score}",10,10)
        draw(f"Distance: {distance}",10,40)
        draw(f"Lives: {lives}",10,70)

        if active:
            draw(f"Power: {active}",10,100)

        if game_over:
            draw("GAME OVER",120,250,big)
            draw("R - restart",120,320)

        pygame.display.update()
        clock.tick(FPS)

# ---------- MAIN ----------
while True:
    choice = menu()

    if choice=="play":
        game()
    elif choice=="leader":
        leaderboard_screen()
    elif choice=="settings":
        settings_screen()