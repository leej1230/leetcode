class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = -1
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            temp_profit = price - min_price
            max_profit = max(max_profit, temp_profit)
        return max_profit

