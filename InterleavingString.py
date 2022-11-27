class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1+l2 != len(s3):
            return False
        dp = [[False for _ in range(l2+1)] for _ in range(l1+1)]
        dp[l1][l2] = True

        for i in range(l1, -1, -1):
            for j in range(l2, -1, -1):
                if i<l1 and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j<l2 and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]
'''
Check if the length of s1+s2 be s3

make 2d array initialized everything with false
right bottom corner should be True

Iterate through from right bottom corner to left upper corner
    if the position right now matches with letter of s3 AND down/bottom is true then set array to true
return dp 0,0

---- Prev Solution (forgot to memoize) ------
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1==0 and l2==0:
            if s3=="":
                return True
            return False
        if l1+l2 != len(s3):
            return False
        def dfs(ind1, ind2, curr_string):
            if ind1==l1 and ind2==l2:
                if curr_string[-1] == s3[-1]:
                    return True
                return False
            
            if ind1>0 or ind2>0:
                if curr_string[-1] != s3[ind1+ind2-1]:
                    return False
            if ind1==l1:
                return dfs(ind1,ind2+1,curr_string.join(s2[ind2]))
            if ind2==l2:
                return dfs(ind1+1,ind2,curr_string.join(s1[ind1]))
            
            return dfs(ind1+1,ind2,curr_string.join(s1[ind1])) or dfs(ind1,ind2+1,curr_string.join(s2[ind2]))
        return dfs(0,0,"")
'''