import pygame
pygame.init()
WIDTH = 650
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("#1008216C")

space = pygame.image.load("Two Player/images/space.png")
red = pygame.image.load("Two Player/images/spaceship_red.png")
red = pygame.transform.scale(red,(50,50))
red = pygame.transform.rotate(red, 90)
yellow = pygame.image.load("Two Player/images/spaceship_yellow.png")
yellow = pygame.transform.scale(yellow, (50,50))
yellow = pygame.transform.rotate(yellow, -90)
wall = pygame.Rect(325,0,10,450)
redrect = pygame.Rect(100,225,50,50)

def redmove():
    if keys_pressed[pygame.K_w]:
        redrect.y-=0.6

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    keys_pressed = pygame.key.get_pressed()
    redmove()
    screen.blit(space, (0,0))
    screen.blit(red, redrect)
    screen.blit(yellow, (500,225))
    pygame.draw.rect(screen, "#000000", wall)
    pygame.display.update()