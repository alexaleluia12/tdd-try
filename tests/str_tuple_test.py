#!/usr/bin/env python3


import unittest

from mod import str_tuple as stu

class StrTupleTest(unittest.TestCase):
    
    def test_mapWords(self):
        self.assertEqual(
            stu.mapWords("alex join now"), 
            [(4, 'alex'), (4, 'join'), (3, 'now')]
        )
        
    def test_getWords(self):
        listTest = [(4, 'alex'), (4, 'joine'), (3, 'now')]
        self.assertListEqual(
            list(stu.getWords(listTest)), 
            ['joine', 'alex', 'now']
        )


if __name__ == '__main__':
    unittest.main()
