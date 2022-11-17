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
    
'''
    Initilaize the answer 0
    
    minimum number initialized with first price
    
    for loop through from 1 to end
        when the curr value is smaller than minimum number, update
        when the curr value is bigger than minimum number, add the difference to the answer and update minimum number with curr value
    
    return ans
'''