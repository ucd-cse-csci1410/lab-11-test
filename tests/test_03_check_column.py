"""
test_03_check_column.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the check_column function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.main import check_column


# def check_column (grid, col):
#     """
#     Function Name: check_column
#     Description: returns True if all the elements in the given column
#     are x or all the elements in the given column are o, otherwise it will
#     return False.
#     Parameter: grid - A 3 by 3 2D nested list.
#                col - column number
#     Returns boolean value as defined in the description.
#     """

#     if grid[0][col] == 'x' and grid[1][col] == 'x' and grid[2][col] == 'x':
#         return True
#     elif grid[0][col] == 'o' and grid[1][col] == 'o' and grid[2][col] == 'o':
#         return True

#     return False



class TestCheckColumn(unittest.TestCase):
    """Unit tests for check_column function."""

    def test_01_check_column_firstcol_all_x(self):
        """Test that check_column returns True if all the elements in the given column are x."""
        grid = [['x', ' ', 'o'], ['x', 'o', ' '], ['x', 'o', ' ']]
        self.assertEqual(check_column(grid, 0), True, msg="Wrong boolean value. Expected True for input [['x', ' ', 'o'], ['x', 'o', ' '], ['x', 'o', ' ']] and column 0")

    def test_02_check_column_firstcol_all_o(self):
        """Test that check_column returns True if all the elements in the given column are o."""
        grid = [['o', ' ', ' '], ['o', 'x', 'x'], ['o', 'x', ' ']]
        self.assertEqual(check_column(grid, 0), True, msg="Wrong boolean value. Expected True for input [['o', 'o', 'o'], ['o', 'x', 'x'], ['o', 'x', 'o']] and column 0")

    def test_03_check_column_firstcol_mixed(self):
        """Test that check_column returns False if the elements in the given column are mixed."""
        grid = [['x', 'o', ' '], ['o', 'x', ' '], ['x', 'o', ' ']]
        self.assertEqual(check_column(grid, 0), False, msg="Wrong boolean value. Expected False for input [['x', 'o', ' '], ['o', 'x', ' '], ['x', 'o', ' ']] and column 0")


    def test_04_check_column_secondcol_all_x(self):
        """Test that check_column returns True if all the elements in the given column are x."""
        grid = [[' ', 'x', 'o'], ['o', 'x', ' '], [' ', 'x', 'o']]
        self.assertEqual(check_column(grid, 1), True, msg="Wrong boolean value. Expected True for input [[' ', 'x', 'o'], ['o', 'x', ' '], [' ', 'x', 'o']] and column 1")

    def test_05_check_column_secondcol_all_o(self):
        """Test that check_column returns True if all the elements in the given column are o."""
        grid = [[' ', 'o', ' '], ['x', 'o', 'x'], [' ', 'o', 'x']]
        self.assertEqual(check_column(grid, 1), True, msg="Wrong boolean value. Expected True for input [[' ', 'o', ' '], ['x', 'o', 'x'], [' ', 'o', 'x']] and column 1")

    def test_06_check_column_secondcol_mixed(self):
        """Test that check_column returns False if the elements in the given column are mixed."""
        grid = [['x', 'o', ' '], ['o', 'x', ' '], [' ', 'o', 'x']]
        self.assertEqual(check_column(grid, 1), False, msg="Wrong boolean value. Expected False for input [['x', 'o', ' '], ['o', 'x', ' '], [' ', 'o', 'x']] and column 1")
    
    def test_07_check_column_thirdcol_all_x(self):
        """Test that check_column returns True if all the elements in the given column are x."""
        grid = [[' ', 'o', 'x'], ['o', 'o', 'x'], [' ', ' ', 'x']]
        self.assertEqual(check_column(grid, 2), True, msg="Wrong boolean value. Expected True for input [[' ', 'o', 'x'], ['o', 'o', 'x'], [' ', ' ', 'x']] and column 2")

    def test_08_check_column_thirdcol_all_o(self):
        """Test that check_column returns True if all the elements in the given column are o."""
        grid = [['x', ' ', 'o'], ['x', 'x', 'o'], [' ', ' ', 'o']]
        self.assertEqual(check_column(grid, 2), True, msg="Wrong boolean value. Expected True for input [['x', ' ', 'o'], ['x', 'x', 'o'], [' ', ' ', 'o']] and column 2")
    
    def test_09_check_column_thirdcol_mixed(self):
        """Test that check_column returns False if the elements in the given column are mixed."""
        grid = [['o', ' ', 'x'], [' ', 'x', 'o'], [' ', 'o', 'x']]
        self.assertEqual(check_column(grid, 2), False, msg="Wrong boolean value. Expected False for input [[' ', ' ', 'x'], [' ', 'x', ' '], [' ', 'o', 'x']] and column 2")
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestCheckColumn))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():  # Goes to stdout (for autograder)
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)            # Non-zero exit code signals failure