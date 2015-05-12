from reduction import Reduction
from polynomial import Polynomial
#gc.collect()  # don't care about stuff that would be garbage collected properly
#from guppy import hpy
#hp = hpy()
#before = hp.heap()
import os
from collections import defaultdict

if __name__ == '__main__':

    pol1 = Polynomial('x^233 + x^74 + 1')
    pol = Polynomial('x^233 + x^159 + 1')
    pol2 = Polynomial('x^409 + x^87 + 1')
    pol3 = Polynomial('x^409 + x^322 + 1')
    pol4 = Polynomial('x^6 + x^3 + 1')
    pol5 = Polynomial('x^18 + x^9 + 1')
    pol6 = Polynomial('x^20 + x^15 + x^10 + x^5 + 1')
    pol7 = Polynomial('x^100 + x^75 + x^50 + x^25 + 1')
    pol8 = Polynomial('x^42 + x^35 + x^28 + x^21 + x^14 + x^7 + 1')
    pol9 = Polynomial('x^294 + x^245 + x^196 + x^147 + x^98 + x^49 + 1')
    #pol10 = Polynomial('x^20 + x^15 + x^10 + x^5 + 1')
    l = []
    l.append(pol1)
    l.append(pol)
    l.append(pol2)
    l.append(pol3)
    l.append(pol4)
    l.append(pol5)
    l.append(pol6)
    l.append(pol7)
    l.append(pol8)
    l.append(pol9)
    #l.append(pol10)
    result = defaultdict()

    red = Reduction()
    for pol in l:
        count = red.reduction(pol.coefs())
        result[str(pol.coefs())] = count
    #l.append(count)
    print result
    #print count
    #count = red.reduction(pol2.coefs())
    #l.append(count)
    #print count
    #count = red.reduction(pol3.coefs())
    #l.append(count)
    #print count
    #print l
