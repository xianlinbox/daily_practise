import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        self.assertTrue(self.solution.canJump([2, 3, 1, 1, 4]))

    def test_case_2(self):
        self.assertFalse(self.solution.canJump([3, 2, 1, 0, 4]))

    def test_case_3(self):
        self.assertTrue(self.solution.canJump([1]))

    def test_case_4(self):
        self.assertTrue(self.solution.canJump([0]))

    def test_case_5(self):
        self.assertTrue(self.solution.canJump([3, 2, 2, 0, 4]))

    def test_case_6(self):
        self.assertTrue(self.solution.canJump([3, 2, 3, 0, 0, 4]))

    def test_case_7(self):
        self.assertFalse(self.solution.canJump([3, 2, 3, 0, 0, 0, 4]))

    def test_case_8(self):
        self.assertFalse(self.solution.canJump([3, 2, 2, 0, 0, 4]))

    def test_case_9(self):
        self.assertFalse(self.solution.canJump([0, 1]))

    def test_case_10(self):
        self.assertTrue(self.solution.canJump([2, 0, 0]))

    def test_case_11(self):
        self.assertTrue(self.solution.canJump([3, 0, 8, 2, 0, 0, 1]))


if __name__ == "__main__":
    unittest.main()
