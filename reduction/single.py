from reduction import Reduction
from polynomial import Polynomial
#gc.collect()  # don't care about stuff that would be garbage collected properly
#from guppy import hpy
#hp = hpy()
#before = hp.heap()
import os

if __name__ == '__main__':

    pol = Polynomial('x^5 + x^3 + 1')
    #pol2 = Polynomial('x^283 + x^142 + x^70 + x + 1')
    #pol3 = Polynomial('x^163 + x^82 + x^6 + x + 1')
    red = Reduction()
    l = []
    count = red.reduction(pol.coefs())
    l.append(count)
    print count
    #count = red.reduction(pol2.coefs())
    #l.append(count)
    #print count
    #count = red.reduction(pol3.coefs())
    #l.append(count)
    print count

    print l
