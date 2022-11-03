class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dp = {}
        for i in len(s):
            dp[s[i]] = 1 + dp.get(s[i],0)
            dp[t[i]] = dp.get(t[i],0) - 1
        for _,val in dp.items():
            if val != 0:
                return False
        return True