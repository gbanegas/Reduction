from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount

if __name__ == '__main__':

	pol = Polynomial('x^17 + x^8 + x^5 + x^3 + 1')
	red = Reduction()
	count = red.reduction(pol.coefs())
	print count
	
	
	