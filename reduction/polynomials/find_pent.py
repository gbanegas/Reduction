'''
Created on 10 Sep 2015

@author: gustavo
'''



#import threading
if __name__ == '__main__':
	f = open("tri_pent.txt", "r")
	pentanomials = open("pent.txt", "a")
	pentanomials.write("Degrees: \n")
	for line in f:
		spl = line.split(',')
		if(len(spl) > 2):
			st = str(spl[0]) + "\n"
			pentanomials.write(st)
	pentanomials.close()