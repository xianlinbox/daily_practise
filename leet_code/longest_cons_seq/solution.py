from typing import List

# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        number_count = len(nums)
        start_point = 0
        seq_length = -1
        for i in range(number_count - 1):
            print(start_point, seq_length)
            if nums[i + 1] == nums[i]:
                start_point += 1
            elif nums[i + 1] != nums[i] + 1:
                seq_length = max(i - start_point + 1, seq_length)
                start_point = i + 1

        return max(seq_length, number_count - start_point)
