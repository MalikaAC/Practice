import pygame, random, json, os
from config import *
from entities import *
from db import save_score, get_top

pygame.mixer.init()

BASE = os.path.dirname(__file__)
def snd(name): return os.path.join(BASE,"sounds",name)

def load_settings():
    try:
        with open("settings.json") as f:
            return json.load(f)
    except:
        return {"sound":True,"color":"green"}

def run_game(screen, username):
    settings = load_settings()

    coin = pygame.mixer.Sound(snd("coin.mp3"))
    crash = pygame.mixer.Sound(snd("crash.wav"))

    if settings.get("sound",True):
        pygame.mixer.music.load(snd("background.wav"))
        pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None,30)

    snake = Snake()
    if settings["color"]=="red": snake.color=(255,0,0)
    if settings["color"]=="blue": snake.color=(0,0,255)

    food = Food(WIDTH,HEIGHT,CELL_SIZE,snake.positions)
    poison=None
    power=None
    obstacles=[]

    score=0
    level=1
    foods=0
    speed=FPS

    active=None
    t0=0

    best=get_top(1)
    best_score = best[0][1] if best else 0

    while True:
        for e in pygame.event.get():
            if e.type==pygame.QUIT: return
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_UP: snake.turn((0,-1))
                if e.key==pygame.K_DOWN: snake.turn((0,1))
                if e.key==pygame.K_LEFT: snake.turn((-1,0))
                if e.key==pygame.K_RIGHT: snake.turn((1,0))

        snake.move()

        if snake.get_head_position()==food.position:
            snake.length+=1
            score+=food.value
            foods+=1

            if settings.get("sound"): coin.play()

            if foods%5==0:
                level+=1
                speed+=1
                if level>=3:
                    obstacles.append(Obstacle(snake.positions))

            food=Food(WIDTH,HEIGHT,CELL_SIZE,snake.positions)

        if poison and snake.get_head_position()==poison.position:
            snake.length-=2
            if snake.length<=1:
                break
            poison=None

        if not poison and random.randint(1,100)<3:
            poison=PoisonFood(WIDTH,HEIGHT,CELL_SIZE,snake.positions)

        if power and snake.get_head_position()==power.position:
            active=power.type
            t0=pygame.time.get_ticks()
            if power.type=="shield":
                snake.shield=True
            power=None

        if not power and random.randint(1,100)<2:
            power=PowerUp(WIDTH,HEIGHT,CELL_SIZE,snake.positions)

        if active:
            if pygame.time.get_ticks()-t0>5000:
                active=None
                snake.shield=False
            if active=="speed": speed=FPS+level+5
            if active=="slow": speed=max(3,FPS-3)

        for obs in obstacles:
            if snake.get_head_position()==obs.position:
                if snake.shield:
                    snake.shield=False
                else:
                    break

        if snake.check_collision():
            break

        screen.fill((0,0,0))
        snake.draw(screen)
        food.draw(screen)
        if poison: poison.draw(screen)
        if power: power.draw(screen)
        for o in obstacles: o.draw(screen)

        screen.blit(font.render(f"Score:{score}",1,(255,255,255)),(10,10))
        screen.blit(font.render(f"Level:{level}",1,(255,255,255)),(10,40))
        screen.blit(font.render(f"Best:{best_score}",1,(255,255,255)),(10,70))

        pygame.display.flip()
        clock.tick(speed)

    if settings.get("sound"):
        crash.play()
        pygame.mixer.music.stop()

    save_score(username,score,level)