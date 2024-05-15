from typing import List

# https://leetcode.com/problems/simplify-path/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def simplifyPath(self, path: str) -> str:
        char_list = path.split("/")
        result = []
        for c in char_list:
            match c:
                case "..":
                    result.pop()
                case ".":
                    continue
                case "":
                    result.append("/")
                case _:
                    if result and result[-1] == "/":
                        result.pop()
                    result.append("/" + c)
        if len(result) > 1 and result[-1] == "/":
            result.pop()
        return "".join(result)
