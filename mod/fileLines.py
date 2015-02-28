#!/usr/bin/env python3

import sys

"""
entradaUsuarioArquivo = raw_input("Digite o nome do arquivo: ")
# foi secessario contatenar strigs para ter a entrada no formato de caminhos.
try:
    
    arqui = open(caminhoArquivo+entradaUsuarioArquivo+'.txt', 'r')
except:
    print "Arquivo nao existe: ", entradaUsuarioArquivo
    exit()
cont = 0
for line in arqui:
    cont = cont + 1
print "quantidade de linhas: ", cont
arqui.close() 
"""

# countLine(iterableFile)
#    return the number of lines in iterableFile

def countLine(iterableFile):
    return len(list(iterableFile))
        
        
if __name__ == '__main__':
    fileName = sys.argv[1]
    with open(fileName) as f:
        numberLines = countLine(f) # the f (file object) suport interation
    print("{0}> {1}".format(fileName, numberLines))
    
    # run: python3 fileLines.py pathFile

