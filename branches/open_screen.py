__author__ = 'Brad'
import pygame,sys,os
pygame.init()
screen = pygame.display.set_mode((640, 400))
running =1
bgcolor = 0, 0, 0
LEFT=1
clock = pygame.time.Clock()
game_font = pygame.font.Font("freesansbold.ttf",15)
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = 0
    screen.fill((bgcolor))
    pygame.draw.rect(screen, (255, 0, 0), (169, 17, 300, 69),1)
    game = game_font.render("GAME", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (299,47) )
    pygame.draw.polygon(screen, (255, 0, 0), [(170, 114),(467,114), (467, 197),(170,197)],1)
    game = game_font.render("Character Creation", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (253,156) )
    pygame.draw.polygon(screen, (255, 0, 0), [(170, 220),(467, 220), (467, 270),(170, 270)],1)
    game = game_font.render("Exit", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (253,220) )
    pygame.display.flip()
    clock.tick(200)
pygame.quit()