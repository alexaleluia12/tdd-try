#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
from mod import counterEmailDomain as ced

class CounterEmailDomainTest(unittest.TestCase):
    
    def test_getAllEmailDomain(self):
        lst = ['any@gmail.com', 'x@gmail.com', 'oi@hotmail.com']
        self.assertEqual(
            list(ced.getAllEmailDomain(lst)),
            ['gmail.com', 'gmail.com', 'hotmail.com']
        )

if __name__ == '__main__':
    unittest.main()

        
