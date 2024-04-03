from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            if nums[i] >= len(nums) - (i + 1):
                return True
        return False
