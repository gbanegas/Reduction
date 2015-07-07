'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
import re
from ot import Ot
from threadred import ThreadRed
from threadremove import ThreadRemove

import copy

NULL = -1
max_collum = 0
mdegree = 0;


class ReductionT(object):

    def __init__(self, exp):
        exp_sorted = sorted(exp, reverse=True)
        self.nr = self._calc_NR(exp_sorted)




    def reduction(self,exp):
        exp_sorted = sorted(exp, reverse=True)
        self.nr = self._calc_NR(exp_sorted)
        self.otimizator = Ot()

        self.mdegree = exp_sorted[0]
        self.max_collum = (2*exp_sorted[0])-1
        self.nr = self._calc_NR(exp_sorted)

        self.matrix = self._generate_matrix()
        exp_sorted.remove(self.mdegree)
        print "Start Reducing..."
        for i in range(0,len(exp_sorted)):
            self._reduce_first(self.matrix, exp_sorted[i])

        #for i in range(0,nr):
        self._reduce_others(self.matrix,exp_sorted)
        print "Finish Reducing..."
        self._remove_repeat(self.matrix)
        print "Finish Remove..."
        self.clean(self.matrix)

        #xls.save_complete(self.matrix)
        self.matrix = self.otimizator.sort(self.matrix)
        self.clean(self.matrix)
        self.matrix = self.reduce_matrix(self.mdegree, self.matrix)
        #print_matrix(self.matrix)
        #xls.save(self.matrix, 'Not Optimized')
        self.p, self.matrix = self.otimizator.optimize(self.matrix, self.mdegree)
        self._remove_one(self.matrix)
            #print_matrix(self.matrix)
        row = [-1 for x in xrange(self.mdegree)]
        self.matrix.append(row)
        count = self._count_xor(self.matrix,self.p)
        #count = count + self.countMatchs(otimizator.matches)
            #xls.save(self.matrix, 'Optimized')
            #self.p_, self.matrix_copy = otimizator.optimize(self.matrix_copy, self.mdegree, 1)
            #xls.save_matches(self.p)
            #print_matrix(self.matrix)
            #print self.p
        del self.matrix
        return count

    def returnNR(self):
        return self.nr

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
        threads = []
        #for i_row in xrange(1, len(matrix)-1):
        #    t =  ThreadRed(matrix[i], exp, self.max_collum)
        #print_matrix(matrix)
        for i_row in xrange(1, len(matrix)-1):
            t =  ThreadRed(matrix[i_row],self.mdegree, exp, self.max_collum,self.nr)
            threads.append(t)
            t.start()

        for t in threads:
            while(t.join()):
                pass

        for t in threads:
            for i in t.getMatrix():
                matrix.append(i)

        self._remove_repeat(matrix)

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

    def putColumn(self, j, column, matrix):
        for i in xrange(0,len(matrix)):
            matrix[i][j] = column[i]

    def _column(self, matrix, i):
        return [row[i] for row in matrix]

    def _remove_repeat(self, matrix):
        threads = []
        for i in xrange(self.mdegree-1, len(matrix[0])):
            thread = ThreadRemove(self._column(matrix, i), i)
            threads.append(thread)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        for t in threads:
            index, column = t.getData()
            self.putColumn(index, column, matrix)

        print "Finished Remove"

        # for j in range(1, len(matrix)):
        #     row = matrix[j]
        #     for i in range(self.mdegree-1, len(row)):
        #         found = False
        #         valueToCompare = row[i]
        #         if valueToCompare <> NULL:
        #             for m in range(j+1, len(matrix)):
        #                 rowToCompare = matrix[m]
        #                 toCompare = rowToCompare[i]
        #                 if toCompare <> NULL:
        #                     if valueToCompare == toCompare:
        #                         rowToCompare[i] = NULL;
        #                         row[i] = NULL;
        #                         found = True;
        #                 matrix[m] = rowToCompare
        #                 if found:
        #                     break
        #     matrix[j] = row

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
        nr = int(math.floor((exp_sorted[0]-2)/(exp_sorted[0]-exp_sorted[1])))+1
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
