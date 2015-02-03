#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(1, os.path.join('..'))
import mod.multElementos as mt


class MultElementosTest(unittest.TestCase):
    
    def test_multElementos(self):
        self.assertEqual(mt.multElementos([3, 5, 2], 2), [6, 10, 4])


if __name__ == '__main__':
    unittest.main()


        
