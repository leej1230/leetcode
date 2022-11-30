class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def backtrack(strPar, openPar, closePar):
            if openPar < closePar:
                return
            if openPar > n:
                return
            if openPar==n and closePar==n:
                answer.append(strPar)
            
            backtrack("".join([strPar,"("]), openPar+1, closePar)
            backtrack("".join([strPar,")"]), openPar, closePar+1)
            return
        
        backtrack("(", 1, 0)
        return answer
        '''
        answer = []
        def backtrack(strPar, openPar, closePar):
            if number of openPar is smaller than closePar:
                It will be not well-formed parentheses -> return (do nothing)
            if openPar is bigger than n:
                It will have extra parentheses -> return (do nothing)
            if openPar and closePar equals to n:
                Satisfies the condition -> append strPar to solution
            
            backtrack(strPar.join("("), openPar+1, closePar)
            backtrack(strPar.join(")"), openPar, closePar+1)
            return
        
        backtrack("(", 1, 0)
        '''