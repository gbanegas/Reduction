'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
from xlsx import Xslxsaver

from otimization import Otimization

NULL = -1
max_collum = 0
mdegree = 0;


class Reduction(object):



    def reduction(self,exp):
        otimizator = Otimization()
        exp_sorted = sorted(exp, reverse=True)
        self.mdegree = exp_sorted[0]
        self.max_collum = (2*exp_sorted[0])-1
        nr = self.calcNR(exp_sorted)
        self.matrix = self.generateMatrix()
        exp_sorted.remove(self.mdegree)
        for i in range(0,len(exp_sorted)):
            self.reduceFirst(self.matrix, exp_sorted[i])
        self.clean(self.matrix)
        for i in range(1,nr):
            self.reduceOthers(self.matrix,exp_sorted)
        self.clean(self.matrix)
        self.removeRepeat(self.matrix)
        self.clean(self.matrix)
        xls = Xslxsaver()
        xls.create_worksheet(exp)
        xls.save(self.matrix, 'Not Optimized')
        self.matrix = otimizator.otimize(self.matrix, self.mdegree, 1)
        row = [-1 for x in xrange(self.max_collum)]
        self.matrix.append(row)
        count = self.countXor(self.matrix)
        #self.clean(self.matrix)
        xls.save(self.matrix, 'Optimized')
        self.delete()
#        self.printMatrix(self.matrix)
        xls.close()
        return count


    def countXor(self, matrix):
        rowToWrite = [-1 for x in xrange(self.max_collum)]
        row = matrix[0]
        for j in range(self.mdegree-1,len(row)):
            countT = 0
            element = row[j]
            if element <> NULL:
                for l in range(1, len(matrix)):
                    rowToCompare = matrix[l]
                    elementToCompare = rowToCompare[j]
                    if elementToCompare <> NULL:
                        countT = countT + 1;
            rowToWrite[j] = countT
        matrix.append(rowToWrite)
        rowToCalc = matrix[len(matrix)-1]
        count = 0
        for i in range(self.mdegree-1,len(rowToCalc)):
            tx = rowToCalc[i]
            count = count + tx
        return count


    def delete(self):
        del self.matrix 

   


    def clean(self, matrix):
        toRemove = []
        for m in matrix:
            if self.isClean(m):
                toRemove.append(m)
        for i in toRemove:
            matrix.remove(i)

    def isClean(self, row):
        for i in row:
            if i <> NULL:
                return False
        return True

    def reduceOthers(self, matrix, exp):
        toReduce = self.needToReduce(matrix)
        for index in toReduce:
            for e in exp:
                reduceRow = self.reduce(matrix[index],e)
                matrix.append(reduceRow)
            self.cleanReduced(matrix,index)

    def removeRepeat(self, matrix):
        for j in range(1, len(matrix)):
            row = matrix[j]
            for i in range(self.mdegree-1, len(row)):
                found = False
                valueToCompare = row[i]
                if valueToCompare <> NULL:
                    for m in range(j+1, len(matrix)):
                        rowToCompare = matrix[m]
                        toCompare = rowToCompare[i]
                        if toCompare <> NULL:
                            if valueToCompare == toCompare:
                                rowToCompare[i] = NULL;
                                row[i] = NULL;
                                found = True;
                        matrix[m] = rowToCompare
                        if found:
                            break
            matrix[j] = row

    def cleanReduced(self, matrix, index):
        row = matrix[index]
        for j in range(0,self.mdegree-1):
            row[j] = NULL
        matrix[index] = row

    def reduce(self, row, exp):
        index = self.max_collum-1;
        rowReduced = [-1 for x in xrange(self.max_collum)]
        for j in range(self.mdegree-2,-1,-1):
            element = row[j]
            rowReduced[index - exp] = element
            index = index -1
        return rowReduced

    def needToReduce(self, matrix):
        indexOfRows = []
        index = (self.max_collum - 1 - self.mdegree);
        for i in range(1,len(matrix)):
            row = matrix[i]
            if row[index] <> NULL:
                indexOfRows.append(i)
        
        return indexOfRows


    def reduceFirst(self, matrix, exp):
        index = self.max_collum-1;
        row = [-1 for x in xrange(self.max_collum)]
        for j in xrange(self.mdegree-2,-1,-1):
            element = matrix[0][j]
            row[index - exp] = element
            index = index -1

        matrix.append(row) 

    def calcNR(self, exp_sorted):
        nr = 2
        temp = (exp_sorted[0]+1)/2
        deg = math.floor(temp)
        if exp_sorted[1] > deg:
            nr = 2* (exp_sorted[0] + 1) - exp_sorted[0]
        return nr

    def generateMatrix(self):
        row = sorted(list(range(0, self.max_collum)), reverse=True)
        matrix = [row] 
        return matrix

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))

