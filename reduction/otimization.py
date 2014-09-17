'''
Created on 10 Sep 2014

@author: gustavo
'''

import math
from collections import defaultdict

class Otimization(object):

    def otimize(self, matrix, degree, deepth):
        #print 'matrix'
        self.degree = degree
        columns = defaultdict(list)
        for i in xrange(0,len(matrix[0])):
            column = self.column(matrix,i)
            for j in xrange(i+1,len(matrix[0])):
                column_2 = self.column(matrix,j)
                if self.compare_column(column,column_2) > 2:
                    columns[i].append(j)
       	#for i in xrange(0,3): 
        self.change(columns,matrix, deepth)
        #print columns
        
	self.printMatrix(matrix)
	return matrix              
        
        #self.printMatrix(matrix)


    def matches(self):
        return self.matches

    def change(self, columns, matrix, deepth):
        matches = defaultdict(set)
        for row in range(1,len(matrix)):
            for i in columns:
                if (len(columns[i]) > deepth):
                    for e in columns[i]:
                        for row_2 in range(row+1, len(matrix)):
                            if(matrix[row][i] == matrix[row_2][e]) and (matrix[row][i] <> -1) and (matrix[row_2][e] <> -1):
                                temp_str = "A" + str(matrix[0][i]);
                                matches[temp_str].add(matrix[row_2][e])
                                matches[temp_str].add(matrix[row][i])
                                matrix[row_2][e] = temp_str
                                matrix[row][i] = temp_str
        
        for i in matches:
            matches[i] = sorted(matches[i])
        print matches
	self.matches = matches


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
