class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        l = len(nums)
        dp = {}
        def dfs(ind, total):
            if ind == l:
                if total == target:
                    return 1
                return 0
            
            if (ind,total) in dp:
                return dp[(ind,total)]
            
            tmp_sol = dfs(ind+1, total+nums[ind]) + dfs(ind+1, total-nums[ind])
            dp[(ind,total)] = tmp_sol
            return dp[(ind,total)]
        
        return dfs(0,0)