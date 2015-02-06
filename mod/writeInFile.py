#!/usr/bin/env python3

import sys

"""
novoArq = open('pyTexto.txt', 'a')
line2 = 'Python is awesome \n'
novoArq.write(line2)  # vai escrever na linha 1
novoArq.close()    
"""
# write(connFile, strContent) → Boll

def write(connFile, strContent):
    amountWriting = connFile.write(strContent)
    return amountWriting > 0
    
if __name__ == '__main__':
    pass

      
