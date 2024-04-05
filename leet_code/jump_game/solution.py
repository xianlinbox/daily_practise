from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        stop_point = len(nums) - 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] == 0:
                if i >= 1 and nums[i - 1] > 1:
                    i += nums[i - 1] - 1
                    continue
                else:
                    stop_point = i
                    break
            i += 1
        return stop_point >= len(nums) - 1
