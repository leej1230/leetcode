class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prev = [1]
        if rowIndex==0:
            return prev
        for i in range(rowIndex+1):
            ans = []
            for j in range(i+1):
                if j==0 or j==i:
                    ans.append(1)
                    continue
                ans.append(prev[j-1]+prev[j])
            prev = ans
        return ans