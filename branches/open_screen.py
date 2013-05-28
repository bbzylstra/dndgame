__author__ = 'Brad'
import ctypes
import pygame,sys,os
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
game=False
def drawScreen(game):
    img=pygame.image.load('tile50x50.png')
    bgcolor = 0, 0, 0
    if game == True:
            borderOffset=10
            x=[borderOffset]
            y=[borderOffset]
            screen.fill((bgcolor))
            sizex=18
            sizey=20
            color = 0,255,0
            maxX=int(screensize[0]-screensize[0]/10)-borderOffset
            maxY=int(screensize[1]-screensize[1]/10)-borderOffset
            for i in range(0,sizey):
                y.append(float(maxY/sizey)+y[i])
            for i in range(0,sizex):
                x.append(float((maxX)/(sizex))+x[i])
            #y[sizey],x[sizex]=x[sizex],y[sizey]
            img=pygame.transform.scale(img,(int(x[1]-borderOffset),int(y[1]-borderOffset)))
            for c,i in enumerate(y):
                for f,z in enumerate(x):
                    if (not f+1==len(x)) and (not c+1==len(y)):
                        screen.blit(img,(z,i))
            for i in range(0,sizex+1):
                pygame.draw.line(screen,color,(x[i],borderOffset),(x[i],y[sizey]),1)
            for i in range(0,sizey+1):
                pygame.draw.line(screen,color,(borderOffset,y[i]),(x[sizex],y[i]),1)
            pygame.display.update()
    return x,y
def detectSquare(x,y,xi,yi):
    cellNumber=-1
    for i,w in enumerate(y):
        for z,h in enumerate(x):
            if ((xi>(screensize[0]-screensize[0]/10)) or yi>(screensize[1]-screensize[1]/10)):
                cellNumber=(-1)
                return cellNumber
            else:
                if (xi>h and xi<x[z+1]) and (yi>w and yi<y[i+1]):
                    cellNumber=(len(x)-1)*i+z
    return cellNumber
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos
        if (event.pos[0] >=170 and event.pos[0] <=467) and (event.pos[1] >=30 and event.pos[1] <=100) :
            game=True
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
    if game==True:
        while game==True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
            x,y=drawScreen(game)
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                xi,yi=event.pos
                print("Cell Number: %d" % detectSquare(x,y,xi,yi))
            clock.tick(200)
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
    clock.tick(200)

pygame.quit()