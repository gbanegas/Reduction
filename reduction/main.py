'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount

import threading
if __name__ == '__main__':
	lock = threading.Lock()
	degree = 163
	f = open('pent_list_' + str(degree) + '.txt','r')
	save = open('pent_result_' + str(degree) + '.txt','w')
	pols = []
	for line in f:
		pol = Polynomial(line)
		red = Reduction()
		count = red.reduction(pol.coefs())
		r = str(pol.coefs())  + ":" + str(count)
		print r
		save.write(r)
		del red

	save.close()
	fn = len(pols)/4
	fn2 = len(pols)/2

	#t1 = ThreadCount(1,lock, pols, save)
	#t2 = ThreadCount(2,lock, pols[fn:fn2], save)
	#t3 = ThreadCount(3,lock, pols[fn2:len(pols)-1], save)
	#t1.start()
	#t2.start()
	#t3.start()
	#t1.join()
	#t2.join()
	#t3.join()
#	red = Reduction()
#	print red.reduction([16,12,8,4,0])
	#if (not t1.isAlive()):
	#	save.close();
	
