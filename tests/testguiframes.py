
import tkinter as tk
import unittest

import context
import SunFlwr
from SunFlwr.sunui import winframes as wf


class GuiTestSuite(unittest.TestCase):
    """docstring for GuiTestSuite."""

    @classmethod
    def setUpClass():
        '''before the first test'''
        pass

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
