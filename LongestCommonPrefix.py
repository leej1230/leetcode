class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        f = strs[0]
        for s in strs[1:]:
            m = min(len(f),len(s))
            tmp = ""
            for i in range(m):
                if(f[i] == s[i]):
                    tmp += f[i]
                else:
                    break
            f = tmp
        return f