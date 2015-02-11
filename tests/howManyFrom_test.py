#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')

from mod import howManyFrom as hmf

class HowManyFromTest(unittest.TestCase):
    
    def test_amountFrom(self):
        self.assertListEqual(
             hmf.amountFrom(['kdi d joe', 'From xckco@a', 'dkkk do'])
            , 
             ['From xckco@a']   
        )

if __name__ == '__main__':
    unittest.main()

        
