#!/usr/bin/env python3

import unittest

import mod.forExample2 as fore

class ForExample2Test(unittest.TestCase):
    
    def test_main(self):
        self.assertEqual(fore.main([1,2,3,906,90]), 906)
        self.assertEqual(fore.main([-1,-2,-45,-1,0]), 0)

if __name__ == '__main__':
    unittest.main()

