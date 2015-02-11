#!/usr/bin/env python3

import collections
try:
    import howManyFrom as hmf
except:
    from . import howManyFrom as hmf

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
# mapDayWeekCount(iterable)→ dict parecido com: {'Fri': 89, 'Thu': 90,...}, 
#    interable de ser parecido com ['Thu', 'Thu', 'Fri']

# getWeekDays(interable)→ generator, onde cada elementos e um dia da 
#    semana (pode haver repetido)

def mapDayWeekCount(iterable):
    return dict(collections.Counter(iterable))
    
def getWeekDays(iterable):
    for i in iterable:
        yield i.split()[2]
    
if __name__ == '__main__':
    FILE = 'static/mbox-short.txt'
    with open(FILE) as f:
        lstContent = hmf.iterableFrom(f)
            
    weekdays = getWeekDays(lstContent)
    daysCounts = mapDayWeekCount(weekdays)
    print(daysCounts)
        

