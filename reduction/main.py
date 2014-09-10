'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial


if __name__ == '__main__':
	degree = 32
	f = open('list_' + str(degree) + '.txt','r')
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)


	dic = { }
	red = Reduction()
	print red.reduction([16,8,0])
	