import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        self.assertEqual(2, self.solution.jump([2, 3, 1, 1, 4]))

    def test_case_2(self):
        self.assertEqual(2, self.solution.jump([2, 3, 0, 1, 4]))

    def test_case_3(self):
        self.assertEqual(1, self.solution.jump([3, 1]))

    def test_case_7(self):
        self.assertEqual(1, self.solution.jump([1, 0]))

    def test_case_4(self):
        self.assertEqual(3, self.solution.jump([1, 3, 1, 4, 1, 1, 1]))

    def test_case_5(self):
        self.assertEqual(0, self.solution.jump([0]))

    def test_case_6(self):
        self.assertEqual(0, self.solution.jump([1]))

    def test_case_8(self):
        self.assertEqual(2, self.solution.jump([1, 2, 3]))

    def test_case_9(self):
        self.assertEqual(
            2, self.solution.jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])
        )


if __name__ == "__main__":
    unittest.main()
