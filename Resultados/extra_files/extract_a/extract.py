import os
from collections import OrderedDict
from polynomial import Polynomial

if __name__ == '__main__':
    f = open('pol_571_.txt','r')
    pols = []

    for line in f:
        pol = Polynomial(line)
        pols.append(pol.coefs()[1])

    s = sorted(set(pols))
    print s

    