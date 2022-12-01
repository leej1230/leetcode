class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sInd = 0
        for c in t:
            if sInd==len(s):
                return True
            if c==s[sInd]:
                sInd+=1
        return sInd==len(s)