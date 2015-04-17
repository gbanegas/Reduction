'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os

import threading
if __name__ == '__main__':
	lock = threading.Lock()
	lockScreen = threading.Lock()
	degree = 283
	directory = str(degree)
	if not os.path.exists(directory):
	 	os.makedirs(directory)
	f = open('pol_' + str(degree) + '_.txt','r')
	save = open('result_' + str(degree) + '.txt','w')
	pols = []
	for line in f:
	 	pol = Polynomial(line)
	 	pols.append(pol)

	
	fn = len(pols)/2
	fn2 = len(pols)/4
	t1 = ThreadCount(1,lockScreen, lock, pols[0:fn2], save)
	t2 = ThreadCount(2,lockScreen, lock, pols[fn2:fn], save)
	t3 = ThreadCount(3,lockScreen, lock, pols[fn:len(pols)-1], save)
	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()
	red = Reduction()
	di = dict()
	#for i in xrange(0,29):
#		x = red.reduction([30,i,0])
#		

#	print di

	#for k in xrange(2,20):
	#x^283 + x^142 + x^70 + x + 
	resultado = red.reduction([283,142,70,1,0])
	di[k] = resultado
	print resultado
	if (not t1.isAlive() and t2.isAlive() and t3.isAlive()):
	 	save.close();
	
