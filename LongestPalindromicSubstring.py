class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        length = len(s)
        for i in range(length):
            #odd cases
            left,right = i,i
            while left>-1 and right<len(s) and s[left]==s[right]:
                if right-left+1 > len(ans):
                    ans = s[left:right+1]
                left -= 1
                right += 1
            
            #even cases
            left,right = i,i+1
            while left>-1 and right<len(s) and s[left]==s[right]:
                if right-left+1 > len(ans):
                    ans = s[left:right+1]
                left -= 1
                right += 1
        return ans
        '''
        Get the length of string

        initialize answer with empty string

        Go through each element in array
            For odd length ones -> set l and r to center
            while l and r are in bound and equal to each other
                add 1 to r and -1 to l
                Check the result if its bigger than current answer

            For even cases -> set left to i right to i+1
            same code as odd cases
                Check the result
        
        return answer
        '''