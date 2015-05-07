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
	save = open('result_pol_283_.txt','w')
	degree = 283
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

	
	fn = len(pols)/29
	inicio =  0 + fn
	prox_1 = inicio + fn
	prox_2 = prox_1 + fn
	prox_3 = prox_2 + fn
	prox_4 = prox_3 + fn
	prox_5 = prox_4 + fn
	prox_6 = prox_5 + fn
	prox_7 = prox_6 + fn
	prox_8 = prox_7 + fn
	prox_9 = prox_8 + fn
	prox_10 = prox_9 + fn
	prox_11 = prox_10 + fn
	prox_12 = prox_11 + fn
	prox_13 = prox_12 + fn
	prox_14 = prox_13 + fn
	prox_15 = prox_14 + fn
	prox_16 = prox_15 + fn
	prox_17 = prox_16 + fn
	prox_18 = prox_17 + fn
	prox_19 = prox_18 + fn
	prox_20 = prox_19 + fn
	prox_21 = prox_20 + fn
	prox_22 = prox_21 + fn
	prox_23 = prox_22 + fn
	prox_24 = prox_23 + fn
	prox_25 = prox_24 + fn
	prox_26 = prox_25 + fn
	prox_27 = prox_26 + fn
	prox_28 = prox_27 + fn

	print str(inicio) + " : " + str(prox_1) + " : " + str(prox_2) + " : " + str(prox_3) + " : " + str(prox_4) + " : " + str(prox_5) + " : "+ str(prox_6) + " : " + str(prox_7) + " : " + str(prox_8) + " : " + str(prox_9) + " : " + str(prox_10) + " : " + str(prox_11) + " : " + str(prox_12) + " : " + str(prox_13) + " : " + str(prox_14) + " : " + str(prox_15) + " : "+ str(prox_16) + " : " + str(prox_17) + " : " + str(prox_18) + " : " + str(prox_19) + " : " + str(prox_20) + " : " + str(prox_21) + " : " + str(prox_22) + " : " + str(prox_23) + " : " + str(prox_24) + " : " + str(prox_25) + " : " + str(prox_26) + " : " + str(prox_27) + " : " + str(prox_28) 

	t1 = ThreadCount(1,lockScreen, lock, pols[0:inicio], save)
	t2 = ThreadCount(2,lockScreen, lock, pols[inicio+1:prox_1], save)
	t3 = ThreadCount(3,lockScreen, lock, pols[prox_1+1:prox_2], save)
	t4 = ThreadCount(4,lockScreen, lock, pols[prox_2+1:prox_3], save)
	t5 = ThreadCount(5,lockScreen, lock, pols[prox_3+1:prox_4], save)
	t6 = ThreadCount(6,lockScreen, lock, pols[prox_4+1:prox_5], save)
	t7 = ThreadCount(7,lockScreen, lock, pols[prox_5+1:prox_6], save)
	t8 = ThreadCount(8,lockScreen, lock, pols[prox_6+1:prox_7], save)
	t9 = ThreadCount(9,lockScreen, lock, pols[prox_7+1:prox_8], save)
	t10 = ThreadCount(10,lockScreen, lock, pols[prox_8+1:prox_9], save)
	t11 = ThreadCount(11,lockScreen, lock, pols[prox_9+1:prox_10], save)
	t12 = ThreadCount(12,lockScreen, lock, pols[prox_10+1:prox_11], save)

	t13 = ThreadCount(13,lockScreen, lock, pols[prox_11+1:prox_12], save)
	t14 = ThreadCount(14,lockScreen, lock, pols[prox_12+1:prox_13], save)
	t15 = ThreadCount(15,lockScreen, lock, pols[prox_13+1:prox_14], save)
	t16 = ThreadCount(16,lockScreen, lock, pols[prox_14+1:prox_15], save)
	t17 = ThreadCount(17,lockScreen, lock, pols[prox_15+1:prox_16], save)
	t18 = ThreadCount(18,lockScreen, lock, pols[prox_16+1:prox_17], save)
	t19 = ThreadCount(19,lockScreen, lock, pols[prox_17+1:prox_18], save)
	t20 = ThreadCount(20,lockScreen, lock, pols[prox_18+1:prox_19], save)
	t21 = ThreadCount(21,lockScreen, lock, pols[prox_19+1:prox_20], save)
	t22 = ThreadCount(22,lockScreen, lock, pols[prox_20+1:prox_21], save)
	t23 = ThreadCount(23,lockScreen, lock, pols[prox_21+1:prox_22], save)
	t24 = ThreadCount(24,lockScreen, lock, pols[prox_22+1:prox_23], save)
	t25 = ThreadCount(25,lockScreen, lock, pols[prox_23+1:prox_24], save)
	t26 = ThreadCount(26,lockScreen, lock, pols[prox_24+1:prox_25], save)
	t27 = ThreadCount(27,lockScreen, lock, pols[prox_25+1:prox_26], save)
	t28 = ThreadCount(28,lockScreen, lock, pols[prox_26+1:prox_27], save)
	t29 = ThreadCount(29,lockScreen, lock, pols[prox_27+1:prox_28], save)
	t30 = ThreadCount(30,lockScreen, lock, pols[prox_28+1:len(pols)-1], save)


	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t5.start()
	t6.start()
	t7.start()
	t8.start()
	t9.start()
	t10.start()
	t11.start()
	t12.start()
	t13.start()
	t14.start()
	t15.start()
	t16.start()
	t17.start()
	t18.start()
	t19.start()
	t20.start()
	t21.start()
	t22.start()
	t23.start()
	t24.start()
	t25.start()
	t26.start()
	t27.start()
	t28.start()
	t29.start()
	t30.start()
	#t1.join()
	#t2.join()
	#t3.join()
	#t4.join()
	#t5.join()
	#t6.join()
	if (not (t1.isAlive() and t2.isAlive() and t3.isAlive() and t4.isAlive() and t5.isAlive() and t6.isAlive()  and t7.isAlive() and t8.isAlive() and t9.isAlive() and t10.isAlive() and t11.isAlive() and t12.isAlive() and t13.isAlive() and t14.isAlive() and t15.isAlive() and t16.isAlive() and t17.isAlive() and t18.isAlive()  and t19.isAlive() and t20.isAlive() and t21.isAlive() and t22.isAlive() and t23.isAlive() and t24.isAlive() and t25.isAlive() and t26.isAlive() and t27.isAlive() and t28.isAlive() and t29.isAlive() and t30.isAlive())):
		print "All threads die...."
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

        