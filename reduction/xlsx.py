'''
Created on 10 Sep 2014

@author: gustavo
'''

import xlsxwriter

class Xslxsaver(object):

	def create_worksheet(self,exp):
		name = "degree_"
		self.degree = exp[0]
		for i in exp:
			name = name +  str(i) + "_"
		name = name + ".xlsx"
		self.workbook = xlsxwriter.Workbook(name)

	def save(self, matrix, name):
		#TODO to save in an xlsx
		worksheet = self.workbook.add_worksheet(name)
		print self.degree
		for i in xrange(0,len(matrix)):
			row = matrix[i]
			for j in xrange(0,len(row)):
				if row[j] == -1:
					worksheet.write(i, j, '')
				else:
					worksheet.write(i, j, row[j])
				 



	def close(self):
		self.workbook.close()
