from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and len(nums) > 1:
            return False

        left_steps = 1
        for i in range(0, len(nums) - 1):
            if nums[i] == 0 and left_steps == 0:
                return False

            if nums[i] > left_steps:
                left_steps = nums[i]
            left_steps = left_steps - 1

        return True

    def jump(self, nums: List[int]) -> int:
        left_steps = len(nums) - 1
        jump_steps = 0
        count = 0
        for i in range(0, len(nums)):
            if jump_steps >= left_steps:
                # count += 1
                break
        return count
