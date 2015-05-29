from reduction import Reduction
from polynomial import Polynomial
import os
from collections import defaultdict
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'single.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'single.py -i <inputfile> -o <outputfile> '
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    
    try:
        fi = open(inputfile,"r")
        fl = open(outputfile,"a")
    except IOError:
        print 'main.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    l = []
    for i in fi:
        p = Polynomial(i)
        l.append(p)
    result = defaultdict(list)

    red = Reduction()
    for pol in l:
        red = Reduction()
        if len(pol.coefs()) > 1:
            count = red.reduction(pol.coefs())
            result =  str(pol.coefs()) + ":" + str(count)
            print result
            fl.write(result + "\n")



if __name__ == '__main__':
    main(sys.argv[1:])
   
   