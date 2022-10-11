class Solution:
    def __init__(self):
        self.d = {}
        self.d[1] = [1]
        self.d[2] = [1,1]

    def recursion_pascal(self, row: int) -> List[int]:
        # if(row == 1):
        #     return [1]
        # if(row == 2):
        #     return [1,1]
        if row in self.d:
            return self.d[row]
        else:
            prev_row = self.recursion_pascal( row - 1 )
        
        tmp = [1]
        # prev_row = self.recursion_pascal(row - 1)
        for x in range(1,row - 1):
            tmp.append(prev_row[x-1] + prev_row[x])
        tmp.append(1)
        self.d[row] = tmp
        return tmp

    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for num in range(1,numRows+1):
            ans.append(self.recursion_pascal(num))
        return ans