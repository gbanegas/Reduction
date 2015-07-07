'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
from xlsx import Xslxsaver
import re
from ot import Ot

import copy

NULL = -1
max_collum = 0
mdegree = 0;


class Reduction(object):



    def reduction(self,exp):
        xls = Xslxsaver()
        xls.create_worksheet(exp)
        self.otimizator = Ot()
        exp_sorted = sorted(exp, reverse=True)
        self.mdegree = exp_sorted[0]
        self.max_collum = (2*exp_sorted[0])-1
        nr = self._calc_NR(exp_sorted)
        self.matrix = self._generate_matrix()

        exp_sorted.remove(self.mdegree)

        for i in range(0,len(exp_sorted)):
            self._reduce_first(self.matrix, exp_sorted[i])
        for i in range(0,nr):
            self._reduce_others(self.matrix,exp_sorted)

        #print "Sem remocoes"
        #print_matrix(self.matrix)
       # print "Size of Columns ", len(self.matrix)
        print "Finish Reducing..."


        #self.matrix_copy = copy.deepcopy(self.matrix)
        xls.save(self.matrix, 'Not Optimized_1')
        #print_matrix(self.matrix)
        #t = self.reduce_matrix(self.mdegree, self.matrix)
        #print_matrix(t)
        self._remove_repeat(self.matrix)
        self.clean(self.matrix)
        #xls.save_complete(self.matrix)
        self.matrix = self.otimizator.sort(self.matrix)
        self.clean(self.matrix)
        self.matrix = self.reduce_matrix(self.mdegree, self.matrix)
        #print_matrix(self.matrix)
        xls.save(self.matrix, 'Not Optimized')
        self.p, self.matrix = self.otimizator.optimize(self.matrix, self.mdegree)
        self._remove_one(self.matrix)
        #print_matrix(self.matrix)
        row = [-1 for x in xrange(self.mdegree)]
        self.matrix.append(row)
        count = self._count_xor(self.matrix,self.p)
        #count = count + self.countMatchs(otimizator.matches)
        xls.save(self.matrix, 'Optimized')
        #self.p_, self.matrix_copy = otimizator.optimize(self.matrix_copy, self.mdegree, 1)
        xls.save_matches(self.p)
        #print_matrix(self.matrix)
        #print self.p
        del self.matrix
        return count

    def reduce_matrix(self, degree, matrix):
        #print "printing..."
        matrix_copy = [[-1 for x in range(degree)] for x in range(len(matrix))]
        for i in xrange(0, len(matrix)):
            h = 0
            #print i
            for j in xrange(degree-1, len(matrix[0])):
                matrix_copy[i][h] = matrix[i][j]
                h += 1

        #print_matrix(matrix_copy)
        return matrix_copy

    def _count_matchs(self, matches):
        count = 0;
        for i in matches:
            count = count + (len(matches[i])-1)
        return count

    def _count_xor(self, matrix, p):
        rowToWrite = [-1 for x in xrange(self.mdegree)]
        row = matrix[0]
        for j in range(0,len(row)):
            countT = 0
            element = row[j]
            if element <> NULL:
                for l in range(1, len(matrix)):
                    rowToCompare = matrix[l]
                    elementToCompare = rowToCompare[j]
                    if elementToCompare <> NULL or (re.search('[a-zA-Z]', str(elementToCompare)) <> None):
                        countT = countT + 1;
            rowToWrite[j] = countT
        matrix.append(rowToWrite)
        rowToCalc = matrix[len(matrix)-1]
        count = 0
        for i in range(0,len(rowToCalc)):
            tx = rowToCalc[i]
            count = count + tx
        count = count + len(p)
        #print
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

    def _reduce_others(self, matrix, exp):
        to_reduce = self._need_to_reduce(matrix)
        for index in to_reduce:
            for e in exp:
                reduceRow = self.reduce(matrix[index],e)
                matrix.append(reduceRow)
            self._clean_reduced(matrix,index)
        self._remove_repeat(self.matrix)
        matrix = self.clean(matrix)

    def _remove_one(self, matrix):
        for j in range(1, len(matrix)):
            row = matrix[j]
            for i in range(self.mdegree-1, len(row)):
                valueToCompare = row[i]
                if valueToCompare <> NULL:
                    for m in range(j+1, len(matrix)):
                        rowToCompare = matrix[m]
                        toCompare = rowToCompare[i]
                        if toCompare <> NULL:
                            if valueToCompare == toCompare:
                                rowToCompare[i] = NULL;
                        matrix[m] = rowToCompare
            matrix[j] = row


    def _remove_repeat(self, matrix):
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

    def _clean_reduced(self, matrix, index):
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

    def _need_to_reduce(self, matrix):
        indexOfRows = []
        index = (self.max_collum - 1 - self.mdegree);
        for i in range(1,len(matrix)):
            row = matrix[i]
            if row[index] <> NULL:
                indexOfRows.append(i)

        return indexOfRows


    def _reduce_first(self, matrix, exp):
        index = self.max_collum-1;
        row = [-1 for x in xrange(self.max_collum)]
        for j in xrange(self.mdegree-2,-1,-1):
            element = matrix[0][j]
            row[index - exp] = element
            index = index -1

        matrix.append(row)

    def _calc_NR(self, exp_sorted):
        nr = 2
        nr = int(math.floor((exp_sorted[0]-2)/(exp_sorted[0]-exp_sorted[1])))
        print "NR = ", nr
        #temp = (exp_sorted[0]+1)/2
        #deg = math.floor(temp)
        #if exp_sorted[1] > deg:
        #    nr = 2* (exp_sorted[0] + 1) - exp_sorted[0]
        return nr

    def _generate_matrix(self):
        row = sorted(list(range(0, self.max_collum)), reverse=True)
        matrix = [row]
        return matrix

def print_matrix(matrix):

        for r in matrix:
            print ''.join(str(r))
        print '----------------------FIM---------------------'
