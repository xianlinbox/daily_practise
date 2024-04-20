from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i + 1, len(height)):
                h = min(height[i], height[j])
                if h * (j - i) > max_area:
                    max_area = h * (j - i)

        return max_area
