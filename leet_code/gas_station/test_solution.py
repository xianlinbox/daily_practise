import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_1(self):
        self.assertEqual(
            3,
            self.solution.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        )

    def test_case_1(self):
        self.assertEqual(
            -1,
            self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]),
        )

    # def test_case_2(self):
    #     self.assertEqual(
    #         -1,
    #         self.solution.canCompleteCircuit([2, 3, 4], [3, 4, 3]),
    #     )


if __name__ == "__main__":
    unittest.main()
