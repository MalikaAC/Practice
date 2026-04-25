import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Mickey clock")
clock = pygame.time.Clock()
mainclock = pygame.image.load('images/mainclock.png').convert_alpha()
right_arm = pygame.image.load('images/rightarm.png').convert_alpha()
left_arm = pygame.image.load('images/leftarm.png').convert_alpha()
font = pygame.font.SysFont(None, 100)
def blitRotate2(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    pos = (0, 0)
    now = datetime.datetime.now()
    hours = now.hour
    seconds = now.second
    minutes = now.minute
    seconds_ang = - (now.second * 6)
    minutes_ang = - (now.minute * 6)
    screen.blit(mainclock, (0, 0))
    blitRotate2(screen, left_arm, pos, minutes_ang)
    blitRotate2(screen, right_arm, pos, seconds_ang)
    text = font.render(f"{hours}:{minutes}:{seconds}", True, (0, 0, 0))
    screen.blit(text, (265, 600))
    pygame.display.flip()
    clock.tick(60)