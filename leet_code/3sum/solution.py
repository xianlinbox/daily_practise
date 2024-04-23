from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = len(nums) - 1
        k = j / 2
        result = []
        while True:
            if i >= k and j <= k:
                break
            if nums[i] + nums[k] + nums[j] >0:
                
            elif nums[i] + nums[k] + nums[j] == 0:
                result.append([i, j, k])
