from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        left = 0
        str_array = list(s)
        n = len(str_array)
        result_len = 0
        for right in range(n):
            result.append(str_array[right])
            while str_array[left] in result:
                print(left, right, result)
                result.remove(str_array[left])
                left += 1
            result_len = max(result_len, len(result))
        return result_len
