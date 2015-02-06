#!/usr/bin/env python3

import sys, os
import unittest

sys.path.insert(1, os.path.join('..'))

from mod import writeInFile as wf

def excludeFile(strName):
    os.remove(strName)
    return not os.path.exists(strName)

class WriteInFileTest(unittest.TestCase):
        
    def test_write(self):
        conn = open('aux/any.txt', 'w')
        self.assertTrue(wf.write(conn, 'oi alex'))
        conn.close()
        excludeFile('aux/any.txt')

class TestHelperFunction(unittest.TestCase):

    def test_excludeFile(self):# essa eh uma funcao definida nesse mesmo arquivo
        open('aux/x.txt', 'w').close()
        self.assertTrue(excludeFile('aux/x.txt'))    
            

if __name__ == '__main__':
    unittest.main()


        
