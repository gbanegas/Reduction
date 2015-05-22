import os
from collections import OrderedDict

if __name__ == '__main__':
    f = open('result_pol_571.txt','r')
    pols = {}
    for line in f:
        if ':' in line:
            splited = line.split(':')
            number = splited[1].replace('\n','')
            pols[int(number)] = splited[0]
            #pols.sort(reverse=True)
    
    ordered = OrderedDict(sorted(pols.items(), key=lambda t: t[0]))
    pol_list =[]
    

    print pol_list