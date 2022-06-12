import pygame
pygame.init()


win = pygame.display.set_mode((1123, 800))
pygame.display.set_caption("Rocket sky ***")

#bg = pygame.image.load('rocket_sky_img_base(1).jfif')
char = pygame.image.load('rocket_sky_img_rocket(1).jfif')

theClock = pygame.time.Clock()
background = pygame.image.load('rocket_sky_img_flight(3).png')
background_size = background.get_size()
background_rect = background.get_rect()
screen = pygame.display.set_mode(background_size)
w, h = background_size
x2 = 0
y2 = 0

x1 = 0
y1 = -h

x = 500
y = 400
width = 123
height = 176
a1 = 0
a2 = 0
vel = 0


run = True

while run:
    pygame.time.delay(100)
    screen.blit(background, background_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        a1 += 5
        y1 += 5 + a1**0.5
        y2 += 5 + a1**0.5
        screen.blit(background, (x2, y2))
        screen.blit(background, (x1, y1))
        if y2 > h:
            y2 = -h
        if y1 > h:
            y1 = -h
        vel += 5 + a1**0.5
    # elif not(keys[pygame.K_SPACE]):
     #   a1 += 5
      #  y1 += 5 - a1**0.5
       # y2 += 5 - a1**0.5
        #screen.blit(background, (x2, y2))
        #screen.blit(background, (x1, y1))
        # if y2 > h:
        #    y2 = -h
        # if y1 > h:
        #    y1 = -h
    pygame.display.flip()
    theClock.tick(100)
    win.blit(char, (x, y))
    pygame.display.update()


pygame.quit()
