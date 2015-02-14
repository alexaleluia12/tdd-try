#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(1, os.path.join('..'))
import mod.fileLines as fl

FILE = os.path.join('aux', 'romeo.txt')
BADFILE = 'any.txt'
class FileLinesTest(unittest.TestCase):
    
    def test_counteLine(self):
        
        self.assertEqual(fl.countLine(FILE), 4)
        self.assertEqual(fl.countLine(BADFILE), -1)        

    
if __name__ == '__main__':
    unittest.main()



