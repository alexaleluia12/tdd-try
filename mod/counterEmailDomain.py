#!/usr/bin/env python3

import os

try:
    import axCounter
except:
    from . import axCounter    

"""
fi_email = open('mbox-short.txt', 'r')
di_localEmail = dict()
di_local = dict()
cont = 0
for i in fi_email:
    i = i.split()
    if len(i) == 0:
        continue
   
    if i[0] == 'From':
        if i[1] not in di_localEmail:
            di_localEmail[i[1]] = 1
        else:
            di_localEmail[i[1]] = di_localEmail[i[1]] + 1

fi_email.close()
indiceAroba = 1
aux = ''
for k in di_localEmail:
    indiceAroba = k.find('@')
    aux = k[indiceAroba +1 : ]
    if aux not in di_local:
        di_local[aux] = di_localEmail[k]

    else:
        di_local[aux] = di_local[aux] + di_localEmail[k]

print di_local

"""
# getAllEmailDomain(iterable)→ retorn um generator, onde cada elemento 
#    contem apenas o dominio do email in relacao ao iterable
#    [dois@gmail.com] -> [gmail.com]

def getAllEmailDomain(iterable):
    for el in iterable:
        aroba = el.find('@')
        assert aroba != -1, "the elemento in iterable showd have any '@' "
        yield el[aroba + 1: ]
    
if __name__ == '__main__':    
    FILE = os.path.join('static', 'mbox-short.txt')
    regexFrom = r'\bFrom .+' # 'From ' seguido de qualquer coisa
    with open(FILE) as f:
        fromContent = axCounter.iterableN(f, regexFrom)

    emails = axCounter.getAllPosionedElement(fromContent, 1)
    emailDomains = getAllEmailDomain(emails)
    contedDomain = axCounter.mapCounter(emailDomains)
    print(contedDomain)

