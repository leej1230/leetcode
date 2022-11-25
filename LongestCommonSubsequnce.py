class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text1)+1)] for _ in range(len(text2)+1)]
        for j in range(len(text1)-1, -1, -1):
            for i in range(len(text2)-1, -1, -1):
                if text1[j] == text2[i]:
                    # print(i,j)
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        '''
        make 2d dp array with len(text1)+1 X len(text2)+1 +1 for empty string, initialize with zero

        Do in buttom up way: from [len(text1)][len(text2)+1] to [0][0]
            If row and column is same number -> add 1 to diagnal value
            If they are different, copy the max value of down or right

        return dp[0][0]
        '''