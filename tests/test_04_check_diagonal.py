"""
test_04_check_diagonal.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the check_diagonal function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import check_diagonal

# def check_diagonal (grid, diagonal):
#     """
#     Function Name: check_diagonal
#     Description: returns True if all the elements in the given
#     diagonal are x or all the elements in the diagonal are o,
#     otherwise it will return False. Note that the diagonal d1
#     includes elements [0][0], [1][1] and [2][2] and the diagonal
#     d2 includes elements [0][2], [1][1] and [2][0].
#     Parameter: grid - A 3 by 3 2D nested list.
#                diagonal - d1 or d2
#     Returns boolean value as defined in the description.
#     """
#     if diagonal == 'd1':
#         if grid[0][0] == 'x' and grid[1][1] == 'x' and grid[2][2] == 'x':
#             return True
#         elif grid[0][0] == 'o' and grid[1][1] == 'o' and grid[2][2] == 'o':
#             return True
#     elif diagonal == 'd2':
#         if grid[0][2] == 'x' and grid[1][1] == 'x' and grid[2][0] == 'x':
#             return True
#         elif grid[0][2] == 'o' and grid[1][1] == 'o' and grid[2][0] == 'o':
#             return True

#     return False



class TestCheckDiagonal(unittest.TestCase):
    """Unit tests for check_diagonal function."""

    def test_01_check_diagonal_d1_all_x(self):
        """Test that check_diagonal returns True if all the elements in the given diagonal are x."""
        grid = [['x', ' ', 'o'], [' ', 'x', 'o'], ['o', ' ', 'x']]
        self.assertEqual(check_diagonal(grid, 'd1'), True, msg="Wrong boolean value. Expected True for input [['x', ' ', 'o'], [' ', 'x', 'o'], ['o', ' ', 'x']] and diagonal 'd1'")

    def test_02_check_diagonal_d1_all_o(self):
        """Test that check_diagonal returns True if all the elements in the given diagonal are o."""
        grid = [['o', ' ', 'x'], [' ', 'o', 'x'], ['x', ' ', 'o']]
        self.assertEqual(check_diagonal(grid, 'd1'), True, msg="Wrong boolean value. Expected True for input [['o', ' ', 'x'], [' ', 'o', 'x'], ['x', ' ', 'o']] and diagonal 'd1'")

    def test_03_check_diagonal_d1_mixed(self):
        """Test that check_diagonal returns False if the elements in the given diagonal are mixed."""
        grid = [['x', ' ', 'o'], [' ', 'x', 'o'], [' ', 'x', 'o']]
        self.assertEqual(check_diagonal(grid, 'd1'), False, msg="Wrong boolean value. Expected False for input [['x', ' ', 'o'], [' ', 'x', 'o'], [' ', 'x', 'o']] and diagonal 'd1'")

    def test_04_check_diagonal_d2_all_x(self):
        """Test that check_diagonal returns True if all the elements in the given diagonal are x."""
        grid = [['o', ' ', 'x'], [' ', 'x', 'o'], ['x', ' ', 'o']]
        self.assertEqual(check_diagonal(grid, 'd2'), True, msg="Wrong boolean value. Expected True for input [['o', ' ', 'x'], [' ', 'x', 'o'], ['x', ' ', 'o']] and diagonal 'd2'")

    def test_05_check_diagonal_d2_all_o(self):
        """Test that check_diagonal returns True if all the elements in the given diagonal are o."""
        grid = [['x', ' ', 'o'], [' ', 'o', 'x'], ['o', ' ', 'x']]
        self.assertEqual(check_diagonal(grid, 'd2'), True, msg="Wrong boolean value. Expected True for input [['x', ' ', 'o'], [' ', 'o', 'x'], ['o', ' ', 'x']] and diagonal 'd2'")

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestCheckDiagonal))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)