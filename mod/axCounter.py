#!/usr/bin/env python3

import re
import collections

# iterableN(iterable, regex)→ return a list where each element is 
#    take relative to `regex`
#    (`regex` is a regular expression like: r'[1-7]+')
#    (`iterable` should be a list of string)

# mapCounter(iterable)→ return a dict like 
#    {'Fri': 89, 'Thu': 90,...}
#    relative to amount of 'Fri' in `iterable`
#    (`iterable` should be a iterable of element repeated
#     repeated or not. Make sense the elements be the same type
#     e.g. ['v1','v2', 'v1',....])

# getAllPosionedElement(iterable, index)→ return a generator where
#    each element is take relative to `index` in `iterable` elements
#    (`iterable`: is an iterable made of standardized string,
#     the string should contain more than one space)
#....(`index`: is an int between 0 and len(iterable[0].split()) )


def iterableN(iterable, regex):
    lst = []
    for el in iterable:
        match = re.search(regex, el)
        if match:
            lst.append(el)
    return lst
    
def mapCounter(iterable):
    return dict(collections.Counter(iterable))

def getAllPosionedElement(iterable, index):
    for el in iterable:
        yield el.split()[index]

if __name__ == '__main__':
    pass

