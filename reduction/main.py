'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os
import threading


#import threading
if __name__ == '__main__':
	lock = threading.Lock()
	lockScreen = threading.Lock()
	save = open('result_pol_test_.txt','w')
	degree = 163
	#directory = str(degree)
	# if not os.path.exists(directory):
	# 	os.makedirs(directory)
	f = open('pol_' + str(degree) + '_.txt','r')
	# save = open('result_' + str(degree) + '.txt','w')
	#f = ["x^63 + x^14 + x^7 + x^4 + 1", "x^63 + x^15 + x^7 + x^4 + 1", "x^63 + x^16 + x^7 + x^4 + 1" , "x^63 + x^17 + x^7 + x^4 + 1" ]
	pols = []
	for line in f:
		pol = Polynomial(line)
		pols.append(pol)
	print len(pols)

	
	fn = len(pols)/6
	inicio =  0 + fn
	prox_1 = inicio + fn
	prox_2 = prox_1 + fn
	prox_3 = prox_2 + fn
	prox_4 = prox_3 + fn
	prox_5 = prox_4 + fn
	print str(inicio) + " : " + str(prox_1) + " : " + str(prox_2) + " : " + str(prox_3) + " : " + str(prox_4) + " : " + str(prox_5) 

	t1 = ThreadCount(1,lockScreen, lock, pols[0:inicio], save)
	t2 = ThreadCount(2,lockScreen, lock, pols[inicio+1:prox_1], save)
	t3 = ThreadCount(3,lockScreen, lock, pols[prox_1+1:prox_2], save)
	t4 = ThreadCount(4,lockScreen, lock, pols[prox_2+1:prox_3], save)
	t5 = ThreadCount(5,lockScreen, lock, pols[prox_3+1:prox_4], save)
	t6 = ThreadCount(6,lockScreen, lock, pols[prox_4:len(pols)-1], save)

	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
	t5.join()
	t6.join()
	if (not (t1.isAlive() and t2.isAlive() and t3.isAlive() and t4.isAlive() and t5.isAlive() and t6.isAlive())):
		save.close();
	#f = open('pol_163_.txt','r')
	
	#pols = []
	#for line in f:
	#	pol = Polynomial(line)
#		pols.append(pol)
	#redu = Reduction()
	#result = redu.reduction([150,10,5,1,0])
	#print result
	#for pol in pols:
	#	print pol.coefs()
	#	valor = redu.reduction(pol.coefs())
	#	save.write(str(pol.coefs()) + ":" + str(valor) + "\n")

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

        