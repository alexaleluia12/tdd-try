#!/usr/bin/env python3

import sys

"""
cont = 0
soma = 0
print 'quantidade de elementos no vetor: \n'
for interaVar in [3, 41, 12, 9, 74, 15]:
    cont  = cont + 1
    soma = soma + interaVar
    
print 'cont: ', cont
print "\nSoma dos elemetos: ", soma
"""
# main(list) → dict
# counterEl(list) → int
# counter(list)→ int 

def counterEl(valList):
    return len(valList)

def counter(valList):
    return sum(valList)

def main(valList):
    return {'amount': counterEl(valList), 'count': counter(valList)}

def convertToList(valStr):
    strMap = str.maketrans("'[]", '   ')# in py2 string.maketrans(..)
    innerList = valStr.translate(strMap).strip().split(',')
    return list(map(lambda x: int(x), innerList)) 
    # map in python3 work different to python2 (return a generator)


if __name__ == '__main__':
    val = sys.argv[1]
    try:
        val = convertToList(val)
    except ValueError as verr:
        print('Only suport int \n{0}'.format(verr))

    msg = "Amount of elements: {amount}\nSum of all: {count}"
    print(msg.format(**main(val)))
    # run: python3 forExample1.py [1,2,3]

