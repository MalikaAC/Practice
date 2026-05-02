import pygame, json, random
from config import *
from db import create_tables, get_top
from game import run_game

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


def input_name(screen):
    font = pygame.font.SysFont(None,40)
    name=""

    while True:
        screen.fill((0,0,0))
        text=font.render("Enter name: "+name,1,(255,255,255))
        screen.blit(text,(100,200))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                return None
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_RETURN:
                    return name
                elif e.key==pygame.K_BACKSPACE:
                    name=name[:-1]
                else:
                    name+=e.unicode

        pygame.display.flip()


def settings_screen(screen):
    font=pygame.font.SysFont(None,40)

    try:
        with open("settings.json") as f:
            settings=json.load(f)
    except:
        settings={"color":"green","sound":True,"grid":False}

    while True:
        screen.fill((0,0,0))

        screen.blit(font.render(f"Color: {settings['color']}",1,(255,255,255)),(100,100))
        screen.blit(font.render(f"Sound: {settings['sound']}",1,(255,255,255)),(100,150))
        screen.blit(font.render("C-change S-sound G-grid",1,(255,255,0)),(100,200))
        screen.blit(font.render("ESC-save",1,(255,255,255)),(100,250))

        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                return
            if e.type==pygame.KEYDOWN:
                if e.key==pygame.K_c:
                    settings["color"]=random.choice(["green","red","blue"])
                if e.key==pygame.K_s:
                    settings["sound"]=not settings["sound"]
                if e.key==pygame.K_g:
                    settings["grid"]=not settings["grid"]
                if e.key==pygame.K_ESCAPE:
                    with open("settings.json","w") as f:
                        json.dump(settings,f)
                    return

        pygame.display.flip()


def main():
    create_tables()

    while True:
        name=input_name(screen)
        if not name: return

        run_game(screen,name)
        settings_screen(screen)


main()