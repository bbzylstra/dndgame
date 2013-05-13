__author__ = 'Brad'
import pygame
screen = pygame.display.set_mode((640, 400))
running =True
linecolor = 255, 255, 255
x = y = 0
bgcolor = 0, 0, 0
LEFT=1
clock = pygame.time.Clock()
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=False
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False
    screen.fill((bgcolor))
    pygame.draw.rect(screen, (255, 0, 0), (169, 17, 300, 69),1)
    pygame.display.flip()
    clock.tick(120)