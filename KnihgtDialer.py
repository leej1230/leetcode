class Solution:
    def knightDialer(self, n: int) -> int:
        move = {
            0: [4,6],
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [0,3,9],
            6: [0,1,7],
            7: [2,6],
            8: [1,3],
            9: [2,4]
        }
        dp = [[0 for b in range(10)] for a in range(n+1)]
        for i in range(0,n+1):
            for x in range(10):
                if(x==5):
                    if(i==0):
                        dp[i][x] = 1
                    continue
                if(i == 0):
                    dp[i][x] = 1
                else:
                    for j in move[x]:
                        dp[i][x] += dp[i-1][j]
        return sum(dp[n-1])%(10**9 + 7)