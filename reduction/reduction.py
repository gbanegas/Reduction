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
        mdegree = exp_sorted[0]
        self.max_collum = (2*exp_sorted[0])-1
        nr = self.calcNR(exp_sorted)
        matrix = self.generateMatrix()
        for r in matrix:
            print ''.join(str(r))
        

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
        
