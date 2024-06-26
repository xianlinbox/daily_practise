import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.candy([1, 0, 2])
        self.assertEqual(5, result)

    def test_case_1(self):
        self.assertEqual(
            4,
            self.solution.candy([1, 2, 2]),
        )

    def test_case_2(self):
        result = self.solution.candy([1, 1, 1])
        self.assertEqual(3, result)

    def test_case_3(self):
        result = self.solution.candy([1, 2, 3, 3, 5, 5])
        self.assertEqual(10, result)

    def test_case_4(self):
        result = self.solution.candy([1, 2, 87, 87, 87, 2, 1])
        self.assertEqual(13, result)

    def test_case_5(self):
        result = self.solution.candy([4, 3, 2, 1])
        self.assertEqual(10, result)


if __name__ == "__main__":
    unittest.main()
