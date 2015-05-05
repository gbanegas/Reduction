
'''
Created on 1 May 2015

@author: gustavo
'''

import math
from collections import defaultdict


NULL = -1

class Optmizator(object):

    def optimize(self, matrix, degree):
        self.matrix = matrix
        self.variable = 2*degree-1
        self.degree = degree
        self.variables = defaultdict()
        for i in xrange(0, (self._max_size_colum(self.matrix))):
        #for i in xrange(0,1):
            self.matrix = self.sort(self.matrix)
            self.matrix = self.doIt(self.matrix)
        
        #print_matrix(self.matrix)
        return self.variables, self.matrix

    def doIt(self, matrix):  
        pairs = self._generate_all_pairs(matrix)
        pairs_repeated = self._get_repeated(pairs)
        while len(pairs_repeated) > 0:
            #print pairs_repeated
            pair = pairs_repeated[0]
            #print "Pair : " + str(pair)
            matrix, pairs_repeated = self._find_and_replace(pair, matrix)
        
        for i in self.variables:
            matrix, pairs_repeated = self._find_and_replace(self.variables[i], matrix)
        return matrix

    def _generate_all_pairs(self, matrix, variables = None):
        pairs =[]
        if variables == None:
            for i in xrange(len(matrix[0])-1, 0, -1):
                column = self._column(matrix, i)
                for j in xrange(1, len(column)):
                    p1 = column[j]
                    if p1 <> -1:
                        for h in xrange(j+1, len(column)):
                            p2 = column[h]
                            if p2 <> -1:
                                pairs.append((p1,p2))
        else:
            for i in xrange(len(matrix[0])-1, self.degree, -1):
                column = self._column(matrix, i)
                for j in xrange(1, len(column)):
                    p1 = column[j]
                    if p1 <> -1:
                        for h in xrange(j+1, len(column)):
                            p2 = column[h]
                            if p2 <> -1 and self._not_in((p1,p2),variables):
                                pairs.append((p1,p2))
        return pairs


    def _get_repeated(self, pairs):
        repeated = []
        for i in xrange(0, len(pairs)):
            pair = pairs[i]
            for j in xrange(i+1, len(pairs)):
                if pair == pairs[j]:
                    if pair not in repeated:
                        repeated.append(pair)
        return repeated
    def _find_and_replace(self, pair_to_compare, matrix):
        #print "Buscando Par :" + str(pair_to_compare)
        for i in xrange(len(matrix[0])-1, self.degree-2, -1):
            column = self._column(matrix, i)
        #    print "Antes: " + str(column)
            for j in xrange(0, len(column)):
                if column[j] <> -1:
                    for h in xrange(j, len(column)):
                        if column[h] <> -1:
                            pair = (column[j],column[h])
                            if self._is_equal(pair, pair_to_compare):
                                resutl = self._not_in(pair)
                                if resutl:
                                    self.variable += 1
                                    self.variables[self.variable] = pair
                                column[h] = -1
                                column[j] = self.variable
        #    print "Depois: " + str(column)
            self._put_column(column, matrix, i)
        #print "--F--"
        pairs_= self._generate_all_pairs(matrix, self.variables)
        pairs_repeated = self._get_repeated(pairs_)
        return matrix, pairs_repeated


    def _not_in(self, pair, variables = None):
        if(variables == None):
            for i in self.variables:            
                if pair[0] == self.variables[i][0]:
                    if pair[1] == self.variables[i][1]:
                        return False
        else:
            #print "Variables : " + str(variables)
            for i in variables:
                #print variables[i]
                if pair[0] == variables[i][0]:
                    if pair[1] == variables[i][1]:
                        return False
        return True

    def _is_equal(self, pair, pair_to_compare):
        return (pair == pair_to_compare)

    def _put_column(self, column, matrix, j):
        for i in xrange(0,len(matrix)):
            matrix[i][j] = column[i]

    def _get_pair(self, i, column):
        pairs = []
        for j in xrange(i, len(column)):
            if column[j] <> -1:
                if column[j] <> column[i]:
                    pairs.append((column[i], column[j]))
        return pairs



    def _max_size_colum(self, matrix):
        size = 0
        for i in xrange(0, len(matrix[0])):
            if(size < len(self._column(matrix, i))):
                size = len(self._column(matrix, i))
        return size

    def _column(self, matrix, i):
        return [row[i] for row in matrix]  

    def sort(self, matrix):
        matrix = self.__remove__(matrix, -1, "")
        for i in xrange(0, len(matrix[0])):
            column = self._column(matrix, i)
            column.sort()
            #print column
            self.putColumn(column, matrix, i)
        matrix = self.__remove__(matrix, "", -1)
        return matrix

    def __remove__(self, matrix, toCompare, toChange):
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[i])):
                if matrix[i][j] == toCompare:
                    matrix[i][j] = toChange
        return matrix

    def putColumn(self, column, matrix, j):
        for i in xrange(0,len(matrix)):
            matrix[i][j] = column[i]

def print_matrix(matrix):
    for r in matrix:
       print ''.join(str(r))
    print '-----------------fff--------------------------'








