'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os


#import threading
if __name__ == '__main__':
	f = open('pol_283_.txt','r')
	save = open('result_pol_283_.txt','w')
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)
	redu = Reduction()
	for pol in pols:
		print pol.coefs()
		valor = redu.reduction(pol.coefs())
		save.write(str(pol.coefs()) + ":" + str(valor) + "\n")
	
	# f = open('result_nova_familia.txt','r')
	# for line in f:
	# 	line = line.replace("[", "")
	# 	line = line.replace("]", "")
	# 	line = line.replace(":", " ")
	# 	line = line.split()
	# 	degree = line[0].replace(",", "")
	# 	value = line[len(line)-1]
	# 	value_expected = 4*int(degree)-4 
	# 	polinomio = line[0] + " " + line[1] + " " + line[2] + " " + line[3] + " " + line[4] + ""
	# 	string = "Pol: " + polinomio + " - Xors: "  + value	+ " Expected by Wu: " + str(value_expected);
	# 	if int(value) < value_expected:
	# 		print string + " OK!"
	# 	else:
	# 		print string + " FAIL!"

        # for line in f:
        # 	pol = Polynomial(line)
        # 	pols.append(pol)

        