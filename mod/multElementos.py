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

# multElementos(inter, val)→ list (retorna uma lista onde cada elemento foi multiplicado por val)

def multElementos(vInter, val): 
    return list(map(lambda x: x * val, vInter))
    
if __name__ == '__main__':
    val, fator = sys.argv[1], int(sys.argv[2])
    val = fore.convertToList(val)
    print("{0} * {1} = ".format(val, fator))
    pprint.pprint(multElementos(val, fator))
    
    # run: $ python3 multElementos.py [3,4,5] 5




    
