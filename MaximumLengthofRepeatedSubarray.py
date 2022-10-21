class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N,M = len(nums1), len(nums2)
        dp = [[0 for x in range(M + 1)] for y in range(N + 1)]
        ans = 0
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    ans = max(ans, dp[i][j])
        return ans