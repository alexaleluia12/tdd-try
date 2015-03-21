#!/usr/bin/env python3

import unittest

from mod import writeInFile as wf

class MockOpen:
    def write(self, content):
        return len(content)
    
    def close(self):
        return True

class WriteInFileTest(unittest.TestCase):

    def test_write(self):
        mkFile = MockOpen()
        self.assertTrue(wf.write(mkFile, 'oi alex'))
        self.assertFalse(wf.write(mkFile, ''))
        mkFile.close()

if __name__ == '__main__':
    unittest.main()

