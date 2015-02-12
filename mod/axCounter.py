#!/usr/bin/env python3

import re
import collections

# iterableN(iterable, regex)→ retorna lista onde cada elemento eh tirado do 
#    iterable baseado na regex
#    (regex e uma expresao regula parecido: r'[1-7]+')
#    (iterable deve ser uma lista de string)

# mapCounter(iterable)→ retorna dict parecido com: {'Fri': 89, 'Thu': 90,...}
#    baseado a quantidade de 'Fri' que acontece em iterable, 
#    (interable de ser parecido com ['v1', 'v1', 'v2', ...])

# getAllPosionedElement(iterable, indice)→ retorna um generator onde cada
#    elemento eh tirado entre os elementos de iterable baseado no indice
#    (iterable: he iterable composto de strings padronizadas)
#    (indece: int entre 0 e len(iterable[0].split()))


def iterableN(iterable, regex):
    lst = []
    for el in iterable:
        match = re.search(regex, el)
        if match:
            lst.append(el)
    return lst
    
def mapCounter(iterable):
    return dict(collections.Counter(iterable))

def getAllPosionedElement(iterable, indece):
    for el in iterable:
        yield el.split()[indece]

if __name__ == '__main__':
    pass

    
        
