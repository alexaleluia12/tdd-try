#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(1, os.path.join('..'))
import mod.forExample2 as fore

class ForExample2Test(unittest.TestCase):
    
    def test_main(self):
        self.assertEqual(fore.main([1,2,3,906,90]), 906)
        

if __name__ == '__main__':
	unittest.main()

        
    


