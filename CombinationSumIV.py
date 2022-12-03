class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        dp = [0 for _ in range(target+1)]
        for t in range(1,target+1):
            for num in nums:
                if num>t:
                    break
                if t==num:
                    dp[t] += 1
                else:
                    dp[t] += dp[t-num]
        return dp[target]