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
        furthest = 0
        end = 0
        count = 0
        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                break

            furthest = max(furthest, i + nums[i])
            if furthest >= len(nums) - 1:
                count += 1
                break

            if i == end:
                count += 1
                end = furthest
        return count
