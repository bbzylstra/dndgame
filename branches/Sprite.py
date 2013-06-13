__author__ = 'Brad'
import pygame,drawScreen,drawToScreen
class Ai_Sprite(pygame.sprite.Sprite):
    def __init__(self,imgpath,cellnumbers,xlist,ylist,screen,squareNumber,cellnumbers2d):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.squareNumber=squareNumber
        self.cellnumbers=cellnumbers
        self.cellnumbers2d=cellnumbers2d
        self.image=pygame.image.load(imgpath).convert()
        self.rect=self.image.get_rect()
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber,self.cellnumbers)
    def moveSprite(self,newcellNumber):
        drawToScreen.drawToScreen(self.image,self.screen,newcellNumber,self.cellnumbers)


