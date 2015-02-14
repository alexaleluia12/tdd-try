#!/usr/bin/env python3

import unittest
import sys, os

sys.path.insert(1, os.path.join('..'))
import mod.listTimes as lt


class MultElementosTest(unittest.TestCase):
    
    def test_timesEl(self):
        self.assertEqual(lt.timesEl([3, 5, 2], 2), [6, 10, 4])


if __name__ == '__main__':
    unittest.main()


        
