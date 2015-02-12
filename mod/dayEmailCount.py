#!/usr/bin/env python3

import collections
import os
try:
    from . import axCounter
except:
    import axCounter 

"""
fi_email = open('mbox-short.txt', 'r')
di_diasSemana = dict()
cont = 0
for i in fi_email:
    i = i.split()
    if len(i) == 0:
        continue
   
    if i[0] == 'From':
        if i[2] not in di_diasSemana:
            di_diasSemana[i[2]] = 1
        else:
            di_diasSemana[i[2]] = di_diasSemana[i[2]] + 1

print di_diasSemana    
"""
# the axCounter module handle with all this thing
 
if __name__ == '__main__':
    FILE = os.path.join('static', 'mbox-short.txt')
    regex = r'\bFrom .+' # comeca com 'From ' e termina com qualquer coisa
    with open(FILE) as f:
        lstContent = axCounter.iterableN(f, regex)
            
    weekdays = axCounter.getAllPosionedElement(lstContent, 2)
    daysCounts = axCounter.mapCounter(weekdays)
    print(daysCounts)
        

