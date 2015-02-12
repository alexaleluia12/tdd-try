#!/usr/bin/env python3

import sys

# TODO
# 

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


# countLine(fileName)→ int (numero de linha de arquivo), -1 se o arquivo nao foi encontrado

def countLine(fileName):
    count = 0
    try:
        with open(fileName) as f:
            for line in f:
                count += 1
        return count
    except FileNotFoundError as err:
        return -1 
        

if __name__ == '__main__':
    fileName = sys.argv[1]
    print("> {0}".format(countLine(fileName)))
    
    # run: python3 linhasArquivo.py pathFile

        
