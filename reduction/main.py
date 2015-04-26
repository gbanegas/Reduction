'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os


#import threading
if __name__ == '__main__':
        f = open('pol_familia.txt','r')
        save = open('result_nova_familia.txt','w')
        pols = []
        for line in f:
        	pol = Polynomial(line)
        	pols.append(pol)

        redu = Reduction()
        for pol in pols:
        	print pol.coefs()
        	valor = redu.reduction(pol.coefs())
        	save.write(str(pol.coefs()) + ":" + str(valor))