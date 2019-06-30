import tkinter as tk
import unittest

import context
import SunFlwr


class testClass(unittest.TestCase):
    """docstring"""

    @classmethod
    def setUpClass():
        '''before the first test'''
        pass

    @classmethod
    def tearDownClass():
        '''after last test'''
        pass

    def setUp(self):
        '''before each method'''
        pass

    def teardown():
        '''after each method'''
        pass


if __name__ == '__main__':
    unittest.main()
