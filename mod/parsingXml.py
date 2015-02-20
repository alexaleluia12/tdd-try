#!/usr/bin/env python3

import xml.etree.ElementTree as treeXml

# TODO
# fazeri o getTagText() funcioar em '<name>alex</name>'
# atualmente nao esta

"""
import xml.etree.ElementTree as ET
data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print 'Name:',tree.find('name').text
print 'Attr:',tree.find('email').get('hide')
print type(data)    
"""
# getTag(tagName, xmlData)
#    return a tagName objec 'xml.etree.ElementTree.Element'
#    from 'xmlData'
#    'xmlData' is an string

# getTagText(tagName, xmlData)
#    return the text of the 'tagName' from 'xmlData' string
#    'tagName' and 'xmlData' need be string
#    <name>alex</name> -> alex

# getTagAttr(attr, tagName, xml)
#    return the atribute value from 'tagName' found in 'xmlData' string
#    'attr' shold be atribute in 'tagName'
#    'attr', 'tagName', 'xmlData' are all string

def getTag(tagName, xmlData):
    xmlData = treeXml.fromstring(xmlData)
    return xmlData.find(tagName)    

def getTagText(tag, xmlData):
    xmlData = treeXml.fromstring(xmlData)
    return xmlData.find(tag).text

def getTagAttr(attr, tag, xmlData):
    tag = getTag(tag, xmlData)
    return tag.get(attr)


if __name__ == '__main__':
    pass

