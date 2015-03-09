#!/usr/bin/env python3

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

def mapWordCount(valStr):
    """Return a dict 
    
    Where each key is an string in 'valStr' and value is the times the
    same string happen.
    'valStr' is str type.
    """
    dictRet = {}
    tabTrans = str.maketrans('().:=_,;?/!', ' '*11)
    lst = valStr.translate(tabTrans).split()
    for e in lst:
        dictRet[e] = dictRet.get(e, 0) + 1
    return dictRet

def getWin(valDict):
    """ 
    Return the tuple (key, value) from valDict where the value
    is the maximum value found in valDict. 
    And yes the key is the respective key where value happen.
    """
    assert bool(valDict) == True, "The dict is empty"
    maxValue = max(valDict.values())
    for k, v in valDict.items():
        if v == maxValue:
            return (k, v)


def main(strFileName):
    content = open(strFileName).read()
    val = mapWordCount(content)
    return getWin(val)


if __name__ == "__main__":
   
    print(main(sys.argv[1]))
    # run: python3 secPalavras.py pathYourFile

