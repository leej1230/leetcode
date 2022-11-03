class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dp = {}
        for num in nums:
            if num in dp:
                return True
            else:
                dp[num] = 1
        return False