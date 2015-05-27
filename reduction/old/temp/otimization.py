'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
from collections import defaultdict

class Otimization(object):

    def otimize(self, matrix, degree, deepth):
        self.degree = degree
        columns = self.create_match(matrix)
        self.change(columns,matrix, deepth)
        self.secondVerification(matrix)
        #self.printMatrix(matrix)
        return matrix              

    def matches(self):
        return self.matches


    def secondVerification(self, matrix):
        for i in self.matches:
            for r in xrange(1,len(matrix)):
                row = matrix[r]
                for e in xrange(0, len(row)):
                    element = row[e];                    
                    if (element in self.matches[i]):
                        for j in xrange(r+1,len(matrix)):
                            row_2 = matrix[j]
                            if(row_2[e] in self.matches[i] and element in self.matches[i]):
                                matrix[r][e] = i
                                



    def create_match(self, matrix):
        columns = defaultdict(list)
        for i in xrange(0,len(matrix[0])):
            column = self.column(matrix,i)
            for j in xrange(i+1,len(matrix[0])):
                column_2 = self.column(matrix,j)
                howMuchEquals = self.find_match(column,column_2)
                if howMuchEquals > 1:
                    columns[i].append(j)
        #print columns

        return columns




    def change(self, columns, matrix, deepth):
        matches = defaultdict(set)      
        for row in range(1,len(matrix)):
            for i in columns:
                if (len(columns[i]) > deepth):
                    for e in columns[i]:
                        for row_2 in range(row+1, len(matrix)):
                            if(matrix[row][i] == matrix[row_2][e]) and (matrix[row][i] <> -1):
                                temp_str = "A" + str(matrix[0][i]);
                                matches[temp_str].add(matrix[row_2][e])
                                matches[temp_str].add(matrix[row][i])
                                matrix[row_2][e] = temp_str
                                matrix[row][i] = temp_str
        
        for i in matches:
            matches[i] = sorted(matches[i])
        #print matches
        self.matches = matches


    def find_match(self, collumn1, collumn2):
        match = 0
        for i in collumn1:
            for j in collumn2:
                if i <> -1 and j <> -1:
                    if i == j:
                        match += 1
        return match

    def sum_column(self, matrix, i):
        column = [row[i] for row in matrix]
        return sum(column)
    
    def column(self, matrix, i):
        return [row[i] for row in matrix]            

    def printMatrix(self,matrix):
        for r in matrix:
            print ''.join(str(r))
