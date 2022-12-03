class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ls = len(s)
        dp = [[0 for _ in range(ls+1)] for _ in range(ls+1)]
        revs = s[::-1]
        for i in range(ls-1,-1,-1):
            for j in range(ls-1,-1,-1):
                if(revs[i]==s[j]):
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]
        '''
        Iterate through the string

        2d array with s and reversed s
        '''