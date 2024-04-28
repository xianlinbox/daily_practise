from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        curr_value = 0
        result = n + 1
        left = 0
        for right in range(n):
            curr_value += nums[right]
            while curr_value >= target:
                result = min(result, right - left + 1)
                curr_value -= nums[left]
                left += 1
        if result == n + 1:
            return 0
        return result
