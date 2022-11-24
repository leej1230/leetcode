class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        for i in range(2,numRows+1):
            tmp = []
            for j in range(i):
                if j==0 or j==(i-1):
                    tmp.append(1)
                    continue
                tmp.append(ans[i-2][j-1]+ans[i-2][j])
            ans.append(tmp)
        return ans