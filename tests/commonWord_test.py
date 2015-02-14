#!/usr/bin/env python3


import unittest
import os, sys

sys.path.insert(1, os.path.join('..'))
import mod.commonWord as cw
from mod.myErrorException import FileEmpty



FILE =  os.path.join('aux', 'romeo.txt')
FILE2 = os.path.join('aux', 'self.txt')
FILEEMP = os.path.join('aux', 'music.txt')

class CommonWordTest(unittest.TestCase):    

    def test_getFile_str(self):
        self.assertIsInstance(cw.getFile(FILE), str)      
      
    def test_getFile_exception(self):
        self.assertRaises(FileEmpty, cw.getFile, FILEEMP)

    #--
    def test_mapWordCount(self):
        words = "it it no can"
        self.assertDictEqual(cw.mapWordCount(words), {'it':2, 'no': 1, 'can': 1})
    
    #--
    def test_getWin(self):
        testDict = {'it':2, 'no': 1, 'can': 1}
        self.assertTupleEqual(cw.getWin(testDict), ('it', 2))
    
    #--
    def test_main(self):        
        self.assertIsInstance(cw.main(FILE), tuple)
        self.assertTupleEqual(cw.main(FILE2), ('self', 4))
        
        

    
if __name__ == "__main__":
    unittest.main()        
    # run test: $ python3 commonWord_test.py -v
    
