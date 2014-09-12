'''
Created on 10 Sep 2014

@author: gustavo
'''
import threading
from reduction import Reduction

class ThreadCount(threading.Thread):
	

	def __init__(self, threadID,  locker, polynomials, save):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.locker = locker
		self.polynomials = polynomials
		self.save = save
	
	def run(self):
		print "Starting thread: " + str(self.threadID) + '\n'
		for i in self.polynomials:
			reduc = Reduction()
			count = reduc.reduction(i.coefs())
			self.locker.acquire()
			r = str(i.coefs()) + ":" + str(count)
			print r
			self.save.write(r + '\n')
			self.locker.release()
			del reduc
			

