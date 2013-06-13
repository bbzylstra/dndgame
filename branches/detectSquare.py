__author__ = 'Brad'
def detectSquare(x,y,xi,yi,screensize):
    cellNumber=(-1)
    cellNumber2d=[]
    for i,w in enumerate(y):
        for z,h in enumerate(x):
            if ((xi>(screensize[0]-screensize[0]/5)) or yi>(screensize[1]-screensize[1]/5)):
                cellNumber=(-1)
                return cellNumber
            else:
                if (xi>h and xi<x[z+1]) and (yi>w and yi<y[i+1]):
                    cellNumber=(len(x)-1)*i+z
                    cellNumber2d=[z,i]
    return cellNumber,cellNumber2d
