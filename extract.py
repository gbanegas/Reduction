import os
from collections import defaultdict,OrderedDict

import xlsxwriter


if __name__ == '__main__':
    f = open('saida_irred_pent_233.txt','r')
    pols = defaultdict(list)
    
    for line in f:
        splited = line.split(':')
        number = splited[1].replace('\n','')

        if pols[int(number)] == None:   
            pols[int(number)] = []

        spl = splited[0].replace(",","").replace("[","").replace("]","").split(' ')
        numbers = []
        for i in spl:
            numbers.append(int(i))

        
        pols[int(number)].append(numbers)

            
            #pols.sort(reverse=True)

    name = "result_1"
    name = name + ".xlsx"
    name = "" + name
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet("irredutiveis")
    worksheet.write(0,0, "XORs")
    worksheet.write(0,1, "m")
    worksheet.write(0,2, "a")
    worksheet.write(0,3, "b")
    worksheet.write(0,4, "c")
    worksheet.write(0,5, "d")
    row = 1
    colum = 0
    f = sorted(pols.keys())
    for i in f:
        for j in pols[i]:
            colum = 0
            worksheet.write(row,colum, i)
            colum = 1
            for num in j:
                worksheet.write(row,colum, num)
                colum = colum+1
            row = row + 1    

    workbook.close()
    
    
    #for i in pols:
    #    print str(i) + ":" +str(pols[i])
    

    