import math
from math import *
def partieDecimal(n, m, nbre):
    reste = n%m
    div = ''
    i = 0
    if reste == 0:
        return 0
    while len(div) < nbre:
        if reste != 0:
            if reste < m:
                reste = reste * 10
            else:
                div = div + str(reste//m)
                reste = reste%m
        i = i + 1


    return div

if __name__ == '__main__':

    n = int(input())
    m = int(input())

    nbre = int(input())

    print(partieDecimal(n,m, nbre))
