from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_array = list(s)
        n = len(str_array)
        result = []
        left = 0
        result_len = 0
        for right in range(n):
            while str_array[right] in result:
                print(left, right, result)
                result.remove(str_array[left])
                left += 1
            result.append(str_array[right])
            result_len = max(result_len, len(result))
        return result_len
