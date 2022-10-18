class Solution:
    def numDecodings(self, s: str) -> int:
        d = {len(s):1}

        for i in range(len(s)-1, -1, -1):
            if(s[i] == "0"):
                d[i] = 0
            else:
                d[i] += d[i+1]
            
            if(( i < len(s)-1 ) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                d[i] += d[i+2]
        
        return d[0]