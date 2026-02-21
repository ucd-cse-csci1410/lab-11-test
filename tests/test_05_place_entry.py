"""
test_05_place_entry.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the place_entry function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest
import sys
import os

from unittest.mock import patch


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import place_entry

# def place_entry (grid, row, col, ch):
#     """
#     Function Name: place_entry
#     Description: places the ch into the location given by row_num
#     and col_num). ch will be either x or o. It will check to make
#     sure that the cell given by row_num and col_num is blank. If it
#     is blank then it will place the ch in the given location and
#     return True. If the cell is not empty then it will return False.
#     Parameter: grid - A 3 by 3 2D nested list.
#                row - row number
#                col - colum number
#                ch - character to insert (x or o)
#     Returns boolean value as defined in the description.
#     """
#     if grid[row][col] == ' ':
#         grid[row][col] = ch
#         return True

#     return False


class TestPlaceEntry(unittest.TestCase):
    """Unit tests for place_entry function."""

    # case_01: Test place_entry correctly if there is blank space
    def test_01_place_entry_blank_space(self):
        """Test that place_entry returns True if there is blank space."""
        grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(place_entry(grid, 0, 0, 'x'), True, msg="Wrong boolean value. Expected True for input [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] and row 0, col 0, ch 'x'")

    # case_02: Test place_entry returns False if there is not blank space
    def test_02_place_entry_not_blank_space(self):
        """Test that place_entry returns False if there is not blank space."""
        grid = [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(place_entry(grid, 0, 0, 'x'), False, msg="Wrong boolean value. Expected False for input [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] and row 0, col 0, ch 'x'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestPlaceEntry))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)