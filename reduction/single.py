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