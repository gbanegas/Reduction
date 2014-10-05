import os
from collections import OrderedDict

if __name__ == '__main__':
    f = open('result_283.txt','r')
    pols = {}
    for line in f:
        if ':' in line:
            splited = line.split(':')
            number = splited[1].replace('\n','')
            pols[int(number)] = splited[0]
    
    ordered = OrderedDict(sorted(pols.items(), key=lambda t: t[0]))
    print ordered