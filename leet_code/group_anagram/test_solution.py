import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = self.solution.groupAnagrams(strs)
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        self.assertEqual(expected, result)

    def test_case_1(self):
        strs = [""]
        result = self.solution.groupAnagrams(strs)
        expected = [[""]]
        self.assertEqual(expected, result)

    def test_case_2(self):
        strs = ["a"]
        result = self.solution.groupAnagrams(strs)
        expected = [["a"]]
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
