#!/usr/bin/env python3

import unittest
import sys
import urllib

sys.path.insert(1, '..')
from mod import urlLinks

"""
Case this code not work check Your DNS internet service. 
see: http://en.wikipedia.org/wiki/DNS_hijacking

I indicate wear http://opendns.com/ 
"""


# this test will be slow because it get resource on web
class UrlLinksTest(unittest.TestCase):
    
    def test_pageContent(self):
        url = 'http://www.dr-chuck.com/page1.htm'
        self.assertEqual(
            list(urlLinks.pageContent(url)),
            [
              '<h1>The First Page</h1>\n',
              '<p>\n',
              'If you like, you can switch to the \n',
              '<a href="http://www.dr-chuck.com/page2.htm">\n',
              'Second Page</a>.\n',
              '</p>\n'
            ],
            msg="if it's FAIL please check if the 'url' sanity"
        )
        
    def test_linksPage(self):
        lst = [
            'alex programing',
            '<p><a href="http://www.google.com/">know</a></p>',
            'brasil is a good place'
            "<li><a href='http://www.g1.globo.com/'>news</a></li>",
            '<h1><a href="https://www.bbc.com/">bbc</a></h1>'
        ]
        self.assertEqual(
            urlLinks.linksPage(lst), 
            ["http://www.google.com/", "http://www.g1.globo.com/", "https://www.bbc.com/"]
        )
    
    def test_pageContentFail(self):
        badUlr = "http://www.dfoijoeijfpaoijf.combage1.htm"
        with self.assertRaises(urllib.error.URLError) as er: # the code inseide 'with' should raise urllib.error.URLError to pass
            e = list(urlLinks.pageContent("http://www.dfoijoeijfpaoijf.combage1.htm"))
            
        
    def test_integration(self):
        url = 'http://www.google.com.br/' # this url need be valid
        aboutBrGoogle = 'http://www.google.com.br/history/optout?hl=pt-BR'        
        page = list(urlLinks.pageContent(url))
        links = urlLinks.linksPage(page)
        self.assertTrue(aboutBrGoogle in links)


if __name__ == '__main__':
    unittest.main()

        
