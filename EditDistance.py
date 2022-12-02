class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]
        
        for x in range(l2):
            dp[-1][x] = l2-x
            
        for x in range(l1):
            dp[x][-1] = l1-x
            
        
        
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = min(dp[i+1][j+1], 1+dp[i+1][j], 1+dp[i][j+1])
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        '''
        2d dp array initialized with 0s
        len(dp) -> len(word1)+1
        len(dp[0]) -> len(word2)+1

        dp[-1] = fill with decreasing order of len(word2)
        for each dp[i][-1] = fill with decreasing numbers of len(word1)

        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j] = min(dp[i+1][j+1], 1+dp[i+1][j], 1+dp[i][j+1])
                else:
                    dp[i][j] = 1 + min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        '''