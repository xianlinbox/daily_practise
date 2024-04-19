from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candies = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        ratings.reverse()
        for i in range(0, length - 1):
            candy_index = length - 1 - i
            if (
                ratings[i] < ratings[i + 1]
                and candies[candy_index - 1] <= candies[candy_index]
            ):
                candies[candy_index - 1] = candies[candy_index] + 1
        return sum(candies)
