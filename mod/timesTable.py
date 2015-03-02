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

# sanityEnter(val, vtype[,interval])
#    return a boll value True if right False otherwise 
#    if interval is given it also check whether val is between interval
#    (val value that we want check)
#    (vtype be class built-in python like str, int, dict)
#    (interval like this (begin, end) inclusive integers)

# getTimesTab(val, interval=(1, 10))
#    return a generator where each is like this (a, b, c)
#    ( interval -> inclusive like: (begin, end) )

def sanityEnter(val, vtype, interval=None):
    if type(str) != type(vtype):#
        raise(TypeError("{0} invalid type 'try: \
              int or str'".format(repr(vtype))))
    valBool = type(val) == vtype
    if interval == None:
        return valBool
    assert type(val) == type(interval[0]) == type(interval[1]), "the \
                                    interval need to be the same type"
                           
    intervalBool = val >= interval[0] and val <= interval[1]
    return valBool and intervalBool    
        
    
def getTimesTab(val, interval=(1, 10)):    
    for i in range(interval[0], interval[1] + 1):
        yield (val, i, i * val)
    
    
if __name__ == '__main__':
    val = int(sys.argv[1])
    if sanityEnter(val, int, (1, 10)):
        for el in getTimesTab(val):
            print(" {0} x {1} = {2}".format(*el))

    # run: python3 timesTable.py number
  
