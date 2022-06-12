import pygame
pygame.init()


win = pygame.display.set_mode((1123, 800))
pygame.display.set_caption("Rocket sky ***")


class rocket(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.a1 = 0
        self.a2 = 0


bg = pygame.image.load('rocket_sky_img_flight(3).png')
bg_size = bg.get_size()
bg_rect = bg.get_rect()
screen = pygame.display.set_mode(bg_size)


shuttle = rocket(500, 400, 123, 176)
fuel = 2500
burn = 0
velo = 0
time = 0

char = pygame.image.load('rocket_sky_img_rocket(1).jfif')

theClock = pygame.time.Clock()

w, h = bg_size
y2 = 0
x1 = 0
y1 = -h


run = True


def vel(velo):
    font = pygame.font.SysFont('comicsans', 30, bold=True, italic=False)
    text = font.render('Velocity : ' + str(velo), 1, (255, 255, 255))
    win.blit(text, (100, 140))


def fuels(fuel):
    if fuel <= 0:
        font = pygame.font.SysFont(
            'comicsans', 30, bold=True, italic=False)
        text = font.render('Fuel Over !!!!!!!!!!!', 1, (255, 255, 255))
        win.blit(text, (500, 400))
        pygame.display.update()
        pygame.time.delay(700)
        pygame.quit()
    font = pygame.font.SysFont('comicsans', 30, bold=True, italic=False)
    text = font.render('Fuel : ' + str(fuel), 1, (255, 255, 255))
    win.blit(text, (100, 100))


def heatup(heat):
    if heat == 30:
        font = pygame.font.SysFont(
            'comicsans', 30, bold=True, italic=False)
        text = font.render('Overheated !!!!!!!!!!!', 1, (255, 255, 255))
        win.blit(text, (500, 400))
        pygame.display.update()
        pygame.time.delay(700)
        pygame.quit()
    font = pygame.font.SysFont('comicsans', 30, bold=True, italic=False)
    text = font.render('Heat : ' + str(heat), 1, (255, 255, 255))
    win.blit(text, (100, 120))


def scores(score):
    font = pygame.font.SysFont('comicsans', 30, bold=True, italic=False)
    text = font.render('Score : ' + str(score), 1, (255, 255, 255))
    win.blit(text, (100, 160))


while run:
    pygame.time.delay(10)
    screen.blit(bg, bg_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        shuttle.a1 += 2.5
        y1 += shuttle.a1**0.5
        y2 += shuttle.a1**0.5
        if y2 > h:
            y2 = -h
        if y1 > h:
            y1 = -h
        screen.blit(bg, (x1, y2))
        screen.blit(bg, (x1, y1))
        fuel -= (5 + shuttle.a1**0.01)
        burn += 0.1
        velo += shuttle.a1**0.5
        time += 0.2
        fuels(int(fuel))
        heatup(int(burn))
        vel(int(velo))
        scores(int(time))

    elif not(keys[pygame.K_SPACE]):
        shuttle.a2 += 1
        if burn <= 0:
            burn = 0
        else:
            burn -= 0.08
        if velo <= 0:
            velo = 0
        else:
            velo -= shuttle.a2**(0.5)
        if y1 == -h and y2 == 0:
            y1 = -h
            y2 = 0
        else:
            y1 += 75*shuttle.a2**(-0.5)
            y2 += 75*shuttle.a2**(-0.5)
        if y2 > h:
            y2 = -h
        if y1 > h:
            y1 = -h
        screen.blit(bg, (x1, y2))
        screen.blit(bg, (x1, y1))
        # if time == 0:
        #    time = 0
        # else:
        #    time += 0.2
        fuels(int(fuel))
        heatup(int(burn))
        vel(int(velo))
        scores(int(time))
    pygame.display.flip()
    theClock.tick(1000)
    win.blit(char, (shuttle.x, shuttle.y))
    pygame.display.update()


pygame.quit()
