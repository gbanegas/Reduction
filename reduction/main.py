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
	degree = 113
	f = open('list_' + str(degree) + '.txt','r')
	save = open('result_' + str(degree) + '.txt','w')
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)

	dic = { }
	fn = len(pols)/2
	t1 = ThreadCount(1,lock, pols[0:fn], dic)
	t2 = ThreadCount(2,lock, pols[fn:len(pols)-1], dic)
	t1.start()
	t2.start()
	t1.join()
	t2.join()
#	red = Reduction()
#	print red.reduction([16,12,8,4,0])
	for i in dic:
		r = str(i.coefs()) + " xors: " + str(dic[i])
		save.write(r + '\n')
	
