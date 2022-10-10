class Solution:
    def __init__(self) -> None:
        self.d = {}
        self.d[0] = 0
        self.d[1] = 1
    def fib(self, n: int) -> int:
        # if(n == 0):
        #     return 0
        # if(n == 1):
        #     return 1
        # return self.fib(n-1) + self.fib(n-2)
        # Sloooooow Method
        
        # Memoization
        if n in self.d:
            return self.d[n]
        else:
            self.d[n] = self.fib[n-1] + self.fib[n-2]
            return self.d[n]
