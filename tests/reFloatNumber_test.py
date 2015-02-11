#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')

from mod import reFloatNumber as rfn

class ReFloatNumberTest(unittest.TestCase):
    
    def test_getStrFloat(self):
        str1 = 'X-DSPAM-Confidence: 4.8475'
        str2 = 'alex89.903 al apucarana 9.0 3 now'
        str3 = 'just run Forrest'
        self.assertListEqual(rfn.getStrFloat('X-DSPAM-Confidence: 4.8475'), ['4.8475'])
        self.assertListEqual(rfn.getStrFloat(str2), ['89.903', '9.0'])
        self.assertListEqual(rfn.getStrFloat(str3), [])
        

if __name__ == '__main__':
    unittest.main()

        


