'''
Created on 10 Sep 2014

@author: gustavo
'''
from reduction import Reduction
from polynomial import Polynomial
from threadc import ThreadCount
import os
import threading
import sys, getopt

def recoverfile(saved, readed):
    if not os.path.exists(saved):
        return True, []
    f = open(saved,'r')
    if(not os.stat(saved).st_size==0):
        pols = []
        pols_done = []
        for line in readed:
            pol = Polynomial(line) 
            pols.append(pol)
        for line in f:
            line = line.replace("[","")
            line = line.replace("]","")
            spl = line.split(',')
            p = ""
            for i in xrange(0,len(spl)-1):
                p = p + " + x^" + str(spl[i].replace(" ","")) 
            p = p + " + 1"
            p = p.replace("+","",1)
            #print p
            pol_ = Polynomial(p) 
            pols_done.append(pol_)
        
        pols_set = set(pols)
        pols_set_done = set(pols_done)
        result = pols_set - pols_set_done
        return False, list(result)
    else:
        return True, []


def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print 'main.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
      for opt, arg in opts:
        if opt == '-h':
            print 'main.py -i <inputfile> -o <outputfile> '
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
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile
   lock = threading.Lock()
   lockScreen = threading.Lock()
   files = [inputfile]
   for fileName in files:
    save = outputfile
    f = open(fileName,'r')
    read, pols = recoverfile(save, f)
    if read:
        for line in f:
            pol = Polynomial(line)
            pols.append(pol)
        
    print len(pols)
    threads = []
    i = 0
    j = 1
    print "starting...."
    for temp in range(0, len(pols)):
        if (j > len(pols)):
            j = len(pols)
        thread = ThreadCount(temp,lockScreen, lock, pols[i:j], save)
        i = j+1
        j += 1
        threads.append(thread)
    for thread in threads:
        thread.start()
    for current in threads:
        current.join()

if __name__ == '__main__':
    main(sys.argv[1:])

    






