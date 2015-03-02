#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
from mod import reverseWord as rw

class ReverseWordTest(unittest.TestCase):
    
    def test_checkWord(self):
        self.assertEqual(rw.checkWord('ab'), 'ab')
        self.assertEqual(rw.checkWord('e'), 'e')
        self.assertFalse(rw.checkWord('a23b'), False)
        self.assertFalse(rw.checkWord(''), False)
        
    def test_revert(self):
        self.assertEqual(rw.invert('a'), 'a')
        self.assertEqual(rw.invert('ab'), 'ba')
               

if __name__ == '__main__':
    unittest.main()
