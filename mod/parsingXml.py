#!/usr/bin/env python3

import xml.etree.ElementTree as treeXml

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
    tagObj = getTag(tag, xmlData)
    return tagObj.text

def getTagAttr(attr, tag, xmlData):
    tagObj = getTag(tag, xmlData)
    return tagObj.get(attr)


if __name__ == '__main__':
    data = '''
    <person>
        <name>Chuck</name>
        <phone type="intl">
            +1 734 303 4456
        </phone>
        <email hide="yes"/>
    </person>'''
    
    print('Name: {0}'.format(getTagText('name', data)))
    print('Attr of email.hide: {0}'.format(getTagAttr('hide', 'email', data)))
    
    # run: python3 parsingXml.py

