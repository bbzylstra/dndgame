__author__ = 'Brad'
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *

def get_key():
    while 1:
        event = pygame.event.poll()
        mods=pygame.key.get_mods()
        if event.type == KEYDOWN:
            if mods and KMOD_SHIFT:
                return event.key-32
            else:
                return event.key
        else:
            pass

def display_box(screen, message,(x,y)):
    xi,yi=screen.get_size()
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font("freesansbold.ttf",yi/70)
    pygame.draw.polygon(screen, (255,0,0),[(x,y),(x+xi/1.5,y),(x+xi/1.5,y+yi/25),(x,y+yi/25)],1)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,0,0),(0,0,0)),
            (x+xi/70, y +yi/80))
    pygame.display.update()
def display_message(screen, message,(x,y)):
    "Print a message in a box in the middle of the screen"
    fontobject = pygame.font.Font("freesansbold.ttf",13)
    if len(message) != 0:
        screen.blit(fontobject.render(message, 1, (255,0,0),(0,0,0)),
            (x,y))
    pygame.display.update()

def ask(screen, question,(x,y)):
    "ask(screen, question) -> answer"
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + string.join(current_string,""),(x,y))
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == K_RETURN:
            break
        elif inkey == pygame.K_ESCAPE:
            return 'FALSE'
            break
        elif inkey == K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
            print inkey
        screen.fill((0,0,0))
        display_box(screen, question + string.join(current_string,""),(x,y))
    print str(current_string)
    return string.join(current_string,"")
