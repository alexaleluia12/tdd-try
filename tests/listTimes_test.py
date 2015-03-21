#!/usr/bin/env python3

import unittest

import mod.listTimes as lt


class MultElementosTest(unittest.TestCase):

    def test_timesElements(self):
        self.assertEqual(lt.timesElements([3, 5, 2], 2), [6, 10, 4])


if __name__ == '__main__':
    unittest.main()

