__author__ = 'Brad'
import ctypes
import pygame,sys,os,drawScreen,detectSquare,drawToScreen,charactercreation,comtest,Sprite,spriteSelected
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
selectedSurf=pygame.Surface((500,50))
selectedSurf=selectedSurf.convert()
selectedSurf.fill((0,0,255))
swordsman=sprite_path+'swordsman-on-tile.png'
mage=sprite_path+'human-mage.png'
ranger=sprite_path+'human-ranger.png'
knight=sprite_path+'human-knight.png'
game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))
cellnumbers2d={}
cellNumber2d=(0,0)
spriteselected=''
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
        textBox.fill((0,0,0))
        game1 = game_font.render("Cell Number: " + str(cellNumber2d), True, (255,0, 0), (0, 0, 0))
        textBox.blit(game1,(0,0))
        screen.blit(textBox,(0,screensize[1]-50))
        x,y,cellNumbers,cellnumbers2d=drawScreen.drawScreen(screen,screensize)
        ai1= Sprite.Ai_Sprite(swordsman,cellNumbers,0,0,screen,cellnumbers2d)
        ai2= Sprite.Ai_Sprite(mage,cellNumbers,5,10,screen,cellnumbers2d)
        ai3= Sprite.Ai_Sprite(ranger,cellNumbers,10,5,screen,cellnumbers2d)
        ai4= Sprite.Ai_Sprite(knight,cellNumbers,5,5,screen,cellnumbers2d)
        ai_group=pygame.sprite.Group()
        ai_group.add(ai1,ai2,ai3,ai4)
        selectedSurf=pygame.transform.scale(selectedSurf,(int(cellnumbers2d[1,1][0])-21,int(cellnumbers2d[1,1][1])-21))

        while Game==True:
            drawScreen.drawScreen(screen,screensize)
            event = pygame.event.poll()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Game=False
                    break

            if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
                xi,yi=event.pos
                cellNumber,cellNumber2d=detectSquare.detectSquare(x,y,xi,yi,screensize)
                spriteselected=spriteSelected.spriteSelected(cellNumber2d,ai_group)
                if spriteselected != None:
                    if spriteselected.selected==True:
                        spriteselected=None

                if spriteselected != None:
                        spriteselected.selected=True

                for i in ai_group.sprites():
                    for z in ai_group.sprites():
                        if i.selected==True and z.selected==True and i != z:
                            i.selected=False
                            z.selected=False

                for v in ai_group.sprites():
                    if v.selected==True and spriteselected==None and cellNumber2d != [-1,-1]:
                        v.moveSprite(cellNumber2d)

                print("Cell Number: " + str(cellNumber2d))
                game1 = game_font.render("Cell Number: " + str(cellNumber2d), True, (255,0, 0), (0, 0, 0))


            for z in ai_group.sprites():
                if z.selected==True:
                    drawToScreen.drawToScreen(selectedSurf,screen,z.squareNumber2d,cellnumbers2d)
                    z.update()
                else:
                    z.update()

            textBox.fill((0,0,0))
            screen.blit(textBox,(0,screensize[1]-50))
            textBox.blit(game1,(0,0))
            screen.blit(textBox,(0,screensize[1]-50))
            xi,yi=pygame.mouse.get_pos()
            game = game_font.render(str(xi)+' '+str(yi), True, (255,0, 0), (0, 0, 0))
            textBox.blit(game,(0,25))
            screen.blit(textBox,(0,screensize[1]-50))
            pygame.display.update()
            clock.tick(100)

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
    clock.tick(100)
pygame.quit()
