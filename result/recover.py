
import os
from collections import OrderedDict

if __name__ == '__main__':
	f = open('result_pol_571.txt','r')
	pols_done= []
	for line in f:
		line = line.replace("[","")
		line = line.replace("]","")
		spl = line.split(',')
		p = ""
		degrees = []
		for i in xrange(0,len(spl)-1):
			degrees.append(int(spl[i].replace(" ","")))
		degrees.append(0)
		degrees.sort(reverse=True)
		print spl[len(spl)-1].replace("0:", "")
		#print p
		
		pols_done.append(degrees)
	

	pols = list(pols_done)
	#print pols
	