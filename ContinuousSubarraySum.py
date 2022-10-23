class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        dp = {}
        total = 0
        for i in range(0,len(nums)):
            total += nums[i]
            rem = total%k
            if rem == 0 and i>0:
                return True
            if rem in dp:
                if i - dp[rem] > 1:
                    return True
            else:
                dp[rem] = i
        return False