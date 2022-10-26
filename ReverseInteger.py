class Solution:
    def reverse(self, x: int) -> int:
        if(x<0):
            a = x*-1
            b = int(str(a)[::-1]) * -1
            return 0 if b > pow(2, 31) or b < -pow(2, 31) else b
        b = int(str(x)[::-1])
        return 0 if b > pow(2, 31) or b < -pow(2, 31) else b