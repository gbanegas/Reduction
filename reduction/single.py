from reduction import Reduction
from polynomial import Polynomial
#gc.collect()  # don't care about stuff that would be garbage collected properly
#from guppy import hpy
#hp = hpy()
#before = hp.heap()
import os

if __name__ == '__main__':
    degree = 571
    directory = str(degree)
    #if not os.path.exists(directory):
    #    os.makedirs(directory)
    #f = open('pent_list_' + str(degree) + '.txt','r')
    #toSave = directory + '/pent_result_' + str(degree) + '.txt'
    ##save = open(toSave,'w')
    #pols = []
    #for line in f:
    #    pol = Polynomial(line)
    #    pols.append(pol)

    #for i in pols:
    #    red = Reduction()
     #   count = red.reduction(i.coefs())
     #   del red
     #   result = str(i.coefs()) + " : " + str(count) + "\n"
     #   save.write(result)
     #   print result

    #save.close()
    pol = Polynomial('x^571 + x^10 + x^5 + x^2 + 1')
    red = Reduction()
    count = red.reduction(pol.coefs())
    print count

    #print count
#    after = hp.heap()
#    leftover = after - before
#    import pdb; pdb.set_trace()
