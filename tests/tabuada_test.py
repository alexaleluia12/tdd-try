#!/usr/bin/env python3

import unittest
import sys, os


sys.path.insert(1, os.path.join('..'))
from mod import tabuada as tbm

class TabuadaTest(unittest.TestCase):
    
    def test_validarEntrada_int(self):
        self.assertTrue(tbm.validaEntrada(1, int))        
        self.assertTrue(tbm.validaEntrada(4, int, (1, 5)))
        self.assertTrue(tbm.validaEntrada(5, int, (1, 5)))
        self.assertFalse(tbm.validaEntrada(6, int, (1, 5)))
        self.assertFalse(tbm.validaEntrada('1', int))
        
        
    def test_validarEntrada_str(self):
        self.assertTrue(tbm.validaEntrada('a', str))
        self.assertFalse(tbm.validaEntrada(2, str))
        self.assertTrue(tbm.validaEntrada('c', str, ('a', 'e')))
    
    def test_validarEntrada(self):
        self.assertRaises(TypeError, tbm.validaEntrada, 'c', ('a', 'e'))
        self.assertTrue( tbm.validaEntrada([5,9], list, ([2, 1], [10, 12])) )# poliformismo 
        
    
    #---
    def test_getTabuada(self):
        self.assertEqual(tbm.getTabuada(3, (1, 2)), [(3, 1, 3), (3, 2, 6)]) 

if __name__ == '__main__':
    unittest.main()

     
