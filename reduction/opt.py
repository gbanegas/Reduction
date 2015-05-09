import math
from collections import defaultdict


NULL = -1

class Opt(object):

    def optimize(self, matrix, degree):
        self.var = 2*degree-1
        print self.var
        self.variables = defaultdict()

        numbers = [x for x in xrange(degree, 2*degree-1)]
        print "numbers : " + str(numbers)
        for m in numbers:
            self.doIt(m, matrix)
            print_matrix(matrix)
        
        print self.variables
        

        return self.variables, matrix


    def doIt(self, m, matrix):
        i = 1
        finish = False
        while(not finish):
            match = defaultdict(list)
            pair = (m,m+i)
            pos = []
            for j in xrange(0, len(matrix[0])):
                column = self._column(matrix, j)
                find = self._search_pair_in_column(pair, column)
                if find:
                    if pair in match:
                        match[pair] = match[pair]+1
                    else:
                        match[pair] = 1
                    pos.append(j)
            if(type(match[pair]) is int):
                if(match[pair] >= 2):
                    print "Match: " + str(pair)
                    self._change(pair, pos, matrix)
            i += 1 
            if (m+i > self.var):
                finish = True

    def _change(self, pair, pos, matrix):
        self.variables[self.var] = pair
        find = False
        for i in pos:
            column = self._column(matrix,i)
            for j in xrange(0, len(column)):
                if(column[j] == pair[0]):
                    for h in xrange(j, len(column)):
                        if column[h] == pair[1]:
                            column[h] = -1
                            column[j] = self.var
                            find = True
            self.putColumn(column, matrix, i)

        if(find):
            self.var += 1


        self.sort(matrix)




    def _search_pair_in_column(self, pair, column):
        for i in xrange(0, len(column)):
            if pair[0] == column[i]:
                for j in xrange(i, len(column)):
                    if (pair[1] == column[j]):
                        return True
        return False


        

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
