#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
from mod import urlLinks


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
            "<li><a href='http://www.g1.globo.com/'>news</a></li>"
        ]
        self.assertEqual(
            urlLinks.linksPage(lst), 
            ["http://www.google.com/", "http://www.g1.globo.com/"]
        )
    
    def test_pageContentFail(self):
        badUlr = 'http://www.dr-chuck.com/bage1.htm'
        error = urlLinks.pageContent(' ')
        self.assertEqual(error, '')
        
    def test_integration(self):
        url = 'http://www.dr-chuck.com/page1.htm' # this url need work
        page = list(urlLinks.pageContent(url))
        links = urlLinks.linksPage(page)
        self.assertEqual(links, ['http://www.dr-chuck.com/page2.htm'])

if __name__ == '__main__':
    unittest.main()

        
