#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(1, os.path.join('..'))
import mod.linhasArquivo as lf

FILE = os.path.join('aux', 'romeo.txt')
BADFILE = 'any.txt'
class LinhasArquivoTest(unittest.TestCase):
    
    def test_counteLine(self):
        
        self.assertEqual(lf.countLine(FILE), 4)
        self.assertEqual(lf.countLine(BADFILE), -1)        

    
if __name__ == '__main__':
    unittest.main()



