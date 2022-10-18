class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        if(n==0):
            return ans
        
        for x in range(1,n+1):
            ind = int(x/2)
            if(x%2):
                # x is odd
                ans.append(ans[ind]+1)
            else:
                # x is even
                ans.append(ans[ind])
        return ans