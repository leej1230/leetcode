class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if n==1:
            return min(costs[0])
        
        for i in range(n-2,-1,-1):
            costs[i][0] = costs[i][0] + min(costs[i+1][1],costs[i+1][2])
            costs[i][1] = costs[i][1] + min(costs[i+1][0],costs[i+1][2])
            costs[i][2] = costs[i][2] + min(costs[i+1][0],costs[i+1][1])
        
        return min(costs[0])