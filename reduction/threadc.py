'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction

class ThreadCount():

	def __init__(self, threadID,  lock, polynomials, dicr):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.lock = lock
		self.polynomials = polynomials
		self.dicr = dicr

	

