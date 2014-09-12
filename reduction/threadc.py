'''
Created on 10 Sep 2014

@author: gustavo
'''
import threading
from reduction import Reduction

class ThreadCount(threading.Thread):

	def __init__(self, threadID,  locker, polynomials, dicr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.locker = locker
		self.polynomials = polynomials
		self.dicr = dicr
	
	def run(self):
		print "Starting thread: " + str(self.threadID) + '\n'
		for i in self.polynomials:
			count = red(i.coefs())
			self.locker.acquire()
			print str(i.coefs()) + " : Xors : " + str(count)
			self.dicr[i] = count
			self.locker.release()


def red(i):
	reduc = Reduction()
	count = reduc.reduction(i)
	return count

