
'''
Created on 1 May 2015

@author: gustavo
'''

import math
from collections import defaultdict


NULL = -1

class OptG(object):

    def optimize(self, matrix, degree):
        self.matrix = matrix
        self.variable = 2*degree-1
        self.degree = degree
        self.variables = defaultdict()
        size = self._max_size_colum(self.matrix)
        print_matrix(self.matrix)
        for i in xrange(0, size+1):
            self.matrix = self.sort(self.matrix)
            self.matrix = self.doIt(self.matrix)

        return self.variables, self.matrix

    def doIt(self, matrix):  
        
    
    def _is_equal(self, pair, pair_to_compare):
        return (pair == pair_to_compare)

    def _put_column(self, column, matrix, j):
        for i in xrange(0,len(matrix)):
            matrix[i][j] = column[i]

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








