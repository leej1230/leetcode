class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        ans = 0
        ind = 0
        while ind < l:
            ans += 1
            left_ind = ind - 1
            right_ind = ind + 1
            while (left_ind > -1 and right_ind < l) and (s[left_ind] == s[right_ind]):
                ans += 1
                left_ind -= 1
                right_ind += 1
            
            if(ind != l-1) and (s[ind] == s[ind+1]):
                ans += 1
                left_ind = ind - 1
                right_ind = ind + 2
                while (left_ind > -1 and right_ind < l) and (s[left_ind] == s[right_ind]):
                    ans += 1
                    left_ind -= 1
                    right_ind += 1
            ind += 1
        return ans