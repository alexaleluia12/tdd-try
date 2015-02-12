#!/usr/bin/env python3

import unittest
import sys


sys.path.insert(1, '..')

from mod import axCounter

class AxCounterTest(unittest.TestCase):
    
    def test_iterableN(self):
        lst = [
            'From alex to marcos 2123',
            'any time 366@gmail.com',
            'any time 8934@hotmail.com',
            'X 3772 king@9098.com'
        ]
        regex = r'\bany .+'
        self.assertEqual(
            axCounter.iterableN(lst, regex),
            ['any time 366@gmail.com',
             'any time 8934@hotmail.com'
            ]
        )
        
        regex2 = r'king'
        self.assertEqual(
            axCounter.iterableN(lst, regex2),
            ['X 3772 king@9098.com']
        )
        
    def test_mapCounter(self):
        lst = ['Thu','Thu','Fri']
        lst2 = ['a@g.com', 'an@ufu.obr', 'x@i.com']
        self.assertEqual(axCounter.mapCounter(lst), {'Thu': 2, 'Fri': 1})
        self.assertEqual(
            axCounter.mapCounter(lst2),
            {'a@g.com': 1, 'an@ufu.obr': 1, 'x@i.com': 1}
        )
        
    def test_getAllPosionedElement(self):
        lst = [
            'any time 366@gmail.com',
            'any time 8934@hotmail.com'
        ]
        self.assertEqual(
            list(axCounter.getAllPosionedElement(lst, 2)),
            ['366@gmail.com', '8934@hotmail.com'] 
        )   
                
    def test_integration(self):
        lst = [
            'From time a@x.com 3772',
            'any uk 366@gmail.com',
            'x US BR to fernada',
            'From all a@hotmail.com 122',
            'From branch a@hotmail.com 3',
        ]
        lstFrom = axCounter.iterableN(lst, r'\bFrom .+')
        lstEmail = axCounter.getAllPosionedElement(lstFrom, 2)
        self.assertEqual(
            axCounter.mapCounter(lstEmail),
            {'a@hotmail.com': 2, 'a@x.com': 1}
        )

if __name__ == '__main__':
    unittest.main()

        
