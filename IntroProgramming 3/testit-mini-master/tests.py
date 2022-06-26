"""Unit tests for testme.py"""

import unittest
from buggy import *

class TestMaxRun(unittest.TestCase):

    def test_max_run_example(self):
        self.assertEqual(max_run([1, 2, 2, 2, 3]), [2, 2, 2])
        #I had the exact same error while sweeping my list so
        #these were the first I looked for
    def test_max_run_all_same_int(self):
        self.assertEqual(max_run([2, 2, 2, 2, 2]), [2, 2, 2, 2, 2])
    def test_max_run_empty_list(self):
        self.assertEqual(max_run([]), [])

if __name__ == "__main__":
    unittest.main()

