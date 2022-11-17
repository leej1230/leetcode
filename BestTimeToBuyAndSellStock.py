class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = -1
        max_profit = 0
        for price in prices:
            min_price = min(price, min_price)
            temp_profit = price - min_price
            max_profit = max(max_profit, temp_profit)
        return max_profit

'''
        Initialize answer with 0
        
        create variable for min number initialized with first element
        
        for loop through array from 1 to l
            ans = max(ans, curr val-min number)
            
            if current position has smaller number than min number
            
        return ans
'''