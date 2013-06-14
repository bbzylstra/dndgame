__author__ = 'Brad'
import pygame,drawScreen,drawToScreen
class Ai_Sprite(pygame.sprite.Sprite):
    def __init__(self,imgpath,cellnumbers,x,y,screen,cellnumbers2d):
        self.movedistance=5
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.squareNumber2d=(x,y)
        self.cellnumbers=cellnumbers
        self.cellnumbers2d=cellnumbers2d
        self.image=pygame.image.load(imgpath).convert()
        self.rect=self.image.get_rect()
        self.moveSurf=pygame.Surface((500,50))
        self.moveSurf.fill((0,0,255))
        self.moveSurf=pygame.transform.scale(self.moveSurf,(int(self.cellnumbers2d[1,1][0])-21,int(self.cellnumbers2d[1,1][1])-21))
        self.selected=False
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)
    def moveSprite(self,newcellNumber2d):
        if self.selected==True and newcellNumber2d in self.movecells:
            self.squareNumber2d=newcellNumber2d
        self.selected=False
    def select(self):
        self.movecells=[]
        for i in range (0,self.movedistance+1):
            for z in range (0,self.movedistance+1):
                if self.movedistance-(z+i) <0:
                    pass
                else:
                    ydist=self.movedistance-(z+i)
                drawToScreen.drawToScreen(self.moveSurf,self.screen,(self.squareNumber2d[0]+i,self.squareNumber2d[1]+ydist),self.cellnumbers2d)
                drawToScreen.drawToScreen(self.moveSurf,self.screen,(self.squareNumber2d[0]-ydist,self.squareNumber2d[1]-z),self.cellnumbers2d)
                drawToScreen.drawToScreen(self.moveSurf,self.screen,(self.squareNumber2d[0]-i,self.squareNumber2d[1]+ydist),self.cellnumbers2d)
                drawToScreen.drawToScreen(self.moveSurf,self.screen,(self.squareNumber2d[0]+ydist,self.squareNumber2d[1]-z),self.cellnumbers2d)
                self.movecells.append((self.squareNumber2d[0]+i,self.squareNumber2d[1]+ydist))
                self.movecells.append((self.squareNumber2d[0]-ydist,self.squareNumber2d[1]-z))
                self.movecells.append((self.squareNumber2d[0]-i,self.squareNumber2d[1]+ydist))
                self.movecells.append((self.squareNumber2d[0]+ydist,self.squareNumber2d[1]-z))

    def update(self):
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)


