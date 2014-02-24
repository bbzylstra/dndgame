__author__ = 'Brad'
def drawScreen(screen,screensize):
    import pygame,os
    current_path=os.getcwd()
    sprite_path=current_path+"\sprites/"
    img=pygame.image.load(sprite_path+'tile50x50.png')
    bgcolor = 0, 0, 0
    borderOffset=20
    x=[borderOffset]
    y=[borderOffset]
    screen.fill((bgcolor))
    sizex=18
    sizey=12
    color = 0,255,0
    cellNumbers={}
    cellNumbers2d={}
    maxX=int(screensize[0]-screensize[0]/5)-borderOffset
    maxY=int(screensize[1]-screensize[1]/5)-borderOffset
    for i in range(0,sizey):
        y.append(float(maxY/sizey)+y[i])
    for i in range(0,sizex):
        x.append(float((maxX)/(sizex))+x[i])
    img=pygame.transform.scale(img,(int(x[1]-borderOffset),int(y[1]-borderOffset)))
    for c,i in enumerate(y):
        for f,z in enumerate(x):
            if (not f+1==len(x)) and (not c+1==len(y)):
                screen.blit(img,(z,i))
                cellNumbers[(len(x)-1)*c+f]=(z,i)
    for i in range(0,sizex+1):
        pygame.draw.line(screen,color,(x[i],borderOffset),(x[i],y[sizey]),1)
    for i in range(0,sizey+1):
        pygame.draw.line(screen,color,(borderOffset,y[i]),(x[sizex],y[i]),1)
    for c,i in enumerate(y):
        for f,z in enumerate(x):
            cellNumbers2d[f,c]=(z,i)
    game_font = pygame.font.Font("freesansbold.ttf",16)
    pygame.draw.polygon(screen,color,[(screensize[0]/1.2,screensize[1]/1.1),(screensize[0]-1,screensize[1]/1.1),(screensize[0]-1,screensize[1]-1),(screensize[0]/1.2,screensize[1]-1)],1)
    game1 = game_font.render("End Turn ", True, (255,0, 0), (0, 0, 0))
    screen.blit(game1,((screensize[0]/1.127,screensize[1]/1.05)))
    return x,y,cellNumbers,cellNumbers2d
#x is a list of the left most borders for each square
#y is a list of the top borders for each square.
#cellNumbers is a dict of the top left points for each square number
#cellNumbers2d is a 2d dict of the squares with the x,y coord for top left point
