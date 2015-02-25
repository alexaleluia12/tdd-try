#!/usr/bin/env python3

import unittest
import sys

# TODO
# ver o que da usando o xmlData2

sys.path.insert(1, '..')
from mod import parsingXml

xmlData = """
<person>
    <name>Chuck</name>    
    <email hide="yes"/>
</person>
"""

xmlData2 = """
<person>
    <name>Chuck</name>
    <name>Julia</name>    
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
        
        self.assertEqual(
            parsingXml.getTagText('name', xmlData),
            'Chuck'
        )
        

if __name__ == '__main__':
    unittest.main()

