#!/usr/bin/env python3

import unittest
from unittest import mock
import os
import sys

sys.path.insert(1, os.path.join('..'))
import mod.commonWord as cw

class CommonWordTest(unittest.TestCase):    
    
    @mock.patch.object(cw, 'getFile', autospec=True)
    def test_getFile(self, mock_getFile):
        self.assertRaises(
            TypeError, mock_getFile, 'fakeFile', 'fake',
            msg="Failed to raise error, the interface of 'getFile' change"
        )
                          
        mock_getFile.return_value = 'the mock content file string'
        
        self.assertEqual(
            mock_getFile('fileName'),
            'the mock content file string'
        )
                                   
    def test_mapWordCount(self):
        valStr = "other   x in : the; the"
        self.assertEqual(
            cw.mapWordCount(valStr),
            {'the': 2, 'x': 1, 'other': 1, 'in': 1}
        )
    
    def test_getWin(self):
        valDict = {'a': 2, 'b': 34, 'c': 33}
        self.assertEqual(cw.getWin(valDict), ('b', 34))
    
if __name__ == "__main__":
    unittest.main()        
    # run test: $ python3 commonWord_test.py -v
   
