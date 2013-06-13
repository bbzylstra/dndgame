__author__ = 'Brad'
def drawToScreen(img,screen,squareNumber,squareDict):
    import pygame
    img=pygame.transform.scale(img,(int(squareDict[19][0])-21,int(squareDict[19][1])-21))
    if squareNumber == -1:
        None
    else:
        xDraw,yDraw=squareDict[squareNumber][0],squareDict[squareNumber][1]
        screen.blit(img,(xDraw+1,yDraw+1))
    return None


