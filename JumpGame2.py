class Solution:
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        # if l == 1 return 0
        
        # dp for length l zeros

        # for loop through end to the beginning
        #   If i+nums[i] >= (l-1)
        #       dp[i] = 1
        #   dp[i] = 1 + dp[i+1]

        # dp[0]

        l = len(nums)
        if l==1:
            return 0
        
        dp = [0]*l

        for i in range(l-2, -1, -1):
            if(nums[i]==0):
                dp[i] = 10**5
                continue
            if i+nums[i] >= (l-1):
                dp[i] = 1
            else:
                dp[i] = 1 + min(dp[i+1:i+1+nums[i]])
        
        return dp[0]