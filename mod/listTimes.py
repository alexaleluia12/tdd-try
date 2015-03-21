#!/usr/bin/env python3

import sys
import pprint

from mod import forExample1 as fore

"""
vetor = [2, 4, 6]
for i in range(len(vetor)):
    vetor[i] = vetor[i] * 5
print vetor
"""

# timesElements(valList, intValue)
#    return a list where each element is times by `intValue`
#    (`valList` is list type)
#    (`intValue` is int type)

def timesElements(vIter, val): 
    return list(map(lambda x: x * val, vIter))

if __name__ == '__main__':
    val = sys.argv[1]
    factor = int(sys.argv[2])
    val = fore.convertToList(val)
    print("{0} * {1} = ".format(val, factor), end='')
    pprint.pprint(timesElements(val, factor))

    # run: $ python3 listTimes.py [3,4,5] 5

