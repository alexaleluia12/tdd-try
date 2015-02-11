#!/usr/bin/env python3

import re

"""
import re
c = 'X-DSPAM-Confidence: 4.8475'
c = c.rstrip()
if re.search('^X\S*: [0-9.]+', c) :
    print c

x = re.findall('^X\S*: ([0-9.]+)', c)  # pega apenas o numeros. Ou seja o que esta entre parenteses
if len(x) > 0 :
    print x

"""
# getStrFloat(string)→ list de string

def getStrFloat(valStr):
    regex = r'([0-9.]+\d+)' #  float numero (yyy.xxxx) um ou mais antes de '.' AND um ou mais depois de '.'  
    return re.findall(regex, valStr)

if __name__ == '__main__':
    strVal = 'X-DSPAM-Confidence: 4.8475'
    strVal = strVal.rstrip()
    if re.search('^X\S*: [0-9.]+', strVal) :
        print(strVal)

    for el in getStrFloat(strVal):
        print(el)
        
    # run: python3 reFloatNumber.py
    


