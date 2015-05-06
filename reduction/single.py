from reduction import Reduction
from polynomial import Polynomial
#gc.collect()  # don't care about stuff that would be garbage collected properly
#from guppy import hpy
#hp = hpy()
#before = hp.heap()
import os

if __name__ == '__main__':

    pol = Polynomial('x^200 + x^10 + x^5 + x^1 + 1')
    red = Reduction()
    count = red.reduction(pol.coefs())
    print count
