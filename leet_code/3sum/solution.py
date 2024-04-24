from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for first in range(n):
            if nums[first] > 0:
                break
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            target = 0 - nums[first]
            i = first + 1
            j = n - 1

            while i < j:
                total = nums[i] + nums[j]
                if total == target:
                    result.append([nums[first], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif total < target:
                    i += 1
                else:
                    j -= 1

        return result
