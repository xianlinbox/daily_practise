from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for i in range(1, len(prices)):
            current_price = prices[i]
            if current_price > buy_price:
                profit += current_price - buy_price
                buy_price = current_price
            elif current_price < buy_price:
                buy_price = current_price

        return profit
