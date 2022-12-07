class Solution:
    def checkValidString(self, s: str) -> bool:
        stringLength = len(s)
        dp = {}
        def dfs(ind, leftBracket):

            if (ind,leftBracket) in dp:
                return dp[(ind,leftBracket)]

            if leftBracket<0:
                dp[(ind,leftBracket)] = False
                return False
            if ind == stringLength:
                if leftBracket==0:
                    return True
                return False

            if s[ind]=="(":
                dp[(ind,leftBracket)] = dfs(ind+1, leftBracket+1)
                return dp[(ind,leftBracket)]
            if s[ind]==")":
                dp[(ind,leftBracket)] = dfs(ind+1, leftBracket-1)
                return dp[(ind,leftBracket)]
            if s[ind]=="*":
                dp[(ind,leftBracket)] = dfs(ind+1, leftBracket+1) or dfs(ind+1, leftBracket-1) or dfs(ind+1, leftBracket)
                return dp[(ind,leftBracket)]
        return dfs(0,0)
        '''
        use backtrack method
        backtrack(ind, leftBracket)
            return False if leftBracket is less than 0

            if ind == len(s)
                leftBracket == 0:
                    return True
                return False
            
            if s[ind]==(
                return backtrack(ind+1, leftBracket+1)
            if s[ind]==)
                return backtrack(ind+1, leftBracket-1)
            if s[ind]==*
                return backtrack(ind+1, leftBracket+1) or backtrack(ind+1, leftBracket-1) or backtrack(ind+1, leftBracket)
        '''