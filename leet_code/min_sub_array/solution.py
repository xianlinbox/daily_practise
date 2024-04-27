from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left_index = 0
        right_index = -1
        curr_value = 0
        for i in range(n):
            curr_value += nums[i]
            if curr_value >= target:
                right_index = i
                break

        if right_index == -1:
            return 0
        else:
            result = right_index - left_index + 1
            while right_index < n:
                print(left_index, right_index, curr_value, result)
                if curr_value >= target:
                    result = min(right_index - left_index + 1, result)
                    curr_value -= nums[left_index]
                    left_index += 1
                else:
                    right_index += 1
                    curr_value += nums[right_index]

            return result
