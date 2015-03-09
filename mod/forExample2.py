#!/usr/bin/env python3

import sys

try: 
    from . import forExample1 as fore
except:
    import forExample1 as fore

"""
maior = None  
print 'Anters: ', maior

for intere in [3, 41, 12, 9, 74, 15]:
    if maior == None or intere > maior:
        maior = intere
    print "loop: ", intere, maior
print "maior numero no vetor: ", maior
"""
# main(list)→ int (return the maximum value on list)

def main(valList):
    return max(valList)

if __name__ == '__main__':
    val = sys.argv[1]
    try:
        val = fore.convertToList(val)
    except ValueError as err:
        print('Suport only int \n{0}'.format(err))
    maxVal = main(val)
    print('Max value: {0}'.format(maxVal))

    # run: $ python3 forExample2.py [1,2,3]

