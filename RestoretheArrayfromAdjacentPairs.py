class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        dp = collections.defaultdict(list)
        ans = []
        for a,b in adjacentPairs:
            dp[a].append(b)
            dp[b].append(a)
        
        for key, arr in dp.items():
            if(len(arr) == 1):
                head = key
                break
        
        #dfs
        seen = set()
        def dfs(head):
            ans.append(head)
            nx = dp[head]
            seen.add(head)
            
            for num in nx:
                if num not in seen:
                    dfs(num)
                    
        dfs(head)
        return ans