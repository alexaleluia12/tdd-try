#!/usr/bin/env python3

import re
import urllib.request
import codecs
# TODO

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
#    return a generator where element is an line of the page

# linksPage(iterable)
#    return a iterable with all links in iterator



def pageContent(url):
    response = urllib.request.urlopen(url)
    if response:
        for i in response:
            yield codecs.decode(i, 'utf8', 'ignore')
            


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
    

        
