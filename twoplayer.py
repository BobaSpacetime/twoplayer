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
fire = pygame.mixer.Sound("Two Player/images/Grenade+1.mp3")
col = pygame.mixer.Sound("Two Player/images/Gun+Silencer.mp3")
font = pygame.font.SysFont("comicsansms", 17)
yelhealth = 5
redhealth = 5

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
yelbulls=[]
while True:
    clock.tick(fps)
    screen.blit(space, (0,0))
    text = font.render("Health = " + str(yelhealth), True, "#000000")
    text1 = font.render("Health = " + str(redhealth), True, "#000000")
    screen.blit(text, (550, 50))
    screen.blit(text, (50, 50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                fire.play()
                bullet = pygame.Rect(redrect.x + 50, redrect.y + 22.5, 5, 5)
                redbulls.append(bullet)
            if event.key == pygame.K_SLASH:
                fire.play()
                bullets = pygame.Rect(yelrect.x - 5, yelrect.y + 23, 5, 5)
                yelbulls.append(bullets)
    for bullet in redbulls:
        pygame.draw.rect(screen, "#FF1E00", bullet)
        bullet.x+=4
        if bullet.colliderect(yelrect):
            col.play()
            yelhealth-=1
            redbulls.remove(bullet)
    keys_pressed = pygame.key.get_pressed()
    for bullets in yelbulls:
        pygame.draw.rect(screen, "#FFC800", bullets)
        bullets.x-=4
        if bullet.colliderect(redrect):
            col.play()
            redhealth-=1
            yelbulls.remove(bullet)

    keys_pressed = pygame.key.get_pressed()
    redmove()
    yellowmove()
    screen.blit(red, redrect)
    screen.blit(yellow, yelrect)
    pygame.draw.rect(screen, "#000000", wall)
    pygame.display.update()