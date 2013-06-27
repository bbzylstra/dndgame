__author__ = 'Brad'
import pygame,drawScreen,drawToScreen,os,ctypes,Astar,AstarHelper
class Ai_Sprite(pygame.sprite.Sprite):
    def __init__(self,imgpath,cellnumbers,screen,cellnumbers2d):
        dir= [name for name in os.listdir(".") if os.path.isdir(name)]
        self.movedistance=5
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.health=None
        self.movesRemaining=self.movedistance
        self.clock = pygame.time.Clock()
        self.cellnumbers=cellnumbers
        self.cellnumbers2d=cellnumbers2d
        self.image=pygame.image.load(imgpath).convert_alpha()
        self.rect=self.image.get_rect()
        self.moveSurf=pygame.Surface((500,50))
        self.moveSurf.convert_alpha()
        self.moveSurf.fill((0,0,0))
        self.moveSurf=pygame.transform.scale(self.moveSurf,(int(self.cellnumbers2d[1,1][0])-21,int(self.cellnumbers2d[1,1][1])-21))
        self.moveSurf.set_alpha(100)
        self.selected=False
    def placeSprite(self,(x,y)):
        self.squareNumber2d=(x,y)
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)
    def moveSprite(self,newcellNumber2d,group):
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        finder=Astar.Astar(AstarHelper.successors,AstarHelper.heuristic_to_goal)
        path=[]
        moves=0
        if newcellNumber2d==self.squareNumber2d:
            self.selected=False
            return
        path,moves=finder.compute_path(self.squareNumber2d,newcellNumber2d,self.notmovecells,group)
        if self.selected==True and newcellNumber2d in self.movecells:
            for i in path:
                self.squareNumber2d=(i)
                self.movesRemaining=self.movesRemaining-1
                pygame.time.wait(200)
                drawScreen.drawScreen(self.screen,screensize)
                group.update()
                pygame.display.update()
        self.selected=False
    def select(self,group,drawflag):
        self.movecells=[]
        self.notmovecells=[]
        position=self.squareNumber2d
        f=0
        g=False
        finder=Astar.Astar(AstarHelper.successors,AstarHelper.heuristic_to_goal)
        path=[]
        moves=0
        if drawflag==0:
            for i in range (0,self.movesRemaining+1):
                for z in range (0,self.movesRemaining+1):
                    if self.movesRemaining-(z+i) <0:
                        pass
                    else:
                        ydist=self.movesRemaining-(z+i)
                    self.movecells.append((self.squareNumber2d[0]+i,self.squareNumber2d[1]+ydist))
                    self.movecells.append((self.squareNumber2d[0]-ydist,self.squareNumber2d[1]-z))
                    self.movecells.append((self.squareNumber2d[0]-i,self.squareNumber2d[1]+ydist))
                    self.movecells.append((self.squareNumber2d[0]+ydist,self.squareNumber2d[1]-z))
            self.movecells=list(set(self.movecells))
            for z in self.movecells:
                if z[0] < 0 or z[1] < 0:
                    del z
            for i in self.cellnumbers2d:
                if i not in self.movecells:
                    self.notmovecells.append(i)
            for i in group.sprites():
                for f,z in enumerate(self.movecells):
                    if i.squareNumber2d==z:
                        self.notmovecells.append(z)
                        del self.movecells[f]
            for z,i in enumerate(self.movecells):
                path,moves=finder.compute_path(self.squareNumber2d,i,self.notmovecells,group)
                if moves==None:
                    self.movecells=[]
                if moves > self.movesRemaining:
                    del self.movecells[z]
                path=[]
                moves=0
        for i in self.cellnumbers2d:
            if i not in self.movecells:
                drawToScreen.drawToScreen(self.moveSurf,self.screen,i,self.cellnumbers2d)
        drawflag=1

    def update(self):
        drawToScreen.drawToScreen(self.image,self.screen,self.squareNumber2d,self.cellnumbers2d)
    def moveUp(self):
        self.squareNumber2d=(self.squareNumber2d[0],self.squareNumber2d[1]-1)
        self.movesRemaining=self.movesRemaining-1
    def moveDown(self):
        self.squareNumber2d=(self.squareNumber2d[0],self.squareNumber2d[1]+1)
        self.movesRemaining=self.movesRemaining-1
    def moveRight(self):
        self.squareNumber2d=(self.squareNumber2d[0]+1,self.squareNumber2d[1])
        self.movesRemaining=self.movesRemaining-1
    def moveLeft(self):
        self.squareNumber2d=(self.squareNumber2d[0]-1,self.squareNumber2d[1])
        self.movesRemaining=self.movesRemaining-1
    def newTurn(self):
        self.movesRemaining=self.movedistance


