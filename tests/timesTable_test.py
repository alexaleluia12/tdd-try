#!/usr/bin/env python3

import unittest
import sys, os


sys.path.insert(1, os.path.join('..'))
from mod import timesTable

class TabuadaTest(unittest.TestCase):
    
    def test_sanityEnter_int(self):
        self.assertTrue(timesTable.sanityEnter(1, int))        
        self.assertTrue(timesTable.sanityEnter(4, int, (1, 5)))
        self.assertTrue(timesTable.sanityEnter(5, int, (1, 5)))
        self.assertFalse(timesTable.sanityEnter(6, int, (1, 5)))
        self.assertFalse(timesTable.sanityEnter('1', int))
        
        
    def test_sanityEnter_str(self):
        self.assertTrue(timesTable.sanityEnter('a', str))
        self.assertFalse(timesTable.sanityEnter(2, str))
        self.assertTrue(timesTable.sanityEnter('c', str, ('a', 'e')))
    
    def test_sanityEnter(self):
        self.assertRaises(TypeError, timesTable.sanityEnter, 'c', ('a', 'e'))
        self.assertTrue( 
            timesTable.sanityEnter([5,9], list, ([2, 1], [10, 12])) 
        )# polymorphism

    #---
    def test_getTimesTab(self):
        self.assertSequenceEqual( 
            list(timesTable.getTimesTab(3, (1,2))), 
            [(3, 1, 3), (3, 2, 6)] 
        
        ) # convert the generator in list

if __name__ == '__main__':
    unittest.main()
    
     
