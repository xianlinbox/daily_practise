import unittest
from merge_sorted_array import Solution


class TestMergeSortedArray(unittest.TestCase):
    solution = Solution()

    def test_2_normal_array(self):
        array_1 = [1, 2, 3, 0, 0, 0]
        self.solution.merge(array_1, 3, [2, 5, 6], 3)
        self.assertEqual(array_1, [1, 2, 2, 3, 5, 6])

    def test_array_2_empty(self):
        array_1 = [1]
        self.solution.merge(array_1, 1, [], 0)
        self.assertEqual(array_1, [1])

    def test_array_1_empty(self):
        array_1 = [0]
        self.solution.merge(array_1, 0, [1], 1)
        self.assertEqual(array_1, [1])


if __name__ == "__main__":
    unittest.main()
