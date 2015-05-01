
'''
Created on 06 Apr 2015

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
        #for i in xrange(0, (self._max_size_colum(self.matrix))):
        for i in xrange(0,1):
            self.matrix = self.sort(self.matrix)
            self.matrix = self.doIt(self.matrix)
        print_matrix(self.matrix)
        return self.variables, self.matrix

    def doIt(self, matrix):
        for i in xrange(1, len(matrix)):
            row = matrix[i]
            for j in xrange(len(row)-1, 0, -1):
                column = self._column(matrix,j)
                pairs = self._get_pair(i, column)
                self._find_and_replace(pairs, matrix)
        return matrix

    def _find_and_replace(self, pairs, matrix):
        for i in xrange(self.degree- 1, len(matrix[0])):
            column = self._column(matrix, i)
            print column
            for j in xrange(0, len(column)):
                if column[j] <> -1:
                    for h in xrange(j, len(column)):
                        if column[h] <> -1:
                            pair = (column[j],column[h])
                            if self._is_equal(pair, pairs):
                                column[h] = -1
                                if (column[j],column[h]) not in self.variables:
                                    self.variable += 1
                                    self.variables[self.variable] = (column[j],column[h])
                                column[j] = self.variable
            self._put_column(column, matrix, i)


    def _is_equal(self, pair, pairs):
        return (pair in pairs)

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
    #for r in matrix:
    #   print ''.join(str(r))
    print '-----------------fff--------------------------'








