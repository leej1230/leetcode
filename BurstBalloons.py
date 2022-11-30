class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]

        def dfs(left, right):
            if right - left < 0:
                return 0

            tmp_max = -1
            for i in range(left, right+1):
                p = nums[i]*nums[i-1]+nums[i]+1
                d = dfs(left, i-1) + dfs(i+1,right)
                tmp_max=max(tmp_max, p+d)
            return tmp_max
        return dfs(0, len(nums)-1)
        '''
        dp = {}

        def dfs(balloons):
            if len(balloons)==1:
                return balloons[0]
            
            if balloons in dp:
                return dp[balloons]
            
            tmp_max = -1
            for i in range(len(balloons)):
                b = balloons[i]
                if i==0:
                    tmp_max = max(tmp_max, (b*balloons[i+1])+dfs(balloons[:i]+balloons[i+1:]))
                    continue
                if i==len(balloons)-1:
                    tmp_max = max(tmp_max, (b*balloons[i-1])+dfs(balloons[:i]+balloons[i+1:]))
                    continue
                tmp_max = max(tmp_max, (balloons[i-1]*b*balloons[i+1])+dfs(balloons[:i]+balloons[i+1:]))

            dp[balloons] = tmp_max
            return tmp_max
        
        return dfs(tuple(nums))
        Make hashtable to save the maximum possible coin you can earn from given tuple
        
        def dfs(balloons(tuple)):
            base case -> when there is only one ballon
                return that amount
            memoization case -> balloons is in hashtable
                return that table
                
            initialize tmp_max with -1
            for i in range(len(balloons)):
                if i is not 0 or len(balloons)-1:
                    tmp_max = max(tmp_max, (ballons[i-1]*balloons[i+1])+dfs(balloons[:i]+balloons[i+1]))
                if i is 0:
                    tmp_max = max(tmp_max, balloons[i+1]+dfs(balloons[:i]+balloons[i+1]))
                if i is len(balloons)-1:
                    tmp_max = max(tmp_max, balloons[i-1]+dfs(balloons[:i]+balloons[i+1]))
            
            dp[balloons] = tmp_max
            return tmp_max
        
        return dfs(tuple(nums))
        ----------------------------
        add 1 to both sides of the array

        def dfs(left, right)
            if right - left < 0
                return 0

            tmp_max = -1
            for i in range(left, right+1):
                p = nums[i]*nums[i-1]+nums[i]+1
                d = dfs(left, i-1) + dfs(i+1,right)
                tmp_max=max(tmp_max, p+d)
            return tmp_max


        '''