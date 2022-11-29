class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sLength = len(s)
        pLength = len(p)
        
        dp = {}
        
        def dfs(sInd, pInd):
            if (sInd,pInd) in dp:
                return dp[(sInd,pInd)]
            
            if sInd >= sLength and pInd >= pLength:
                return True
            
            if pInd >= pLength:
                return False
            
            match = (sInd<sLength) and (s[sInd]==p[pInd] or p[pInd]==".")
            
            if pInd+1<pLength and p[pInd+1]=="*":
                dp[(sInd,pInd)] = (match and dfs(sInd+1,pInd)) or dfs(sInd,pInd+2)
                return dp[(sInd,pInd)]
            
            if match:
                dp[(sInd,pInd)] = dfs(sInd+1,pInd+1)
                return dp[(sInd,pInd)]
            
            dp[(sInd,pInd)] = False
            return dp[(sInd,pInd)]
        
        return dfs(0,0)
        '''
        sLength
        pLength

        def dfs(sInd, pInd):
            implement memoization

            if sInd AND pInd is equal to sLength, pLength
                return True
            sLength is equal to sInd then Fail
            pLength is equal to pInd then Fail

            if letter in sInd and pInd is same OR pInd is ".":
                return dfs(sInd+1, pInd+1)
            
            ---If they weren't same -> 2 cases:  1.pInd is * 2.they have different letter

            if pInd is "*":
                if letter in sInd is same as letter in pInd-1 OR pInd-1 is .
                    return dfs(sInd+1, pInd+1) or dfs(sInd+1, pInd)
            
            return False
        '''