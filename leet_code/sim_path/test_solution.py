import unittest
from solution import Solution


class TestJump(unittest.TestCase):
    solution = Solution()

    def test_case_0(self):
        path = "/home/"
        result = self.solution.simplifyPath(path)
        expected = "/home"
        self.assertEqual(expected, result)

    def test_case_1(self):
        path = "/home//foo/"
        result = self.solution.simplifyPath(path)
        expected = "/home/foo"
        self.assertEqual(expected, result)

    def test_case_2(self):
        path = "/home/user/Documents/../Pictures"
        result = self.solution.simplifyPath(path)
        expected = "/home/user/Pictures"
        self.assertEqual(expected, result)

    def test_case_3(self):
        path = "/../"
        result = self.solution.simplifyPath(path)
        expected = "/"
        self.assertEqual(expected, result)

    def test_case_4(self):
        path = "/.../a/../b/c/../d/./"
        result = self.solution.simplifyPath(path)
        expected = "/.../b/d"
        self.assertEqual(expected, result)

    def test_case_5(self):
        path = "/a/../../b/../c//.//"
        result = self.solution.simplifyPath(path)
        expected = "/c"
        self.assertEqual(expected, result)

    def test_case_6(self):
        path = "/a//b////c/d//././/.."
        result = self.solution.simplifyPath(path)
        expected = "/a/b/c"
        self.assertEqual(expected, result)

    def test_case_7(self):
        path = "/a/.."
        result = self.solution.simplifyPath(path)
        expected = "/"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
