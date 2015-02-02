#!/usr/bin/env python3

import sys


try: 
    from . import forExample1 as fore
except:
    import forExample1 as fore
    
# eu nao gosto desse estilo de import mas foi o unico que funcionou
# tanto no test quanto na excecao narmal do arquivo    
"""
maior = None  
print 'Anters: ', maior

for intere in [3, 41, 12, 9, 74, 15]:
    if maior == None or intere > maior:
        maior = intere
    print "loop: ", intere, maior
print "maior numero no vetor: ", maior	
"""
# main(list)→ int (retorna o maior elemento da list)

def main(valList):
    return max(valList)
    
if __name__ == '__main__':
	val = sys.argv[1]
	try:
	    val = fore.convertToList(val)
	except ValueError as err:
	    print('Suport only int \n{0}'.format(err))
	maxVal = main(val)
	print('Max value: {}'.format(maxVal))
	
	# run: $ python3 forExample2.py [1,2,3]
	

    
