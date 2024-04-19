from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i in range(0, len(ratings)):
            if i > 0:
                if ratings[i] > ratings[i - 1]:
                    candies[i] = candies[i - 1] + 1
                elif ratings[i] < ratings[i - 1]:
                    candies[i - 1] = candies[i] + 1
        return sum(candies)
