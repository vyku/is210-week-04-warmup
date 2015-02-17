#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests lesson 04 task 04."""


# Import Python libs
import unittest
import mock

class Lesson04Task04TestCase(unittest.TestCase):
    """
    Test cases for lesson 04 task 04.

    """

    def test_short_str(self):
        """
        Tests that correct output is captured for a short string.
        """
        values = ['a']
        with mock.patch('__builtin__.raw_input',  side_effect=values):
            import task_04
            self.assertEqual(task_04.LONGSTR, 'short')

    def test_long_str(self):
        """
        Tests that correct output is captured for a long string.
        """
        values = ['a' * 100]
        with mock.patch('__builtin__.raw_input',  side_effect=values):
            import task_04
            self.assertEqual(task_04.LONGSTR, 'long')


if __name__ == '__main__':
    unittest.main()
