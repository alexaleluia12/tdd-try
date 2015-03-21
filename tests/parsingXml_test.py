#!/usr/bin/env python3

import unittest

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
   
    def test_getTag(self):# posso adicionar mais cosas a esse teste
        tagObj = parsingXml.getTag('name', xmlData)
        self.assertTrue(isinstance(tagObj, parsingXml.treeXml.Element))


    def test_getTagAttr(self):
        self.assertEqual(
            parsingXml.getTagAttr('hide', 'email', xmlData),
            'yes'
        )
    
    def test_getTagText(self):
        self.assertEqual(parsingXml.getTagText('name', xmlData), 'Chuck')
        self.assertEqual(parsingXml.getTagText('name', xmlData2), 'Chuck')
        # return the first tag 'name' 


if __name__ == '__main__':
    unittest.main()

