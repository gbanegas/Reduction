'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os
import threading


#import threading
if __name__ == '__main__':
	lock = threading.Lock()
	lockScreen = threading.Lock()
	save = 'file_to_save.txt'
	degree = 2
	f = open('pol_' + str(degree) + '_.txt','r')
	# save = open('result_' + str(degree) + '.txt','w')
	#f = ["x^63 + x^14 + x^7 + x^4 + 1", "x^63 + x^15 + x^7 + x^4 + 1", "x^63 + x^16 + x^7 + x^4 + 1" , "x^63 + x^17 + x^7 + x^4 + 1" ]
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)
	print len(pols)

	
	
	t1 = ThreadCount(1,lockScreen, lock, pols[0:2], save)
	t2 = ThreadCount(2,lockScreen, lock, pols[2+1:4], save)
	t3 = ThreadCount(3,lockScreen, lock, pols[3+1:5], save)

	t1.start()
	t2.start()
	t3.start()

	t1.join()
	t2.join()
	t3.join()