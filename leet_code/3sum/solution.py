from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, item in enumerate(nums):
            target = 0 - item
            i = index + 1
            j = len(nums) - 1
            while True:
                if i >= j:
                    break
                if nums[i] + nums[j] == target:
                    if [nums[index], nums[i], nums[j]] not in result:
                        result.append([nums[index], nums[i], nums[j]])
                    i = i + 1
                    j = j - 1
                elif nums[i] + nums[j] > target:
                    j = j - 1
                else:
                    i = i + 1

        return result
