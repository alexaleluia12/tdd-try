#!/usr/bin/env python3

import re
import os

"""
f_CurtoBox = open('static/mbox-short.txt')
cont = 0
li_email = list()
for i in f_CurtoBox:
    
    k = i.split()
    if len(k) == 0: 
        continue
    
    if k[0] == 'From':
        li_email.append(k[1])
        cont = cont + 1
   

f_CurtoBox.close()
print 'Quantidade de Fron : ', cont
for k in li_email:
    print k    
"""

# iterableFrom(interable)→ list, 
#   where each element is like
#   'From rjlowe@iupui.edu Fri Jan  4 15:46:24 2008'

def iterableFrom(iterable):
    regex = r'\bFrom .+'
    lst = []
    for el in iterable:
        match = re.search(regex, el)
        if match:
            lst.append(match.string)
    return lst        

def amount(lst):
    return len(lst)
    
if __name__ == '__main__':
    FILE = os.path.join('static', 'mbox-short.txt')
    with open(FILE) as f:
        lstFrom = iterableFrom(f)
    
    amt = amount(lstFrom)
    print('all start with "From ": {0}\n'.format(amt))
    for el in lstFrom:
        print(el)
    
    # run: python3 howManyFrom.py

