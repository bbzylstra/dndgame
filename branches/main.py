__author__ = 'Brad'
import ctypes
import pygame,sys,os,drawScreen,detectSquare,drawToScreen,charactercreation,comtest,Sprite,spriteSelected,characterselection, open_screen,game
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
orcKnight=sprite_path+'ork_knight.png'
game1 = game_font.render("Cell Number: " + str(cellNumber), True, (255,0, 0), (0, 0, 0))
cellnumbers2d={}
cellNumber2d=(0,0)
spriteselected=''
name, race, cclass, hp, mana, stamina, stre, agl, inte, cour, dex, conc=characterselection.characterSelect(screen)
while running:
    open_screen.openScreen(screen)
    game.game(screen)