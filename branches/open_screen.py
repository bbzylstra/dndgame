__author__ = 'Brad'
import ctypes
import pygame,sys,os
import ctypes
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
    img=img.convert_alpha()
    bgcolor = 0, 0, 0
    if game == True:
        while True:
            x=[0]
            y=[0]
            event = pygame.event.poll()
            screen.fill((bgcolor))
            size=10
            for i in range(0,size):
                y.append((screensize[1]/size)+y[i])
                x.append((screensize[0]/size)+x[i])
            img=pygame.transform.scale(img,(x[1],y[1]))
            for i in x:
                for z in y:
                    screen.blit(img,(i,z))
            for i in range(0,size+1):
                if i==size:
                    pygame.draw.line(screen,(0,0,255),(x[i]-1,0),(x[i]-1,screensize[1]),1)
                    pygame.draw.line(screen,(0,0,255),(0,y[i]-1),(screensize[0],y[i]-1),1)
                else:
                    pygame.draw.line(screen,(0,0,255),(x[i],0),(x[i],screensize[1]),1)
                    pygame.draw.line(screen,(0,0,255),(0,y[i]),(screensize[0],y[i]),1)

            pygame.display.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
    return None
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
    drawScreen(game)
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