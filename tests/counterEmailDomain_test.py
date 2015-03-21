#!/usr/bin/env python3

import unittest

from mod import counterEmailDomain as ced

class CounterEmailDomainTest(unittest.TestCase):

    def test_getAllEmailDomain(self):
        lst = ['any@gmail.com', 'x@gmail.com', 'oi@hotmail.com']
        self.assertEqual(
            list(ced.getAllEmailDomain(lst)),
            ['gmail.com', 'gmail.com', 'hotmail.com']
        )

    def test_getAllEmailDomainFail(self):
        lst = ['any@gmail.com', 'x#hotmail.com']
        with self.assertRaises(AssertionError) as er:
            self.assertEqual(
                list(ced.getAllEmailDomain(lst)),
                ['I hope this test fail']
            )


if __name__ == '__main__':
    unittest.main()
