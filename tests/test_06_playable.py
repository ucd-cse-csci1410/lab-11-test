"""
test_06_playable.py

Author: Chiranth Ajjamane Manohar
Date: 2026-02-05
Version: 0.1
Description: test file for the playable function.
Copyright (c) 2026 University of Colorado Denver - Department of Computer Science

"""

import unittest


from unittest.mock import patch

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import playable

# def playable (grid):
#     """
#     Function Name: playable
#     Description: check to see if there are any empty (blank) elements.
#     It will use nested loops to check each element in the nested list.
#     If any of the element is empty (blank) then it will return True,
#     otherwise it will return False.
#     Parameter: grid - A 3 by 3 2D nested list.
#     Returns boolean value as defined in the description.
#     """
#     for i in range (3):
#         for j in range (3):
#             if grid[i][j] == ' ':
#                 return True

#     return False


class TestPlayable(unittest.TestCase):
    """Unit tests for playable function."""

    # case_01: Test playable returns True if there is blank space
    def test_01_playable_blank_space(self):
        """Test that playable returns True if there is blank space."""
        grid = [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(playable(grid), True, msg="Wrong boolean value. Expected True for input [['x', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]")
    
    # case_02: Test playable returns False if there is not blank space
    def test_02_playable_not_blank_space(self):
        """Test that playable returns False if there is not blank space."""
        grid = [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]
        self.assertEqual(playable(grid), False, msg="Wrong boolean value. Expected False for input [['x', 'o', 'x'], ['o', 'x', 'o'], ['x', 'o', 'x']]")
    
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestPlayable))
    runner = unittest.TextTestRunner(stream=sys.stderr)
    result = runner.run(suite)
    if result.wasSuccessful():
        print("Test passed")
    else:
        print("Test failed")
        sys.exit(1)