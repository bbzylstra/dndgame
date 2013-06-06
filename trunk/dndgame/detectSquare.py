__author__ = 'Brad'
def detectSquare(x,y,xi,yi,screensize):
    cellNumber=(-1)
    for i,w in enumerate(y):
        for z,h in enumerate(x):
            if (xi>=(x[-1]) or yi>=(y[-1])):
                cellNumber=(-1)
                return cellNumber
            else:
                if (xi>h and xi<x[z+1]) and (yi>w and yi<y[i+1]):
                    cellNumber=(len(x)-1)*i+z
    return cellNumber
