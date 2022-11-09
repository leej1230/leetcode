class Solution:
    def isHappy(self, n: int) -> bool:
        df = {x:x*x for x in range(10)}
        
        curr = str(n)
        seen = set()
        while True:
            total = 0
            for i in curr:
                total += df[int(i)]
            if (total == 1):
                return True
            elif total in seen:
                return False
            else:
                seen.add(total)
                curr = str(total)