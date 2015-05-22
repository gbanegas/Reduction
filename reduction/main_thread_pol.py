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
	lock = threading.Lock()
	lockScreen = threading.Lock()
	files = ["pent_2.txt", "pent_3.txt", "pent_4.txt", "pent_5.txt"]
	degrees = [21, 97, 139, 163, 233, 283]
	degree = 571
	for fileName in files:
		save = 'result_pol_'+fileName    
		f_save = open(save, "a")
		f = open(fileName,'r')
		read, pols = recoverfile(save, f)
		if read:
			for line in f:
				pol = Polynomial(line)
				pols.append(pol)
		print len(pols)
		print "I am here"
		# threads = []
		# i = 0
		# j = 2
		# for temp in range(0, len(pols)/2):
		# 	if (j > len(pols)):
		# 		j = len(pols)
		# 		thread = ThreadCount(temp,lockScreen, lock, pols[i:j], save)
		# 		i = j+1
		# 		j += 2
		# 		threads.append(thread)
		# for thread in threads:
		# 	thread.start()
			# for current in threads:
		# 	current.join()
		for i in pols:
			print "doing pol: " + str(i.coefs())
			reduc = Reduction()
			count = reduc.reduction(i.coefs())
			r = str(i.coefs()) + ":" + str(count)
			f_save.write(r + '\n')
			del reduc








