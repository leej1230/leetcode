class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        #max_profit = 0
        total_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            if (price - min_price) > 0:
                total_profit += (price - min_price)
                min_price = price
        return total_profit