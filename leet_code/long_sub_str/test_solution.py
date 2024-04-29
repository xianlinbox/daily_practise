import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        result = self.solution.lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(3, result)

    def test_case_1(self):
        result = self.solution.lengthOfLongestSubstring("bbbbb")
        self.assertEqual(1, result)

    def test_case_2(self):
        result = self.solution.lengthOfLongestSubstring("pwwkew")
        self.assertEqual(3, result)


if __name__ == "__main__":
    unittest.main()
