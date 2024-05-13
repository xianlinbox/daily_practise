from typing import List

# https://leetcode.com/problems/insert-interval/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(intervals[i][1], end)
            else:
                result.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
        result.append([start, end])
        return result
