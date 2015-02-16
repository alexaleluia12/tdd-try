#!/usr/bin/env python3

import re
import urllib.request
"""
import urllib
import re
url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
links = re.findall('href="(http://.*?)"', html) # return a iterable

for link in links:
    print link    
"""
# pageContent(url)
#    return a generator were element is an line of the page

# linksPage(iterable)
#    return a iterable with all links in iterator



def pageContent(url):
    response = urllib.request.urlopen(url)
    if response.status == 200:
        for i in response:
            yield i.decode()


def linksPage(iterable):
    regex = """href=["'](http://.*?)["']""" # return just inside the ()
    strContent = " ".join(iterable)
    return re.findall(regex, strContent) 
    
if __name__ == '__main__':
    pass
    

        
