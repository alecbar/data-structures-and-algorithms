import unittest
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    """Tests for binary search"""

    def test_1(self):
        """Test not found"""

        arr = [0, 1, 2, 3, 4, 5]
        item = 6

        self.assertEqual(None, binary_search(arr, item))

    def test_2(self):

        arr = [0, 1, 2, 3, 4, 5]
        item = 3

        self.assertEqual(3, binary_search(arr, item))



if __name__ == "__main__":
    unittest.main()