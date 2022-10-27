class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff=[]
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])
        print(sum(diff))
        if sum(diff) < 0:
            return -1
        ans = -1
        total = 0
        for ind,val in enumerate(diff):
            if(total == 0 and total+val >= 0):
                ans = ind
                total += val
                continue
            if(total+val < 0):
                total = 0
                continue
            total += val
        return ans