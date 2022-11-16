class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        l = len(nums)
        pos_dp = [0]*l
        neg_dp = [0]*l
        
        if nums[0] > 0:
            pos_dp[0] = 1
        
        if nums[0] < 0:
            neg_dp[0] = 1
            
        ans = pos_dp[0]

        for i in range(1,l):
            if nums[i] < 0:
                neg_dp[i] = pos_dp[i-1]+1
                if neg_dp[i-1] > 0:
                    pos_dp[i] = neg_dp[i-1]+1
                
            if nums[i] > 0:
                pos_dp[i] = pos_dp[i-1]+1
                if neg_dp[i-1] > 0:
                    neg_dp[i] = neg_dp[i-1]+1
                
            ans = max(ans, pos_dp[i])
        return ans

        '''
        PSEUDOCODE
        Create two dp array with length l
            One for counting max subarray for positive product
            One for countring max subarray for negative product
        
        Initialize the array
            If first element is positive -> add 1 to pos prod dp 0
            If first element is negative -> add 1 to neg prod dp 0
        
        Initialize answer with pos prod dp [0]

        For loop through 1 to l
            If the current value is negative
                Add 1 to prev pos prod dp and input to current neg dp
                
                If prev neg dp exist, add 1 and input to curr positive dp

            If the current value is positive
                Add 1 to prev pos prod dp and input to current pos dp
                If prev neg dp exist, add 1 and input to curr negative dp
            Update answer with max(curr ans, pos dp curr)
        '''