from reduction import Reduction
from polynomial import Polynomial

if __name__ == '__main__':

	pol = Polynomial('x^8 + x^7 + x^6 + x^3 + 1')
	red = Reduction()
	count = red.reduction(pol.coefs())
	print count
	
