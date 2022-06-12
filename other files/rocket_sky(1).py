import pygame
pygame.init()


win = pygame.display.set_mode((1123, 800))
pygame.display.set_caption("Rocket sky ***")

#bg = pygame.image.load('rocket_sky_img_base(1).jfif')
char = pygame.image.load('rocket_sky_img_rocket(1).jfif')


def redrawgamewindow():
    #win.blit(bg, (0, 0))
    win.blit(char, (x, y))
    pygame.display.update()


x = 500
y = 600
width = 123
height = 176
vel_up = 50
vel_down = 25

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        y -= vel_up
        if y == 0:
            y = 800
    else:
        y += vel_down
        if y == 800:
            run = False
    win.fill((0, 0, 0))
    redrawgamewindow()

pygame.quit()
