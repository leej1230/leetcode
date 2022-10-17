class Solution:
    def climbStairs(self, n: int) -> int:
        d = {1:1, 2:2}
        def recursion_step(n: int) -> int:
            if n in d:
                return d[n]
            else:
                d[n] = recursion_step(n-1) + recursion_step(n-2)
            return d[n]
        return recursion_step(n)