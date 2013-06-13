__author__ = 'Brad'
def drawToScreen(img,screen,squareNumber2d,cellnumbers2d):
    import pygame
    img=pygame.transform.scale(img,(int(cellnumbers2d[1,1][0])-21,int(cellnumbers2d[1,1][1])-21))
    if squareNumber2d == (-1,-1):
        None
    else:
        xDraw,yDraw=cellnumbers2d[squareNumber2d][0],cellnumbers2d[squareNumber2d][1]
        screen.blit(img,(xDraw+1,yDraw+1))
    return None


