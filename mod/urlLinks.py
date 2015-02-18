#!/usr/bin/env python3

import re
import urllib.request

# TODO



# pageContent(url)
#    return a generator where element is an line of the page

# linksPage(iterable)
#    return a iterable with all links in iterator



def pageContent(url):
    response = urllib.request.urlopen(url)
    if response:
        for i in response:
            yield i.decode()


def linksPage(iterable):
    regex = """href=["'](http://.*?)["']""" # return just inside the ()
    strContent = " ".join(iterable)
    return re.findall(regex, strContent) 
    
if __name__ == '__main__':
    print(list(pageContent('http://www.dr-chuck.combage1.htm')))
    

        
