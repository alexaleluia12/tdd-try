#!/usr/bin/env python3

import sys
import pprint

try: 
    from . import forExample1 as fore
except:
    import forExample1 as fore


"""
vetor = [2, 4, 6]
for i in range(len(vetor)):
    vetor[i] = vetor[i] * 5
print vetor
    
"""

# timesEl(list, intValue)
#    return a list where each element was times by intValue


def timesEl(vIter, val): 
    return list(map(lambda x: x * val, vIter))
    
if __name__ == '__main__':
    val, fator = sys.argv[1], int(sys.argv[2])
    val = fore.convertToList(val)
    print("{0} * {1} = ".format(val, fator), end='')
    pprint.pprint(timesEl(val, fator))
    
    # run: $ python3 listTimes.py [3,4,5] 5




    
