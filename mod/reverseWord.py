#!/usr/bin/env python3

import re

"""
def fu_inPalavra():
    while True:
        aux_palavra = raw_input('digite uma palavra: ')
        if '0' in aux_palavra or '1' in aux_palavra or '2' in aux_palavra or '3' in aux_palavra or '4' in aux_palavra or '5' in aux_palavra or '6' in aux_palavra or '7' in aux_palavra or '8' in aux_palavra or '9' in aux_palavra or aux_palavra == '':
            continue          # o if decima ve se tem um numero ou foi digido um enter
        return aux_palavra
    
        
palavra = fu_inPalavra()
i = len(palavra)
pa_invertida = list()
while i > 0:
    i = i - 1
    pa_invertida.append(palavra[i])

delimiter = ''
invertida = delimiter.join(pa_invertida)  # vai juntar os elementos da lista para formar uma string
print invertida
    
"""
# checkWord(string)→ string, se ela nao tiver nenhum numero e tamanho maior que zero Caso contrario retorna False
# invert(string)→ string invertida

def checkWord(valStr):
    regex = r'\d+'
    if len(valStr) == 0:
        return False
    if re.search(regex, valStr):
        return False
    return valStr
    
def invert(valStr):
    return valStr[::-1]
    
if __name__ == '__main__':
    def again():
        while True:
            userEnter = input('Type any word: ')
            if not checkWord(userEnter):
                continue
            return userEnter
    
    valStr = again()
    print(invert(valStr))

    
    # run: $ python3 reverseWord.py

        
