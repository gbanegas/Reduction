import math
from collections import defaultdict
import numpy as np

NULL = -1
MAX = 99999999

class OptNumpy(object):

    def optimize(self, matrix, degree):
        m = np.asmatrix(matrix)
        m = self.sort_matrix(m)
        #print m
        self.variables = defaultdict()
        self.var = 2*degree-2
        numbers = xrange(degree, 2*degree-2)
        for n in numbers:
            self.doIt(n, m)
            
        return self.variables, m

    def doIt(self, n, m):
        i = 1
        finish = False
        while(not finish):
            value = n+i
            goodvalues = [(n,value)]
            ix = np.in1d(m.ravel(), goodvalues).reshape(m.shape)
            pos = self._find_positions_(ix)

            if(len(pos) >= 2):
                m = self._replace_(pos, m, (n,value))

            if (n+i > self.var):
                finish = True
            i += 1

    def _replace_(self, pos, m, pair):
        for i in pos:
            m[pos[i][0],i] = self.var
            m[pos[i][1],i] = -1
        self.variables[self.var] = pair
        self.var += 1
        return m
                 

    def _find_positions_(self, ix):
        pos = defaultdict(list)
        columns = defaultdict(list)
        for i in xrange(0, len(ix[0])):
            column = self.column_num_py(ix, i)
            s =  np.sum(column)
            if s >= 2:
                columns[i].append(column)

                
        if len(columns) > 1:
            #print columns
            for col in columns:
                c = columns[col]
                for i in xrange(0, len(c)):
                    pos[col] = self._pos_elements_(c)

        return pos

    def _pos_elements_(self, column):
        pos = []
        #print column
        for i in xrange(0, len(column[0])):
            if column[0][i]:
                pos.append(i)
        return pos

    def sort_matrix(self, m):
        m[m < 0] = MAX
        m = np.sort(m, axis=0)
        m[m == MAX ] = NULL
        return m


    def row_num_py(self, m, i):
        return m[i,:]

    def column_num_py(self, m, i):
        return m[:,i]


    def sort(self, matrix):
        matrix = self.__remove__(matrix, -1, "")
        for i in xrange(0, len(matrix[0])):
            column = self._column(matrix, i)
            column.sort()
            self.putColumn(column, matrix, i)
        matrix = self.__remove__(matrix, "", -1)
        return matrix

    def _column(self, matrix, i):
        return [row[i] for row in matrix]


    def __remove__(self, matrix, toCompare, toChange):
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[i])):
                if matrix[i][j] == toCompare:
                    matrix[i][j] = toChange
        return matrix

    def putColumn(self, column, matrix, j):
        for i in xrange(0,len(matrix)):
            matrix[i][j] = column[i]