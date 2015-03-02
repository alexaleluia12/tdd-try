#!/usr/bin/env python3

import unittest
from unittest import mock
import sys

sys.path.insert(1, '..')
from mod import urlLinks


class UrlLinksTest(unittest.TestCase):
    
    @mock.patch.object(urlLinks.request, 'urlopen', autospec=True)
    def test_pageContent(self, mk_urlopen):
        url = 'http://www.dr-chuck.com/page1.htm'
        lstByte = [
            b'<h1>The First Page</h1>\n',
            b'<p>\n',
            b'If you like, you can switch to the \n',
            b'<a href="http://www.dr-chuck.com/page2.htm">\n',
            b'Second Page</a>.\n',
            b'</p>\n'
        ]
        lstNormal = [
            '<h1>The First Page</h1>\n',
            '<p>\n',
            'If you like, you can switch to the \n',
            '<a href="http://www.dr-chuck.com/page2.htm">\n',
            'Second Page</a>.\n',
            '</p>\n'
        ]
        mk_urlopen.return_value = lstByte
        self.assertEqual(
            list(urlLinks.pageContent(url)),
            lstNormal,
            msg="if it's FAIL please check if the 'url' sanity"
        )
        mk_urlopen.assert_called_with(url)
        
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
            ["http://www.google.com/", 
             "http://www.g1.globo.com/", 
             "https://www.bbc.com/"
            ]
        )
    
if __name__ == '__main__':
    unittest.main()

