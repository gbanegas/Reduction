'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
from collections import defaultdict

class Otimization(object):

    def otimize(self, matrix, degree, deepth):
        print 'matrix'
        columns = defaultdict(list)
        for i in xrange(0,len(matrix[0])):
            column = self.column(matrix,i)
            for j in xrange(i,len(matrix[0])-1):
                column_2 = self.column(matrix,j)
                if self.compare_column(column,column_2) > (len(matrix) - deepth):
                    columns[i].append(j)


                    
        print columns
        #self.printMatrix(matrix)

    def compare_column(self,column1, column2):
        match = 0;
        for i in column1:
            if i <> -1:
                for j in column2:
                    if j <> -1:
                        if (i == j):
                            match = match + 1
        return match


    def sum_column(self, matrix, i):
        column = [row[i] for row in matrix]
        return sum(column)
    
    def column(self, matrix, i):
        return [row[i] for row in matrix]            

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))