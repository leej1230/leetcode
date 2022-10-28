class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        for x in range(1,len(colors)):
            if colors[x] == colors[x-1]:
                ans += min(neededTime[x],neededTime[x-1])
                neededTime[x] = max(neededTime[x],neededTime[x-1])
        return ans