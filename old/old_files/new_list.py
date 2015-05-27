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


def recoverfile(saved, readed):
	if not os.path.exists(saved):
		return True, []
	f = open(saved,'r')
	if(not os.stat(saved).st_size==0):
		pols = []
		pols_done = []
		for line in readed:
			pol = Polynomial(line) 
			pols.append(pol)
		for line in f:
			line = line.replace("[","")
			line = line.replace("]","")
			spl = line.split(',')
			p = ""
			for i in xrange(0,len(spl)-1):
				p = p + " + x^" + str(spl[i].replace(" ","")) 
			p = p + " + 1"
			p = p.replace("+","",1)
			#print p
			pol_ = Polynomial(p) 
			pols_done.append(pol_)
		
		pols_set = set(pols)
		pols_set_done = set(pols_done)
		result = pols_set - pols_set_done
		return False, list(result)
	else:
		return True, []

if __name__ == '__main__':
	degree = 571
	save = 'result_pol_'+str(degree)+'.txt'
	f = open('pol_' + str(degree)+ '.txt','r')
	newfile = open('pol_571_n', 'a')
	newfile_2 = open('pol_571_n_2', 'a')
	read, pols = recoverfile(save, f)
	print len(pols)
	l = len(pols)/2
	pol_1 = pols[0:l]
	pol_2 = pols[l+1:len(pols)]

	for pol in pol_1:
		newfile.write(str(pol) + "\n")
	for pol in pol_2:
		newfile_2.write(str(pol)+"\n")
	print len(pol_1) + len(pol_2)
	newfile.close()
	newfile_2.close()
	
	
	
	
	
