import os
from collections import defaultdict

import xlsxwriter


if __name__ == '__main__':
    f = open('saida_irre_19.txt','r')
    pols = defaultdict(list)
    
    for line in f:
        splited = line.split(':')
        number = splited[1].replace('\n','')

        if pols[int(number)] == None:
            pols[int(number)] = []
        pols[int(number)].append(splited[0])
        
            
            #pols.sort(reverse=True)

    name = "result_1"
    name = name + ".xlsx"
    name = "" + name
    workbook = xlsxwriter.Workbook(name)
    worksheet = workbook.add_worksheet("irredutiveis")
    row = 0
    colum = 0
    for i in pols:
        colum = 1
        worksheet.write(row,colum, i)
        colum = 2
        for j in pols[i]:
            worksheet.write(row,colum, j)
            colum = colum+1
        row = row + 1    

    workbook.close()
    
    
    #for i in pols:
    #    print str(i) + ":" +str(pols[i])
    

    