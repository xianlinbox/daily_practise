from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = []

        for i in range(0, len(ratings)):
            candies[i] = 1
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        return sum(candies)
