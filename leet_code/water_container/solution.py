from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = min(height[i], height[j]) * (j - i)
        while i < j:
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
            if min(height[i], height[j]) * (j - i) > max_area:
                max_area = min(height[i], height[j]) * (j - i)

        return max_area
