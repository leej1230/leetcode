class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for x in range(len(nums))]
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1,len(nums)):
                if(nums[i] < nums[j]):
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

        #Binary Tree Soluion
        sub = []
        for num in nums:
            i = bisect_left(sub, num)
            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num
            print(sub)
            print(i)
        return len(sub)