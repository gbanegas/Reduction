'''
Created on 10 Sep 2014

@author: gustavo
'''

import math

class Otimization(object):

    def otimize(self, matrix, degree, deepth):
        print 'matrix'
        for i in xrange(1, len(matrix)):
            row = matrix[i]
            index = self.findNotNull(row)
            self.optimize(matrix,row[index])

        self.printMatrix(matrix)


    def optimize(self, matrix, element):
        dic = {}
        for i in xrange(0, len(matrix)-1):
            row = matrix[i]
            for j in xrange(0, len(row)):
                if row[j] == element:
                    if matrix[i+1][j] <> -1:
                        if  matrix[i+1][j] in dic:
                            value = dic[ matrix[i+1][j]] +1
                        else:
                            dic[matrix[i+1][j]] = 1
        
        key = 0;
        app = -1
        for i in dic:
            if dic[i] > app:
                key = i
                app = dic[i]

        for i in xrange(0, len(matrix)-1):
            row = matrix[i]
            for j in xrange(0, len(row)):
                if row[j] == element:
                    if matrix[i+1][j] ==  key:
                        matrix[i+1][j] = 'T'
                        row[j] = 'T'
                        matrix[i] = row
                       

    def findNotNull(self, row):
        for i in xrange(0, len(row)):
            if row[i] <> -1:
                return i

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))