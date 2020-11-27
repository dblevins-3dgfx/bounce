import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [100, 100]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

clock = pygame.time.Clock()

while 1:

    dt = clock.tick(30)/1000
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    vel = [dt*x for x in speed]
    ballrect = ballrect.move(vel)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
