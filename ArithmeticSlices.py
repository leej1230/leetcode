class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l = len(nums)
        if l<3:
            return 0
        dp = [0]*l
        
        for i in range(1,l-1):
            if (nums[i]-nums[i-1]) == (nums[i+1]-nums[i]):
                dp[i] = dp[i-1] + 1
        
        return sum(dp)
        '''
        l = len(nums)
        Get 1d array with length of l initialized with 0

        Use three size window
        Starting from i=0,1,2 go until l-3,l-2,l-1
        middle-first is equal to end-middle -> add 1 to dp[i-1] and update dp[i]

        return the sum of dp
        '''