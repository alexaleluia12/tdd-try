#!/usr/bin/env python3

import unittest
import os
import sys

sys.path.insert(1, os.path.join('..'))
import mod.commonWord as cw

class CommonWordTest(unittest.TestCase):    
                                   
    def test_mapWordCount(self):
        valStr = "other   x in : the; the"
        self.assertEqual(
            cw.mapWordCount(valStr),
            {'the': 2, 'x': 1, 'other': 1, 'in': 1}
        )
        self.assertEqual(cw.mapWordCount(''), {})
    
    def test_getWin(self):
        valDict = {'a': 2, 'b': 34, 'c': 33}
        self.assertEqual(cw.getWin(valDict), ('b', 34))
        self.assertRaises(AssertionError, cw.getWin, {})
    
if __name__ == "__main__":
    unittest.main()        
    # run test: $ python3 commonWord_test.py -v
 
