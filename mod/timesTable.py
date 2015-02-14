#!/usr/bin/env python3

import sys

"""
aux = 1
while aux == 1:
    entra = raw_input("Digite um numero interio entre 1 e 10: ")
    try:
        if type(int(entra)) == int:
            entraValida = int(entra)
            break
        
    except:
        print "entrada invalida\n"

cont = 1
for i in range(10):
    
    i = i + 1
    print "%d  x %d : %d" % (entraValida, i, i*entraValida)
    
"""

# sanityEnter(val, type[,interval])
#    return a boll value True if right False otherwise 
#    (val value that we want check)
#    (type be class built-in python like str, int, dict)
#    (interval like this (begin, end) inclusive integers)

# getTimesTab(val, interval)→ 
#    return a generator where each is like this (a, b, c)
#    ( interval -> inclusive like: (begin, end) )

def sanityEnter(val, vtype, inter=None):
    if type(str) != type(vtype):#
        raise( TypeError("{0} invalid type 'try: int or str'".format(repr(vtype))) )
    valBoll = type(val) == vtype
    if inter == None:
        return valBoll
    assert type(val) == type(inter[0]) == type(inter[1]), "the interval need to be the same type"
    intervalBoll = val >= inter[0] and val <= inter[1]
    return valBoll and intervalBoll    
        
    
def getTimesTab(val, interval):    
    for i in range(interval[0], interval[1] + 1):
        yield (val, i, i * val)
    
    
if __name__ == '__main__':
    val = int(sys.argv[1])
    if sanityEnter(val, int, (1, 10)):
        for el in getTimesTab(val, (1, 10)):
            print(" {0} x {1} = {2}".format(*el))

    # run: python3 tabuada.py number
  
     
