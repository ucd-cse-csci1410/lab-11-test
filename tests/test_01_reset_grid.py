"""
test_01_reset_grid.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the reset_grid function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch


import sys
import os

# def reset_grid (grid):
#     """
#     Function Name: reset_grid
#     Description: reset the grid by changing all the elements to blank (' ').
#     Parameter: grid - A 3 by 3 2D nested list.
#     Returns Nothing
#     """

#     for i in range (3):
#         for j in range (3):
#             grid [i][j] = ' '



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import reset_grid


class TestResetGrid(unittest.TestCase):
    """Unit tests for reset_grid function."""

    def test_01_reset_grid(self):
        """Test the reset_grid function."""
        grid = [['x', 'o', 'o'], ['o', 'x', 'o'], ['x', 'o', 'x']]
        reset_grid(grid)
        self.assertEqual(grid, [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], msg="Wrong grid. Expected [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']] for input [['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'O', 'X']]")
    

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestResetGrid))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():  # Goes to stdout (for autograder)
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)