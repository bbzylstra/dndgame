__author__ = 'Brad'
def spriteSelected(cellNumber2d,group):
    for i in group.sprites():
        if i.squareNumber2d==cellNumber2d:
            return i
        else:
            pass