'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial

if __name__ == '__main__':
	degree = 32
	f = open('list_' + str(degree) + '.txt','r')
	pol = Polynomial('x^32 + x^12 + x^1 + 1')
	print pol
	#pols = []
	#for line in f:
	#	pol = Polynomial(line)
	#	pols.append(pol)

	#print pols
	
	red = Reduction()
	p = [16,8,0]
	red.reduction(p)