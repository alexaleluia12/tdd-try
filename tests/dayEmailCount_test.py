#!/usr/bin/env python3

import unittest
import sys

sys.path.insert(1, '..')
from mod import dayEmailCount as dmc

class DayEmailCountTest(unittest.TestCase):
    
    def test_mapDayWeekCount(self):
        lst = ['Thu','Thu','Fri']
        self.assertEqual(dmc.mapDayWeekCount(lst), {'Thu': 2, 'Fri': 1})
    
    def test_getWeekDays(self):
        lst = [
            'From louis@media.berkeley.edu Thu Jan  3 19:51:21 2008',
            'From louis@media.berkeley.edu Thu Jan  3 17:18:23 2008',
            'From david.horwitz@uct.ac.za Fri Jan  4 07:02:32 2008'   
        ]
        self.assertEqual(list(dmc.getWeekDays(lst)), ['Thu', 'Thu', 'Fri'])

if __name__ == '__main__':
    unittest.main()

"""
    
"""

