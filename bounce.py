import sys, pygame

pygame.init()
pygame.font.init()
sysFont = pygame.font.SysFont("", 20)

size = width, height = 320, 240
speed = [200, 150]
black = 0, 0, 0
WHITE = [255, 255, 255]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

clock = pygame.time.Clock()

while 1:

    dt = clock.tick(120)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    vel = [dt*x for x in speed]
    ballrect = ballrect.move(vel)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    fpstext = str(int(1.0/dt))
    fpssurface = sysFont.render(fpstext, False, WHITE)
    fpsrect = fpssurface.get_rect()
    fpsrect.top = 1
    fpsrect.left = 1

    screen.fill(black)
    screen.blit(ball, ballrect)
    screen.blit(fpssurface, fpsrect)
    pygame.display.flip()
