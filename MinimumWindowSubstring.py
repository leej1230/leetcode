class Solution:
    def minWindow(self, s: str, t: str) -> str:
        answer = float('inf')
        answerRange = (0,0)
        dp = {}
        for ch in t:
            dp[ch] = dp.get(ch, 0) + 1
        
        def checkZero(h):
            for v in h.values():
                if v>0:
                    return False
            return True
        
        l,r = 0,0
        while r<len(s)+1:
            isValid = checkZero(dp)
            if isValid:
                if s[l] in dp:
                    dp[s[l]] += 1
                if r-l < answer:
                    answer = r-l
                    answerRange=(l,r)
                l += 1
            else:
                if r==len(s):
                    pass
                elif s[r] in dp:
                    dp[s[r]] -= 1
                r += 1
        if answer != float('inf'):
            return s[answerRange[0]:answerRange[1]]
        else:
            return ""

        '''
        initialize answer with inf

        make hashmap that contains all the letters in t

        def checkZero(hashmap):
            iterate through the hashmap value
            return true if all the values are lower or equal to 0
            else false

        l,r = 0
        while r<len(s):
            isValid = checkZero(hashmap)
            when the window is valid (isValid == true)
                increment the counter in hashmap if left was at letter thats in t
                shift left pointer
                update the answer with minimum value
            when the window is invalid
                decrement the counter in hashmap
                shift right pointer
        '''