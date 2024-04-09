import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        self.assertEqual(6, self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_case_2(self):
        self.assertEqual(9, self.solution.trap([4, 2, 0, 3, 2, 5]))

    def test_case_3(self):
        self.assertEqual(0, self.solution.trap([1]))

    def test_case_4(self):
        self.assertEqual(1, self.solution.trap([1, 0, 1]))

    def test_case_5(self):
        self.assertEqual(1, self.solution.trap([1, 0, 3]))


if __name__ == "__main__":
    unittest.main()
