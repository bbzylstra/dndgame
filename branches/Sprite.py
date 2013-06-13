__author__ = 'Brad'
import pygame,drawScreen,drawToScreen
class Ai_Sprite(pygame.sprite.Sprite):
    def __init__(self,imgpath,cellnumbers,x,y,screen,cellnumbers2d):
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.squareNumber2d=(x,y)
        self.cellnumbers=cellnumbers
        self.cellnumbers2d=cellnumbers2d
        self.image=pygame.image.load(imgpath).convert()
        self.rect=self.image.get_rect()
        self.selected=False
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)
    def moveSprite(self,newcellNumber2d):
        if self.selected==True:
            self.squareNumber2d=newcellNumber2d
        self.selected=False
    def update(self):
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)


