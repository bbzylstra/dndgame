__author__ = 'Brad'
def drawToScreen(x,y,img,screen,squareNumber,squareDict):
    import pygame
    img=pygame.transform.scale(img,(int(x[1]-21),int(y[1]-21)))
    if squareNumber == -1:
        None
    else:
        xDraw,yDraw=squareDict[squareNumber][0],squareDict[squareNumber][1]
        screen.blit(img,(xDraw+1,yDraw+1))
    return None
