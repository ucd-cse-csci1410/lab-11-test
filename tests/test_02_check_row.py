"""
test_02_check_row.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the check_row function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.main import check_row


# def check_row (grid, row):
#     """
#     Function Name: check_row
#     Description: returns True if all the elements in the given row
#     are x or all the elements in the given row are o, otherwise it will
#     return False.
#     Parameter: grid - A 3 by 3 2D nested list.
#                row - row number
#     Returns boolean value as defined in the description.
#     """

#     if grid[row][0] == 'x' and grid[row][1] == 'x' and grid[row][2] == 'x':
#         return True
#     elif grid[row][0] == 'o' and grid[row][1] == 'o' and grid[row][2] == 'o':
#         return True

#     return False



class TestCheckRow(unittest.TestCase):
    """Unit tests for check_row function."""

    def test_01_check_row_firstrow_all_x(self):
        """Test that check_row returns True if all the elements in the given row are x."""
        grid = [['x', 'x', 'x'], [' ', 'o', 'o'], [' ', 'o', ' ']]
        self.assertEqual(check_row(grid, 0), True, msg="Wrong boolean value. Expected True for input [['x', 'x', 'x'], [' ', 'o', 'o'], [' ', 'o', ' ']] and row 0")

    def test_02_check_row_firstrow_all_o(self):
        """Test that check_row returns True if all the elements in the given row are o."""
        grid = [['o', 'o', 'o'], [' ', 'x', 'x'], [' ', 'x', ' ']]
        self.assertEqual(check_row(grid, 0), True, msg="Wrong boolean value. Expected True for input [['o', 'o', 'o'], [' ', 'x', 'x'], [' ', 'x', ' ']] and row 0")

    def test_03_check_row_firstrow_mixed(self):
        """Test that check_row returns False if the elements in the given row are mixed."""
        grid = [['x', 'o', 'x'], ['o', 'x', 'o'], [' ', ' ', ' ']]
        self.assertEqual(check_row(grid, 0), False, msg="Wrong boolean value. Expected False for input [['x', 'o', 'x'], ['o', 'x', 'o'], [' ', ' ', ' ']] and row 0")


    def test_04_check_row_secondrow_all_x(self):
        """Test that check_row returns True if all the elements in the given row are x."""
        grid = [['x', 'x', ' '], ['o', 'o', 'o'], ['x', ' ', ' ']]
        self.assertEqual(check_row(grid, 1), True, msg="Wrong boolean value. Expected True for input [['x', 'x', ' '], ['o', 'o', 'o'], ['x', ' ', ' ']] and row 1")

    def test_05_check_row_secondrow_all_o(self):
        """Test that check_row returns True if all the elements in the given row are o."""
        grid = [['o', 'o', ' '], ['x', 'x', 'x'], ['o', ' ', ' ']]
        self.assertEqual(check_row(grid, 1), True, msg="Wrong boolean value. Expected True for input [['o', 'o', ' '], ['x', 'x', 'x'], ['o', ' ', ' ']] and row 1")

    def test_06_check_row_secondrow_mixed(self):
        """Test that check_row returns False if the elements in the given row are mixed."""
        grid = [['x', 'o', ' '], ['o', 'x', ' '], [' ', ' ', ' ']]
        self.assertEqual(check_row(grid, 1), False, msg="Wrong boolean value. Expected False for input [['x', 'o', ' '], ['o', 'x', ' '], [' ', ' ', ' ']] and row 1")
    
    def test_07_check_row_thirdrow_all_x(self):
        """Test that check_row returns True if all the elements in the given row are x."""
        grid = [['o', ' ', ' '], [' ', 'o', 'o'], ['x', 'x', 'x']]
        self.assertEqual(check_row(grid, 2), True, msg="Wrong boolean value. Expected True for input [['o', ' ', ' '], [' ', 'o', 'o'], ['x', 'x', 'x']] and row 2")

    def test_08_check_row_thirdrow_all_o(self):
        """Test that check_row returns True if all the elements in the given row are o."""
        grid = [['x', ' ', ' '], ['x', 'x', ' '], ['o', 'o', 'o']]
        self.assertEqual(check_row(grid, 2), True, msg="Wrong boolean value. Expected True for input [['x', ' ', ' '], ['x', 'x', ' '], ['o', 'o', 'o']] and row 2")
    
    def test_09_check_row_thirdrow_mixed(self):
        """Test that check_row returns False if the elements in the given row are mixed."""
        grid = [[' ', ' ', ' '], ['o', 'x', 'o'], ['x', 'o', 'x']]
        self.assertEqual(check_row(grid, 2), False, msg="Wrong boolean value. Expected False for input [[' ', ' ', ' '], ['o', 'x', 'o'], ['x', 'o', 'x']] and row 2")
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestCheckRow))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():  # Goes to stdout (for autograder)
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)            # Non-zero exit code signals failure