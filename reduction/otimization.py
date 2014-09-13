'''
Created on 10 Sep 2014

@author: gustavo
'''

import math

class Otimization(object):

    def otimize(self, matrix, degree, deepth):
        print 'matrix'
        columns = {}
        for i in xrange(0,len(matrix[0])):
            column = self.column(matrix,i)
            for j in xrange(i,len(matrix[0])-1):
                column_2 = self.column(matrix,i)

        #self.printMatrix(matrix)


    def sum_column(self, matrix, i):
        column = [row[i] for row in matrix]
        return sum(column)
    
    def column(self, matrix, i):
        return [row[i] for row in matrix]            

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))