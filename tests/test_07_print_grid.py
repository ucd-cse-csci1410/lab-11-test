"""
test_04_compute_sd.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the compute_sd function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest

from unittest.mock import patch
from io import StringIO

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from src.main import print_grid

# def print_grid (grid):
#     """
#     Function Name: print_grid
#     Description: prints grid using f string.
#     Parameter: grid - A 3 by 3 2D nested list.
#     Returns nothing
#     """

#     for i in range (3):
#         print ('-------------')
#         for j in range (3):
#             print (f'| {grid[i][j]:1s}', end=' ')
#         print ('|')
#     print ('-------------')


class TestPrintGrid(unittest.TestCase):
    """Unit tests for print_grid function."""

    # case_01: Test print_grid correctly.
    @patch('sys.stdout', new_callable=StringIO)
    def test_01_print_grid(self, mock_stdout):
        """Test that print_grid prints the grid correctly."""
        grid = [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
        print_grid(grid)
        output = mock_stdout.getvalue()
        expected = "-------------\n| x | o | x |\n-------------\n| o | x | o |\n-------------\n| x | o | x |\n-------------\n"
        self.assertEqual(
             output,
             expected,
             msg=f"Wrong print. Expected:\n{expected!r}\n\nActual output:\n{output!r}\n\nFor input [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]")
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestPrintGrid))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")