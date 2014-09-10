'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
import numpy

NULL = -1
max_collum = 0
mdegree = 0;

class Reduction(object):

    def reduction(self,exp):
        exp_sorted = sorted(exp, reverse=True)
        self.mdegree = exp_sorted[0]
        self.max_collum = (2*exp_sorted[0])-1
        nr = self.calcNR(exp_sorted)
        matrix = self.generateMatrix()
       # self.printMatrix(matrix)
        exp_sorted.remove(self.mdegree)
        for i in range(0,len(exp_sorted)):
            self.reduceFirst(matrix, exp_sorted[i])
        self.printMatrix(matrix)



    def reduceFirst(self, matrix, exp):
        index = self.max_collum-1;
        #self.printMatrix(matrix)
        row = [-1 for x in xrange(self.max_collum)]
        for j in range(0,self.mdegree-1):
            element = matrix[1][j]
            row[index - exp] = element
            index = index -1            
        matrix.append(row) 

    def calcNR(self, exp_sorted):
        nr = 2
        temp = (exp_sorted[0]+1)/2
        deg = math.floor(temp)
        if exp_sorted[1] > deg:
            nr = 2* (exp_sorted[0] + 1) - exp_sorted[0]

    def generateMatrix(self):
        row = sorted(list(range(0, self.max_collum)), reverse=True)
        #row2 = [-1 for x in xrange(self.max_collum)]
        matrix = [[]] 
        matrix.append(row)
        #matrix.append(row2)
        return matrix

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))

