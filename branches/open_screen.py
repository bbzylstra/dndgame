__author__ = 'Brad'
import ctypes
import pygame,sys,os,drawScreen,detectSquare
from decimal import Decimal
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()
screen=pygame.display.set_mode((screensize),pygame.FULLSCREEN)
running =1
bgcolor = 0, 0, 0
LEFT=1
clock = pygame.time.Clock()
game_font = pygame.font.Font("freesansbold.ttf",15)
Game=False
cellNumber=-1
textBox=pygame.Surface(screen.get_size())
textBox=textBox.convert()
game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos
        if (event.pos[0] >=170 and event.pos[0] <=467) and (event.pos[1] >=30 and event.pos[1] <=100) :
            Game=True
        elif(event.pos[0] >=170 and event.pos[0] <=467) and (event.pos[1] >=114 and event.pos[1] <=197) :
            path=os.getcwd()
            os.startfile(path+'\charactercreation.py')
        elif (event.pos[0] >=5 and event.pos[0] <=150) and (event.pos[1] >=330 and event.pos[1] <=380) :
            running=0
        elif (event.pos[0] >=370 and event.pos[0] <=590) and (event.pos[1] >=330 and event.pos[1] <=380) :
            path=os.getcwd()
            os.startfile(path+'\comtest.py')
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = 0
    if Game==True:
        while Game==True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game=False
                    break
            x,y=drawScreen.drawScreen(screen,screensize)
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                xi,yi=event.pos
                cellNumber=detectSquare.detectSquare(x,y,xi,yi,screensize)
                print("Cell Number: %d" % detectSquare.detectSquare(x,y,xi,yi,screensize))
                game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))
            screen.blit(game1,(0,screensize[1]-50))
            pygame.display.update()
            xi,yi=pygame.mouse.get_pos()
            game = game_font.render(str(xi)+' '+str(yi), True, (255,0, 0), (0, 0, 0))
            screen.blit(game,(0,screensize[1]-30))
            pygame.display.update()
    screen.fill((bgcolor))
    pygame.draw.polygon(screen, (255, 0, 0), [(170, 30),(467,30), (467, 100),(170,100)],1)
    game = game_font.render("Game", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (253,50) )
    pygame.draw.polygon(screen, (255, 0, 0), [(170, 114),(467,114), (467, 197),(170,197)],1)
    game = game_font.render("Character Creation", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (253,156) )
    pygame.draw.polygon(screen, (255, 0, 0), [(370, 380),(370,330), (590, 330),(590,380)],1)
    game = game_font.render("1v1 Combat Simulator", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (375,350) )
    pygame.draw.polygon(screen, (255, 0, 0), [(10, 380),(150, 380), (150, 330),(10, 330)],1)
    game = game_font.render("Exit", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (50,350) )
    pygame.display.flip()
    clock.tick(30)
pygame.quit()