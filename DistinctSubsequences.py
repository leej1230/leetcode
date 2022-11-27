class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1 = len(s)
        l2 = len(t)
        dp = {}
        def dfs(ind1, ind2):
            if (ind1, ind2) in dp:
                return dp[(ind1,ind2)]
            if ind2 == l2:
                return 1
            if ind1 == l1:
                return 0

            if s[ind1] == t[ind2]:
                dp[(ind1, ind2)] = dfs(ind1+1, ind2+1) + dfs(ind1+1, ind2)
            else:
                dp[(ind1, ind2)] = dfs(ind1+1, ind2)
            
            return dp[(ind1, ind2)]

        return dfs(0,0)