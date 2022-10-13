class Solution:
    def palindrome_recursion(self, ind: int, end_ind: int, s: str) -> bool:
        while 97 > ord(s[ind]) or 122 < ord(s[ind]):
            ind += 1
        while 97 > ord(s[end_ind]) or 122 < ord(s[end_ind]):
            end_ind -= 1
        if(ind == end_ind):
            return True
        if(abs(end_ind - ind) == 1) and s[ind] == s[end_ind]:
            return True
        if(s[ind] != s[end_ind]):
            return False
        else:
            return self.palindrome_recursion(ind+1, end_ind-1, s)

    def isPalindrome(self, s: str) -> bool:
        a = s.lower()
        a = ''.join(ch for ch in a if ch.isalnum())
        if(len(a)==0 or len(a)==1):
            return True
        return self.palindrome_recursion(0, len(a)-1, a)