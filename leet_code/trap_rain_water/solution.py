from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_max_heights = []
        current_left_max = 0
        for each_height in height:
            current_left_max = max(current_left_max, each_height)
            left_max_heights.append(current_left_max)

        height.reverse()
        right_max_heights = []
        current_right_max = 0
        for reverse_height in height:
            current_right_max = max(current_right_max, reverse_height)
            right_max_heights.append(current_left_max)
        result = 0
        for i in range(0, len(height)):
            result += min(left_max_heights[i], right_max_heights[i]) - height[i]

        return result
