class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 0
        Iszero = False
        ans = []
        for x in nums:
            if x != 0 and total == 0:
                total = x
            elif x != 0:
                total *= x
            elif Iszero:
                total = 0
                break
            else:
                Iszero = True
        if Iszero:
            for v in nums:
                if(v):
                    ans.append(0)
                else:
                    ans.append(total)
            return ans
        else:
            for v in nums:
                ans.append(int(total/v))
        return ans