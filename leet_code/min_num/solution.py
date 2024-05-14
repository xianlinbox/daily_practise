from typing import List

# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        previous = points[0]
        overlaps = []
        for i in range(1, len(points)):
            current = points[i]
            if current[0] <= previous[1]:
                previous = [current[0], min(previous[1], current[1])]
                continue
            overlaps.append(previous)
            previous = current
        overlaps.append(previous)
        return len(overlaps)
