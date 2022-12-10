class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lengthString = len(s)
        l,r = 0,0
        dp = {}
        answer = -1
        while r<lengthString:
            dp[s[r]] = dp.get(s[r], 0) + 1
            lengthWindow = r-l+1
            maxFrequency = max(list(dp.values()))
            if lengthWindow - maxFrequency <= k:
                #valid window
                r += 1
                answer = max(answer, lengthWindow)
            else:
                dp[s[l]] -= 1
                dp[s[r]] -= 1 #avoid counting double
                l += 1
        return answer
        # def dfs(ind,l,k):
        #     new_k = k
        #     if ind == lengthString:
        #         return ind
        #     if s[ind] != l:
        #         if k == 0:
        #             return ind
        #         new_k -= 1
        #     return dfs(ind+1,l,new_k)
        
        # answer = -1

        # for i in range(lengthString):
        #     if lengthString-i < answer:
        #         return answer
        #     answer = max(answer, (dfs(i,s[i],k)-i))

        # return answer
        '''
        dfs(ind,l,k):
            if current index is different with letter
                if k is 0 then return ind-1
                else subtract k by 1
            return dfs(ind+1,l,new_k)

        Iterate through each letter
            if len(s)-current index < answer -> no need to consider others, simply return answer
            use dfs get into maximum depth you can reach from there
        
        Problem with solution above -> it is one-sided solution (gets error on ABBB)

        ---------After watching Neetcode--------
        l,r = 0,0
        dp = {}
        answer = -1
        while r<lengthString:
            dp[s[r]] = dp.get(s[r], 0) + 1
            lengthWindow = r-l+1
            maxFrequency = max(list(dp.values()))
            if lengthWindow - maxFrequency <= k:
                #valid window
                r += 1
                answer = max(answer, lengthWindow)
            else:
                dp[s[l]] -= 1
                l += 1
        return answer
        '''