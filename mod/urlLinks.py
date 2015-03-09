#!/usr/bin/env python3

import re
from urllib import request
import codecs

"""
import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html) # retorna uma lista

for link in links:
    print link
"""

# pageContent(url)
#    return a generator where element is a line of the page

# linksPage(iterable)
#    return a iterable with all links

"""
Case this code not work check Your DNS internet service. 
see: http://en.wikipedia.org/wiki/DNS_hijacking
(request invalid url still return some thing)

I indicate wear http://opendns.com/
"""

def pageContent(url):
    response = request.urlopen(url)
    if response:
        for i in response:
            yield codecs.decode(i, 'utf-8', 'ignore')

def linksPage(iterable):
    regex = r"""href=["'](https?://.*?)["']""" # suport http and https
    strContent = " ".join(iterable)
    return re.findall(regex, strContent) 

if __name__ == '__main__':
    url = input('Enter with url like http://google.com\n ->: ')
    links = linksPage(pageContent(url))
    print('###')
    for link in links:
        print(link)

    # run: $ python3 urlLinks.py

