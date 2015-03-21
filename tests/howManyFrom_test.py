#!/usr/bin/env python3

import unittest

from mod import howManyFrom as hmf

class HowManyFromTest(unittest.TestCase):
    
    def test_iterableFrom(self):
        self.assertListEqual(
             hmf.iterableFrom(['kdi d joe', 'From xckco@a', 'dkkk do']), 
             ['From xckco@a']   
        )

    def test_amount(self):
        self.assertEqual(hmf.amount(['e', 'e', 'e']), 3)

if __name__ == '__main__':
    unittest.main()
