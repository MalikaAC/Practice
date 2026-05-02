import pygame
import random
from config import *

class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(WIDTH // 2, HEIGHT // 2)]
        self.direction = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        self.color = (0,255,0)
        self.shield = False

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        self.direction = point

    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = ((cur[0]+x*CELL_SIZE)%WIDTH,(cur[1]+y*CELL_SIZE)%HEIGHT)

        if len(self.positions) > 2 and new in self.positions[2:]:
            if self.shield:
                self.shield = False
            else:
                raise Exception("Collision")

        self.positions.insert(0,new)
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface,self.color,(*p,CELL_SIZE,CELL_SIZE))

    def check_collision(self):
        head = self.get_head_position()
        return head in self.positions[1:]


class Food:
    def __init__(self,w,h,c,snake):
        self.value=random.choice([1,2,3])
        while True:
            self.position=(random.randint(0,w//c-1)*c,random.randint(0,h//c-1)*c)
            if self.position not in snake:
                break

    def draw(self,s):
        pygame.draw.rect(s,(255,255,0),(*self.position,CELL_SIZE,CELL_SIZE))


class PoisonFood:
    def __init__(self,w,h,c,snake):
        while True:
            self.position=(random.randint(0,w//c-1)*c,random.randint(0,h//c-1)*c)
            if self.position not in snake:
                break

    def draw(self,s):
        pygame.draw.rect(s,(200,0,0),(*self.position,CELL_SIZE,CELL_SIZE))


class PowerUp:
    def __init__(self,w,h,c,snake):
        self.type=random.choice(["speed","slow","shield"])
        self.spawn_time=pygame.time.get_ticks()

        while True:
            self.position=(random.randint(0,w//c-1)*c,random.randint(0,h//c-1)*c)
            if self.position not in snake:
                break

    def draw(self,s):
        color=(0,255,255) if self.type=="speed" else (0,0,255) if self.type=="slow" else (255,0,255)
        pygame.draw.rect(s,color,(*self.position,CELL_SIZE,CELL_SIZE))


class Obstacle:
    def __init__(self, snake):
        while True:
            self.position=(random.randint(0,WIDTH//CELL_SIZE-1)*CELL_SIZE,
                           random.randint(0,HEIGHT//CELL_SIZE-1)*CELL_SIZE)
            if self.position not in snake:
                break

    def draw(self,s):
        pygame.draw.rect(s,(100,100,100),(*self.position,CELL_SIZE,CELL_SIZE))