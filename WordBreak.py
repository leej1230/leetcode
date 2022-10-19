class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {len(s): True}
        previous = len(s)
        for i in range(len(s)-1, -1, -1):
            if(s[i:] in wordDict): #OR if the whole stuff from head to the end exist in the dictionary, that's also true
                dp[i] = True
                previous = i
                continue
                
            if(s[i:previous] in wordDict): #If segment from head to the last word where there was word can be break into word
                if(dp[previous]): #And from that segment to after also has word
                    dp[i] = True
                    previous = i
                    continue

            dp[i] = False # If not applicable to both condition, then that's just the segment of word where cannot have all the words broken
        return dp[0]

        ###SOLUTION###
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if(i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]