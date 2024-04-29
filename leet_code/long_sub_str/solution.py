from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_array = list(s)
        n = len(str_array)
        result = []
        left = 0
        result_len = 0
        for right in range(n):
            curr_item = str_array[right]
            while curr_item in result:
                result.remove(str_array[left])
                left += 1
            result.append(curr_item)
            result_len = max(result_len, right - left + 1)
        return result_len
