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
wall = pygame.Rect(320,0,10,450)
redrect = pygame.Rect(100,225,50,50)
yelrect = pygame.Rect(500,225,50,50)
fps = 60
clock = pygame.time.Clock()

def redmove():
    if keys_pressed[pygame.K_w]and redrect.y>0:
        redrect.y-=2
    if keys_pressed[pygame.K_s]and redrect.y<400:
        redrect.y+=2
    if keys_pressed[pygame.K_a]and redrect.x>0:
        redrect.x-=2
    if keys_pressed[pygame.K_d]and redrect.x<270:
        redrect.x+=2

def yellowmove():
    if keys_pressed[pygame.K_UP]and yelrect.y>0:
        yelrect.y-=2
    if keys_pressed[pygame.K_DOWN]and yelrect.y<400:
        yelrect.y+=2
    if keys_pressed[pygame.K_LEFT]and yelrect.x>330:
        yelrect.x-=2
    if keys_pressed[pygame.K_RIGHT]and yelrect.x<600:
        yelrect.x+=2

redbulls=[]
while True:
    clock.tick(fps)
    screen.blit(space, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                bullet = pygame.Rect(redrect.x, redrect.y,5, 5)
                redbulls.append(bullet)
    for bullets in redbulls:
        pygame.draw.rect(screen, "#65180E", bullets)
    keys_pressed = pygame.key.get_pressed()
    redmove()
    yellowmove()
    screen.blit(red, redrect)
    screen.blit(yellow, yelrect)
    pygame.draw.rect(screen, "#000000", wall)
    pygame.display.update()