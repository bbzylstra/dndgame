__author__ = 'Brad'
import pygame,sys,os
pygame.init()
screen = pygame.display.set_mode((640, 400))
running =True
bgcolor = 0, 0, 0
LEFT=1
clock = pygame.time.Clock()
game_font = pygame.font.Font("freesansbold.ttf",15)
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
    game = game_font.render("GAME", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (299,47) )
    pygame.display.flip()
    clock.tick(120)