#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
import mod.fileLines as fl


class FileLinesTest(unittest.TestCase):
    
    def test_counteLine(self):
        good = ['nay', 'now', 'node', 'tdd']
        self.assertEqual(fl.countLine(good), 4)
        self.assertEqual(fl.countLine([]), 0)
        self.assertEqual(fl.countLine(["'"]), 1)        

    
if __name__ == '__main__':
    unittest.main()

