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
	degree = 163
	directory = str(degree)
	if not os.path.exists(directory):
		os.makedirs(directory)
	f = open('pol_' + str(degree) + '_.txt','r')
	save = open('result_' + str(degree) + '.txt','w')
	pols = [
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)

	
	fn = len(pols)/2
	fn2 = len(pols)/4
	t1 = ThreadCount(1,lock, pols, save)
	t2 = ThreadCount(2,lock, pols[fn:fn2], save)
	t3 = ThreadCount(3,lock, pols[fn2:len(pols)-1], save)
	t1.start()
	t2.start()
	t3.start()
	t1.join()
	t2.join()
	t3.join()
	#red = Reduction()
	#print red.reduction([16,12,8,4,0])
	if (not t1.isAlive() and t2.isAlive() and t3.isAlive()):
		save.close();
	
