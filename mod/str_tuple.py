#!/usr/bin/env python3

"""
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word)) # adicionado uma tuple a uma lista, a cada interacao do for
t.sort(reverse=True) # ordena em ordem decrescente
res = list()
for length, word in t:# percorrer uma lista formada de tuple com dois elemetos por isso o for do tipo: for x, y in lista
    res.append(word)
    print length, word
print res

"""

# mapWords(str) → retorna uma lista de tupla, cada tupla na forma (intLength, word)
# getWords(list) → retorna uma lista de string in order da maior para a menor

def mapWords(valStr):
    return list( map(lambda x: (len(x), x), valStr.split()) )
    
def getWords(valList):
    copy = valList
    copy.sort(reverse=True)
    return list( map(lambda x: x[1], copy) )
    

if __name__ == '__main__':
    txt = 'but soft what light in yonder window breaks'
    myList = mapWords(txt)
    for length, word in myList:
        print('{0} {1}'.format(length, word))
    
    print()
    for i in getWords(myList):
        print(i)        

    

    
