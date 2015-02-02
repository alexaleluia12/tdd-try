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

# validarEntrada(val, type,[intervalo])→ boll (intervalo na forma (inicio, fim) inclusivo)

# getTabuada(val, intervalo)→ list (lista de tupla onde cada elemento tem forma '(a, b, c)')
# intervalo -> inclusivo forma: '(inicio, fim)'

def validaEntrada(val, vtype, intervalo=None):
    if type(str) != type(vtype):
        raise( TypeError("{0} invalid type 'try: int or str'".format(repr(vtype))) )
    valBoll = type(val) == vtype
    if intervalo == None:
        return valBoll
    assert type(val) == type(intervalo[0]) == type(intervalo[1]), "the interval need to be the same type"
    intervaloBoll = val >= intervalo[0] and val <= intervalo[1]
    return valBoll and intervaloBoll    
        
    
def getTabuada(val, intervalo):
    lt = []
    for i in range(intervalo[0], intervalo[1] + 1):
        lt.append((val, i, i * val))
    return lt
    
if __name__ == '__main__':
    val = int(sys.argv[1])
    if validaEntrada(val, int, (1, 10)):
        for el in getTabuada(val, (1, 10)):
            print(" {0} x {1} = {2}".format(*el))

    # run: python3 tabuada.py 4
  
     
