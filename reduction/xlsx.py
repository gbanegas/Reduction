'''
Created on 10 Sep 2014

@author: gustavo
'''

import xlsxwriter

class Xslxsaver(object):
	def save(self, exp, matrix):
		#TODO to save in an xlsx
		name = "degree_"
		for i in exp:
			name = name + str(i) + "_"
		name = name + ".xlsx"
		self.workbook = xlsxwriter.Workbook(name)
		worksheet = self.workbook.add_worksheet()
		for i in xrange(0,len(matrix)):
			row = matrix[i]
			for j in xrange(0,len(row)):
				if row[j] == -1:
					worksheet.write(i, j, '')
				else:
					worksheet.write(i, j, row[j])
				 



	def close(self):
		self.workbook.close()
