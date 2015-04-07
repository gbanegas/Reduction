'''
Created on 06 Apr 2015

@author: gustavo
'''

import math
from collections import defaultdict
from pair import Pair

class Ot(object):

	def optimize(self, matrix, degree, deepth):
		self.matrix = matrix
		self.deepth = deepth
		pairs = self.__find_pairs__()

		print "pairs : " + str(pairs)



	def __find_pairs__(self):
		columns = defaultdict()
		pairs = self.mount_all_pairs(self.matrix)

		repeated = []
		for i in xrange(0,len(pairs)):
			for j in xrange(i+1, len(pairs)):
				if self.pair_equal(pairs[i], pairs[j]):
					repeated.append(j)
		for j in repeated:
			del pairs[j]
		print "All - repeated:" + str(pairs)
		for pair in pairs:
			for j in xrange(0, len(self.matrix[0])):
				matches = self.find_matches(pair, self.matrix, j)
				columns[pair] = matches 
		return columns
		

	def mount_all_pairs(self, matrix):
		allPairs = []
		for i in xrange(0,len(self.matrix[0])):
			result = self.generate_pairs(self.column(self.matrix,i))
			allPairs = allPairs + result
		print "all pairs_ : " + str(allPairs)
		return allPairs


	def find_matches(self, pair, matrix, j):
		matches = 0
		collumn = self.column(matrix, j)
		pairs = self.generate_pairs(collumn)
		print "all pairs per collumn: " + str(pairs)
		for pair_to_compare in pairs:
			print "Comparing = " + str(pair) + " == " + str(pair_to_compare)
			if self.pair_equal(pair_to_compare, pair):
				matches = matches + 1
		return matches

	def pair_equal(self, pair_to_compare, pair):
		if pair_to_compare[0] == pair[0]:
			if pair_to_compare[1] == pair[1]:
				return True
		return False

	def generate_pairs(self, collumn):
		result = []
		for i in xrange(1, len(collumn)):
			if collumn[i] <> -1:
				p1 = collumn[i]
				for j in xrange(i+1, len(collumn)):
					p2 = collumn[j]
					if p2 <> -1:
						result.append((p1, p2))
		print result
		return result
		



	def pair_not_contain_null(self, pair):
		p1 = pair[0]
		p2 = pair[1]
		if p1 == -1 or p2 == -1:
			return False
		else:
			return True

	def find_match(self, collumn1, collumn2):
		match = 0
		for i in collumn1:
			for j in collumn2:
				if i <> -1 and j <> -1:
					if i == j:
						match += 1
		return match

	def mount_pair(self, matrix, i):
		column = self.column(matrix, i)
		p1 = -1
		p2 = -1
		for i in xrange(1, len(column)):
			if column[i] <> -1:
				if p1 <> -1:
					p2 = column[i]
				else:
					p1 = column[i]
		print "Column : " + str(column)
		return (p1, p2)

	
	def column(self, matrix, i):
		return [row[i] for row in matrix]       