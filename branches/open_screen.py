__author__ = 'Brad'
import ctypes
import pygame,sys,os,drawScreen,detectSquare,drawToScreen,charactercreation,comtest
from decimal import Decimal
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
pygame.init()
screen=pygame.display.set_mode((screensize),pygame.FULLSCREEN)
running =1
bgcolor = 0, 0, 0
LEFT=1
clock = pygame.time.Clock()
game_font = pygame.font.Font("freesansbold.ttf",16)
Game=False
cellNumber=0
current_path=os.getcwd()
sprite_path=current_path+'/sprites/'
textBox=pygame.Surface((500,50))
textBox=textBox.convert()
img3=pygame.image.load(sprite_path+'swordsman-on-tile.png')

game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))
while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running=0
    elif event.type == pygame.MOUSEMOTION:
        x, y = event.pos
    elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
        print "You released the left mouse button at (%d, %d)" % event.pos
        if (event.pos[0] >=screensize[0]*.4033 and event.pos[0] <=screensize[0]*.63) and (event.pos[1] >=screensize[1]*.02 and event.pos[1] <=screensize[1]*.16) :
            Game=True
        elif(event.pos[0] >=screensize[0]*.1244 and event.pos[0] <=screensize[0]*.63) and (event.pos[1] >=screensize[1]*.02 and event.pos[1] <=screensize[1]*.15625) :
            charactercreation.characterCreate(screen)
        elif (event.pos[0] >=screensize[0]*.0073 and event.pos[0] <=screensize[0]*.106149) and (event.pos[1] >=screensize[1]*.8905 and event.pos[1] <=screensize[1]*.990885) :
            running=0
        elif (event.pos[0] >=370 and event.pos[0] <=590) and (event.pos[1] >=330 and event.pos[1] <=380) :
            comtest.combatsim(screen)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = 0
    if Game==True:
        textBox.fill((0,0,0))
        screen.blit(textBox,(0,screensize[1]-50))
        pygame.display.update()
        while Game==True:
            x,y,cellNumbers=drawScreen.drawScreen(screen,screensize)
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game=False
                    break
            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                xi,yi=event.pos
                cellNumber=detectSquare.detectSquare(x,y,xi,yi,screensize)
                print("Cell Number: %d" % detectSquare.detectSquare(x,y,xi,yi,screensize))
                game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))
            drawToScreen.drawToScreen(x,y,img3,screen,cellNumber,cellNumbers)
            textBox.fill((0,0,0))
            screen.blit(textBox,(0,screensize[1]-50))
            textBox.blit(game1,(0,0))
            screen.blit(textBox,(0,screensize[1]-50))
            xi,yi=pygame.mouse.get_pos()
            game = game_font.render(str(xi)+' '+str(yi), True, (255,0, 0), (0, 0, 0))
            textBox.blit(game,(0,25))
            screen.blit(textBox,(0,screensize[1]-50))
            pygame.display.update()
    screen.fill((bgcolor))
    pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.4033,screensize[1]*.02),(screensize[0]*.63,screensize[1]*.02),(screensize[0]*.63,screensize[1]*.16),(screensize[0]*.4033,screensize[1]*.16)],1)
    game = game_font.render("Launch A Game", True, (255,0, 0), (0, 0, 0))
    screen.blit(game,(screensize[0]*.46658,screensize[1]*.0799))
    pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.1244,screensize[1]*.02),(screensize[0]*.35139,screensize[1]*.02),(screensize[0]*.35139,screensize[1]*.15625),(screensize[0]*.1244,screensize[1]*.15625)],1)
    game = game_font.render("Create A New Character", True, (255,0, 0), (0, 0, 0))
    screen.blit(game,(screensize[0]*.16065,screensize[1]*.0799))
    pygame.draw.polygon(screen, (255, 0, 0), [(370, 380),(370,330), (590, 330),(590,380)],1)
    game = game_font.render("1v1 Combat Simulator", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (375,350) )
    pygame.draw.polygon(screen, (255, 0, 0), [(screensize[0]*.0073,screensize[1]*0.9375),(screensize[0]*.106149,screensize[1]*0.9375), (screensize[0]*.106149,screensize[1]*.990885),(screensize[0]*.0073,screensize[1]*.990885)],1)
    game = game_font.render("Exit", True, (255,0, 0), (0, 0, 0))
    screen.blit(game, (screensize[0]*.034407,screensize[1]*0.96484375))
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
