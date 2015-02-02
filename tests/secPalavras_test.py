#!/usr/bin/env python3


import unittest
import os, sys

sys.path.insert(1, os.path.join('..'))
import mod.secPalavras as secp
from mod.myErrorException import FileEmpty



FILE =  os.path.join('aux', 'romeo.txt')
FILEEMP = os.path.join('aux', 'music.txt')

class SecPalavasTest(unittest.TestCase):    

    def test_getFile_str(self):
        self.assertIsInstance(secp.getFile(FILE), str)      
      
    def test_getFile_exception(self):
        self.assertRaises(FileEmpty, secp.getFile, FILEEMP)

    #--
    def test_mapWordCount(self):
        words = "it it no can"
        self.assertDictEqual(secp.mapWordCount(words), {'it':2, 'no': 1, 'can': 1})
    
    #--
    def test_getWin(self):
        testDict = {'it':2, 'no': 1, 'can': 1}
        self.assertTupleEqual(secp.getWin(testDict), ('it', 2))
    
    #--
    def test_main(self):        
        self. assertIsInstance(secp.main(FILE), tuple)
        
        

    
if __name__ == "__main__":
    unittest.main()        
    # run test: $ python3 secPalavras_test.py -v
    
