#!/usr/bin/env python3

import unittest
import os, sys

sys.path.insert(1, os.path.join('..'))
import mod.forExample1 as fore


class ForExample1Test(unittest.TestCase):
    
    def test_counterEl(self):
        self.assertEqual(fore.counterEl([2,2,2]), 3)
        self.assertNotEqual(fore.counterEl([2,2,2]), 6)
    
    def test_counter(self):
        self.assertEqual(fore.counter([2,2,2]), 6)
        self.assertNotEqual(fore.counter([2,2,2]), 3)
    
    def test_convertToList(self):
        self.assertListEqual(fore.convertToList('[2,2,2]'), [2,2,2])
        self.assertListEqual(fore.convertToList('[2, 2, 2, 490,  39 ]'), [2, 2, 2, 490, 39])
        
    def test_main(self):
        self.assertDictEqual(
            fore.main(
                [2,2,2]
            ),
            {'amount': 3, 'count': 6}
        )
        self.assertRaises(TypeError, fore.main, "[1,1,'alex']")


if __name__ == '__main__':
	unittest.main()

        

