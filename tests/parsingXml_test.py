#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
from mod import parsingXml

xmlData = """
<person>
    <name>Chuck</name>    
    <email hide="yes"/>
</person>
"""

class ParsingXmlTest(unittest.TestCase):
    
   
        
    def test_getTag(self):
        self.assertEqual(
            type(parsingXml.getTag('name', xmlData)),
            parsingXml.treeXml.Element
        )
        # this is a bit tricky but is like
        # >>> int == type(1) 
        # True

            
    def test_getTagAttr(self):
        self.assertEqual(
            parsingXml.getTagAttr('hide', 'email', xmlData),
            'yes'
        )            
    
    def test_getTagText(self):
        simpleXml = '<name>alex</name>'
        self.assertEqual(
            parsingXml.getTagText('name', xmlData),
            'Chuck'
        )
        self.assertEqual(
            parsingXml.getTagText('name', simpleXml),
            'alex'
        ) 

if __name__ == '__main__':
    unittest.main()

        
"""
espera:
    
    
"""



