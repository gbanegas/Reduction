'''
Created on 06 Apr 2015

@author: gustavo
'''



class Pair(object):
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y

	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)

	def __str__(self):
		return '({0.x!s}, {0.y!s})'.format(self)

	def __iter__(self):
		for each in self.__dict__.keys():
			yield self.__getattribute__(each)