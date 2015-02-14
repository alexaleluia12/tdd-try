#!/usr/bin/env python3


try:
    from . import myErrorException as myerr
except:
    import myErrorException as myerr
    
import sys


"""
name = raw_input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount
	
"""
# getFile(str)→ string, 

# mapWordCount(str)→ dict

# getWin(dict)→ tuple

# main(str)→ str

def getFile(filename):
    with open(filename, 'r') as f:
        content = f.read()
        if len(content) == 0:
            raise myerr.FileEmpty('the file is empty: ' + filename )
        
        return content
    
def mapWordCount(valStr):
    dictRet = {}
    tabTrans = str.maketrans('().:=_,', ' '*7)
    lst = valStr.translate(tabTrans).split()
    for e in lst:
        dictRet[e] = dictRet.get(e, 0) + 1
    return dictRet
    
def getWin(valDict):
    maxValue = max(valDict.values())
    for e in valDict.items():
        k, v = e
        if v == maxValue:
            return (k, v)
          

def main(strFileName):
    val = mapWordCount(getFile(strFileName))
    return getWin(val)
              

if __name__ == "__main__":
   
    print(main(sys.argv[1]))
    # run: python3 secPalavras.py pathYourFile

