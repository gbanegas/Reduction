'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os
import threading


import threading
if __name__ == '__main__':
	lock = threading.Lock()
	lockScreen = threading.Lock()
	save = open('result_pol_283_2.txt','w')
	degree = 163
	#directory = str(degree)
	# if not os.path.exists(directory):
	# 	os.makedirs(directory)
	f = open('pol_' + str(degree) + '_.txt','r')
	# save = open('result_' + str(degree) + '.txt','w')
	#f = ["x^63 + x^14 + x^7 + x^4 + 1", "x^63 + x^15 + x^7 + x^4 + 1", "x^63 + x^16 + x^7 + x^4 + 1" , "x^63 + x^17 + x^7 + x^4 + 1" ]
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)
	print len(pols)
	threads = []
	i = 0
	j = 15
	for temp in range(0, len(pols)/15):
		if (j > len(pols)):
			j = len(pols)
		thread = ThreadCount(temp,lockScreen, lock, pols[i:j], save)
		i = j+1
		j += 15
		threads.append(thread)

	for thread in threads:
		thread.start()
	
	for current in threads:
		current.join()

	save.close()


